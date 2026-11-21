---
project: binutils
subsystem: ld/pdb.c
patch_id: null
tags:
- linker
- security
- hardening
- integer overflow
- rfc
discussion_id: y107bi7akd3.fsf@nickc-thinkpadp1gen8.rmtgb.csb
source_type: public_inbox
title: 'RFC: non-AI hardening of ld/pdb.c'
headline: 'RFC: non-AI hardening of ld/pdb.c'
tldr: Proposes a patch to harden ld/pdb.c against integer overflows, going beyond
  an initial AI-generated fix.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 6
technical_tradeoffs:
- Increases robustness by fixing potential integer overflows.
- Addresses code quality through tidying and reformatting.
- Risk of over-engineering if the expanded fixes are not strictly necessary.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Submits an RFC for a manually created patch to harden ld/pdb.c, expanding
    on an AI-generated fix to address multiple potential integer overflows and includes
    code cleanup.
  quote: 'I may however have gone slightly overboard...


    Looking at the code, there were several other places where similar

    integer overflows could - theoretically - occur, and so I decided to

    fix those too. Then there were some minor tidu

    '
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the RFC and the author's effort in creating a manual patch,
    noting the 'overboard' aspect mentioned by the proposer.
  quote: Acknowledges the RFC and the author's effort in creating a manual patch,
    noting the 'overboard' aspect mentioned by the proposer.
primer_expert: This RFC concerns `ld/pdb.c`, a file within the GNU linker responsible
  for processing PDB (Program Database) related information, likely for Windows PE/COFF
  targets. The patch addresses potential integer overflows identified in this module,
  going beyond a previously reported AI-generated fix. The author manually reimplemented
  the fix and extended it to cover additional theoretical overflow scenarios, along
  with general code cleanup, indicating a focus on robustness and maintainability
  of the linker's PDB handling.
primer_glossary:
- term: RFC
  definition: Request For Comments. A document that proposes new standards or provides
    background information and invites feedback.
- term: ld/pdb.c
  definition: A source file within the GNU linker (`ld`) that deals with Program Database
    (PDB) files, typically used for debugging information on Windows platforms.
- term: integer overflow
  definition: A condition that occurs when an arithmetic operation attempts to create
    a numeric value that is too large to be represented in the memory or number type
    used.
- term: hardening
  definition: The process of designing and implementing software to be more secure
    and resilient against attacks or unexpected conditions, such as overflows.
- term: AI agent
  definition: An automated software program designed to perform tasks that typically
    require human intelligence, such as writing code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/y107bi7akd3.fsf@nickc-thinkpadp1gen8.rmtgb.csb
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This RFC proposes a patch to harden the `ld/pdb.c` file against potential integer overflows. The author created this patch manually after an AI-generated fix was reported, and expanded the scope to address several other theoretical overflow possibilities within the code, alongside minor tidying and reformatting.
