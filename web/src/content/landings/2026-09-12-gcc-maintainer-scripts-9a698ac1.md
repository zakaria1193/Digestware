---
project: gcc
subsystem: gcc/maintainer-scripts
patch_id: null
tags:
- documentation
- maintainer-scripts
commit_hash: 9a698ac1bdabbb0420465959203f5fd3fd261b8f
source_type: github
author: Gerald Pfeifer
headline: Stop generating redundant compressed PDF documentation.
tldr: PDF documentation will no longer be additionally gzipped.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `update_web_docs_git` script, used for updating GCC's web documentation,
  previously created `.pdf.gz` versions of generated PDF files. As PDF is a format
  that incorporates compression, the additional gzip step was largely superfluous.
  This commit removes that redundant step from the script.
primer_glossary:
- term: maintainer-scripts
  definition: Scripts used by project maintainers to automate tasks related to building,
    testing, releasing, or managing project assets.
- term: PDF
  definition: Portable Document Format, a file format developed by Adobe for representing
    documents in a manner independent of application software, hardware, and operating
    systems. It typically includes compression.
- term: gzip
  definition: A popular data compression program and file format widely used in Unix-like
    operating systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9a698ac1bdabbb0420465959203f5fd3fd261b8f
date: '2026-09-12'
is_stub: true
stub_reason: low_score
---

The maintainer script `update_web_docs_git` has been modified to stop generating `.pdf.gz` files. Since PDF files are already compressed, applying gzip compression provides minimal benefit and is redundant. This change streamlines the documentation generation process.
