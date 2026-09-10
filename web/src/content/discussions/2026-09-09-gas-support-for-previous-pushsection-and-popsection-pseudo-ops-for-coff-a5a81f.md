---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- COFF
- assembler directives
discussion_id: 45021ca3-5b69-44be-84ed-7f0cc68ab76c@johannesthoma.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: support for .previous, .pushsection and .popsection pseudo
  ops for coff'
headline: 'gas: support for .previous, .pushsection and .popsection pseudo ops for
  coff'
tldr: Addresses review comments on adding .previous, .pushsection, and .popsection
  to gas for COFF targets.
proposer: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds section management capabilities to gas for COFF.
- Potential complexity in handling xcoff's predefined section structure.
exchanges:
- author: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
  role: proposer
  position: Has addressed review comments and is seeking clarification on xcoff patches,
    as well as further feedback.
  quote: 'Thanks for the comments, I think I have addressed all of them.


    I am still not sure about the xcoff patches, looking at the code,

    they are needed but on the other hand with xcoff there are only

    predefined sections (as I read in a comment).


    Please let me know if I can do anything else at the moment,'
- author: Jan Beulich
  role: reviewer
  position: Provided several review comments on the patch, including omitting NEWS
    entries, using NULL for pointer comparisons, and suggesting `static` for certain
    variables.
  quote: 'This wants omitting; it''s added as part of making a release.


    static?


    NULL please when comparing against a pointer.'
primer_expert: This email is a follow-up to a patch series introducing `.previous`,
  `.pushsection`, and `.popsection` directives to GNU as (gas) for COFF targets. These
  directives manage section stacking, allowing more flexible section manipulation,
  akin to their ELF counterparts. The author is seeking confirmation on the necessity
  of specific xcoff-related patches, as xcoff has a more rigid section definition
  compared to ELF.
primer_glossary:
- term: gas
  definition: GNU Assembler, the assembler used in the GNU toolchain.
- term: COFF
  definition: Common Object File Format. A file format for executables, object code,
    and libraries, primarily used on Windows systems.
- term: pseudo-ops
  definition: Assembler directives that do not generate machine code but control the
    assembly process, such as defining sections or symbols.
- term: .previous
  definition: A gas pseudo-op that restores the previously active section.
- term: .pushsection
  definition: A gas pseudo-op that saves the current section and then activates a
    new section.
- term: .popsection
  definition: A gas pseudo-op that restores the section that was most recently saved
    by .pushsection.
- term: xcoff
  definition: An extended version of COFF, used on some Unix systems like AIX, known
    for its predefined section structure.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/45021ca3-5b69-44be-84ed-7f0cc68ab76c@johannesthoma.com
bugzilla_url: null
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

Johannes Khoshnazar-Thoma responds to review comments on a patch that adds support for `.previous`, `.pushsection`, and `.popsection` pseudo-operations to the gas assembler for COFF targets. He expresses uncertainty about the necessity of xcoff patches given the predefined sections in xcoff, but believes they are needed. The author is seeking further feedback and offering to make additional changes.
