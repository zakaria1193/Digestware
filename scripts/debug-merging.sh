#!/usr/bin/env bash
# Run the agent pipeline end-to-end against public-inbox/gcc with a tiny
# discussion cap so thread merging in PublicInboxAdapter can be debugged
# cheaply. Extra flags are forwarded (e.g. --dry-run, --force, --since-hours).
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -f .env ]]; then
    set -a
    # shellcheck disable=SC1091
    source .env
    set +a
fi

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
    echo "error: OPENROUTER_API_KEY is not set." >&2
    echo "       put it in .env or export it, then retry." >&2
    exit 1
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    echo "warning: GITHUB_TOKEN is not set — GitHub fetches will hit the 60/h" >&2
    echo "         unauthenticated rate limit." >&2
fi

exec python -m agents.main \
    --since-hours 24 \
    --project gcc \
    --max-discussions 5 \
    "$@"
