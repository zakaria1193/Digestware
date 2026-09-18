---
project: gcc
subsystem: maintainer-scripts
patch_id: null
tags:
- gcc
- documentation
- release-process
commit_hash: bef869c1b9b818d4ad27063e539b3c95c1691c67
source_type: github
author: Jakub Jelinek
headline: Fix online documentation installation after web docs update
tldr: Corrected a script that failed to install compressed PDF documentation due to
  a change in file compression handling.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `update_web_docs_git` script, used by GCC administrators to deploy
  online documentation, had a regression after a change removed the compression of
  `.pdf` files. The script's logic includes a `cmp -s` check followed by copying both
  the file and its `.gz` counterpart. When `.gz` files are absent, `cp $file.gz $DOCSDIR/$file.gz`
  fails. This patch adjusts the script to gracefully handle missing `.gz` files, resolving
  installation issues highlighted in the `gccadmin` mailing list.
primer_glossary:
- term: online documentation
  definition: User and developer documentation for the GCC compiler, typically hosted
    on the official GCC website. This includes manuals, architecture-specific options,
    and internals.
- term: maintainer-scripts
  definition: A collection of shell scripts used by the GCC project maintainers for
    various administrative tasks, such as updating the website, managing releases,
    and building documentation.
- term: PDF
  definition: Portable Document Format, a file format used to present documents in
    a manner independent of application software, hardware, and operating systems.
    GCC documentation includes PDF versions.
- term: gzip
  definition: A common file compression utility. The `.gz` extension indicates a file
    that has been compressed using gzip.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bef869c1b9b818d4ad27063e539b3c95c1691c67
date: '2026-09-17'
is_stub: true
stub_reason: low_score
---

A recent change that stopped compressing PDF files for web documentation installation inadvertently broke the installation process. The `update_web_docs_git` script now incorrectly attempts to copy non-existent `.gz` files, causing installation failures. This commit modifies the script to ignore `.gz` files that are not present, ensuring that web documentation, including PDFs, can be installed correctly.
