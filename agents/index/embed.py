"""Embedding provider for the Pulse index.

Root CLAUDE.md says all LLM traffic goes through OpenRouter. OpenRouter exposes
no embeddings endpoint, so embeddings are the one documented carve-out — see the
"Embeddings" note in CLAUDE.md. To keep that carve-out contained, every call
goes through the ``EmbeddingProvider`` protocol below and the concrete client
speaks the OpenAI-compatible ``/embeddings`` API, which OpenAI, Voyage, Mistral
and most self-hosted servers all implement. Switching provider is therefore two
environment variables, not a code change — and if OpenRouter ever ships
embeddings, it becomes a one-line default swap.

Cost context: the whole ~2,950-document corpus is roughly 1.5M tokens, about
$0.02 one-off at text-embedding-3-small rates, and the nightly delta is ~30
documents. Every call is logged to agents/output/usage.log through the same
``append_usage`` helper the digest agents use, so embedding spend shows up in
the one €5/month audit trail rather than in a blind spot.
"""

from __future__ import annotations

import logging
import os
import struct
from typing import Protocol, runtime_checkable

from agents._retry import retry_with_backoff
from agents.usage_log import append_usage

logger = logging.getLogger(__name__)

DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"
DEFAULT_EMBEDDING_BASE_URL = "https://api.openai.com/v1"

# The API rejects oversized batches, and a smaller batch loses less work to a
# retry. 64 short digest documents per request is comfortably inside every
# provider's limit.
_BATCH_SIZE = 64


@runtime_checkable
class EmbeddingProvider(Protocol):
    """Anything that can turn texts into fixed-width vectors."""

    model: str

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in input order."""
        ...


class OpenAICompatibleEmbeddings:
    """Embeddings via any OpenAI-compatible ``/embeddings`` endpoint."""

    def __init__(
        self,
        model: str | None = None,
        base_url: str | None = None,
        api_key: str | None = None,
    ) -> None:
        self.model = model or os.environ.get("EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL)
        self._base_url = base_url or os.environ.get(
            "EMBEDDING_BASE_URL", DEFAULT_EMBEDDING_BASE_URL
        )
        self._api_key = api_key or os.environ.get("EMBEDDING_API_KEY", "")
        self._client = None

    def _get_client(self):
        # Imported lazily so `--no-embeddings` builds and lexical-only queries
        # never need the openai package installed.
        if self._client is None:
            from openai import OpenAI

            if not self._api_key:
                raise RuntimeError(
                    "EMBEDDING_API_KEY is not set — run with --no-embeddings for a "
                    "lexical-only index, or export a key (see .env.example)."
                )
            self._client = OpenAI(base_url=self._base_url, api_key=self._api_key)
        return self._client

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        client = self._get_client()
        vectors: list[list[float]] = []
        for start in range(0, len(texts), _BATCH_SIZE):
            batch = texts[start : start + _BATCH_SIZE]
            response = retry_with_backoff(
                lambda b=batch: client.embeddings.create(model=self.model, input=b),
                label=f"embed[{start}:{start + len(batch)}]",
            )
            # Providers are permitted to return results out of order; `index`
            # is the field that says where each one belongs.
            ordered = sorted(response.data, key=lambda d: d.index)
            vectors.extend(list(d.embedding) for d in ordered)
            append_usage("index_embed", self.model, getattr(response, "usage", None))
        return vectors


def pack_vector(vector: list[float]) -> bytes:
    """Serialise an L2-normalised vector as little-endian float32.

    Normalising at write time turns query-time cosine similarity into a plain
    dot product, so the hot path does no per-document division.
    """
    norm = sum(v * v for v in vector) ** 0.5
    if norm > 0:
        vector = [v / norm for v in vector]
    return struct.pack(f"<{len(vector)}f", *vector)


def unpack_vector(blob: bytes) -> list[float]:
    """Inverse of :func:`pack_vector`."""
    return list(struct.unpack(f"<{len(blob) // 4}f", blob))


def build_provider() -> EmbeddingProvider:
    """Return the configured embedding provider."""
    return OpenAICompatibleEmbeddings()
