---
project: gcc
subsystem: gcc
patch_id: null
tags:
- documentation
- libiberty
- texinfo
discussion_id: 20261101173923.5f1e09cade0a700684605a04@schemamania.org
source_type: public_inbox
title: libiberty/functions.texi appears out of date
headline: libiberty/functions.texi appears out of date
tldr: Update libiberty/functions.texi to include ldirname in generated info.
proposer: '"James K. Lowden" <jklowden@schemamania.org>'
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Updating documentation ensures accuracy but requires careful management of versioning
  and dependencies.
exchanges:
- author: James K. Lowden
  role: proposer
  position: Reports that the generated libiberty.info document is missing the ldirname
    function because libiberty/functions.texi is out of date. Offers to commit a fix
    if desired.
  quote: "In master branch running make -C build/libiberty info produces a\nlibiberty.info\
    \ document lacking ldirname.  This appears to be because\nlibiberty/functions.texi\
    \ is out of date.  \n\nI ran gather-docs and make info, and the resulting libiberty.info\
    \ file\nincludes the function.  I didn't want to commit functions.texi\nbecause\
    \ it's outside my aegis.  But I'm happy to if that's what is\nwanted."
primer_expert: The `libiberty` library provides common utility functions for GCC.
  This discussion concerns its documentation, specifically the Texinfo files used
  to generate man pages and info documents. The `ldirname` function appears to be
  missing from the generated info output, indicating a staleness in the `functions.texi`
  file.
primer_glossary:
- term: libiberty
  definition: A C library providing common utility functions used by various GNU projects,
    including GCC. It's often built as a separate component.
- term: texinfo
  definition: A documentation system used by GNU to produce online and printed documentation.
    It's a markup language used to write manuals, which can then be formatted into
    various output formats like HTML, PDF, and Info.
- term: info document
  definition: A documentation format produced by the Texinfo system, typically browsed
    using the `info` reader. It's a hypertextual system designed for online reading.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20261101173923.5f1e09cade0a700684605a04@schemamania.org
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

The libiberty.info document generated from the master branch is missing the ldirname function. This is due to the source file libiberty/functions.texi being out of date. The proposer has a fix but is hesitant to commit it as it falls outside their area of responsibility.
