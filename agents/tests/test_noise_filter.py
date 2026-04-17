"""Tests for the deterministic noise filter."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from agents.models.raw import RawCommit, RawDiscussion
from agents.tools.noise_filter import (
    filter_noise,
    is_noise_commit,
    is_noise_discussion,
)


def _commit(msg: str) -> RawCommit:
    return RawCommit(
        sha="c" * 40,
        author="a@b",
        date=datetime(2026, 4, 16, tzinfo=timezone.utc),
        message=msg,
        diff_stat="",
        url="https://example.com",
        source_type="github",
        project="gcc",
    )


def _discussion(body: str, diff_text: str | None = None) -> RawDiscussion:
    return RawDiscussion(
        id="x",
        title="Subject",
        body=body,
        author="a@b",
        date=datetime(2026, 4, 16, tzinfo=timezone.utc),
        url="https://example.com",
        replies=[],
        diff_text=diff_text,
        source_type="public_inbox",
    )


class TestCommitNoise:
    @pytest.mark.parametrize(
        "msg",
        [
            "Daily bump.",
            "Daily bump",
            "Update copyright years.",
            "Regenerate configure",
            "Bump version to 15.2",
            "Merge branch 'master' into devel",
            "Merge pull request #42 from user/branch",
        ],
    )
    def test_noise_dropped(self, msg: str):
        assert is_noise_commit(_commit(msg))

    @pytest.mark.parametrize(
        "msg",
        [
            "gcc/ipa: improve inlining for hot callers",
            "kernel/mm: fix TLB flush on arm64",
            "malloc: introduce ifuncs for malloc functions",
        ],
    )
    def test_real_commits_kept(self, msg: str):
        assert not is_noise_commit(_commit(msg))

    def test_empty_message_is_noise(self):
        assert is_noise_commit(_commit(""))


class TestDiscussionNoise:
    def test_short_body_no_diff_is_noise(self):
        assert is_noise_discussion(_discussion("+1", diff_text=None))

    def test_short_body_with_diff_kept(self):
        assert not is_noise_discussion(_discussion("ping", diff_text="diff --git …"))

    def test_substantial_body_kept(self):
        body = "x" * 250
        assert not is_noise_discussion(_discussion(body))


class TestFilterNoise:
    def test_counts(self):
        commits = [_commit("Daily bump."), _commit("gcc/ipa: fix something real")]
        discs = [_discussion("+1"), _discussion("x" * 250)]
        kept_d, kept_c, dropped_d, dropped_c = filter_noise(discs, commits)
        assert dropped_d == 1
        assert dropped_c == 1
        assert len(kept_d) == 1
        assert len(kept_c) == 1
