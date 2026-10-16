---
project: gcc
subsystem: gcc
patch_id: null
tags:
- windows
- symlinks
- tar
- builds
discussion_id: SL2P216MB227161FE83EB9082BCFD3889EF9C2@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: Dereferencing symlinks in GCC snapshot source archives for Windows
headline: Dereferencing symlinks in GCC snapshot source archives for Windows
tldr: GCC snapshots for Windows contain symlinks that fail to extract on Windows,
  suggesting a need to dereference them during archive creation or remove them from
  t…
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Modifying the tar command to dereference symlinks might increase archive size.
- Removing the symlink by copying the file duplicates content, potentially increasing
  storage and maintenance overhead if the files diverge.
exchanges:
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Reports that GCC 17 snapshot archives contain symlinks that cause extraction
    failures on Windows, proposing solutions to dereference symlinks or remove them.
  quote: "When testing GCC 17 snapshot 17-20261011, the MSYS2 builds failed while\
    \ extracting the source archive with bsdtar [1]:\n\n  gcc-17.0.0+20261011/.github/PULL_REQUEST_TEMPLATE.md:\n\
    \  Can't create 'gcc-17.0.0+20261011/.github/PULL_REQUEST_TEMPLATE.md':\n  No\
    \ such file or directory\n\n.github/PULL_REQUEST_TEMPLATE.md is a symlink to CONTRIBUTING.md.\
    \ This means that extracting it on Windows with either GNU…"
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: reviewer
  position: Acknowledges the issue by quoting the proposer's description, indicating
    they have seen the problem.
  quote: "Hi,\n\nI am setting up GitHub Actions builds of GCC snapshots for MSYS2,\n\
    MinGW-w64, and Cygwin, using their existing package recipes.\n\nWhen testing GCC\
    \ 17 snapshot 17-20261011, the MSYS2 builds failed while\nextracting the source\
    \ archive with bsdtar [1]:\n\n  gcc-17.0.0+20261011/.github/PULL_REQUEST_TEMPLATE.md:\n\
    \  Can't create 'gcc-17.0.0+20261011/.github/PULL_REQUEST_TEMPLATE.md':\n  No\
    \ such file or di"
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Provides further context in response to Andrea Pinski's acknowledgment.
  quote: 'On Thu, Oct 15, 2026 at 6:09 AM Zhongteng Gui via Gcc <gcc@gcc.gnu.org>
    wrote:

    > ...

    > .github/PULL_REQUEST_TEMPLATE.md is a symlink to CONTRIBUTING.md. This means
    that extracting it on Windows with either GNU tar or bsdtar is likely broken,
    see [2].'
primer_expert: This discussion concerns the handling of symbolic links in GCC's snapshot
  tarball generation for Windows. Specifically, a symlink within the .github directory
  is causing extraction failures on Windows due to differences in how Windows tar
  utilities handle symlinks compared to Unix-like systems. The proposer suggests modifying
  the tar command or the source tree to resolve this.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SL2P216MB227161FE83EB9082BCFD3889EF9C2@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

A user setting up GitHub Actions builds for GCC snapshots on Windows encountered build failures due to symlinks in the source archive. Specifically, '.github/PULL_REQUEST_TEMPLATE.md' is a symlink to 'CONTRIBUTING.md', which causes extraction issues with tar on Windows. The user proposes either adding a --dereference flag when creating archives or removing the symlink by copying the file. This issue affects GCC 17 snapshots and is not yet present in mainline distributions.
