---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- PDB
- debug info
- alignment
discussion_id: 20260918093607.779-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] ld: Align the PDB DBI source-info substream'
headline: 'ld: Align the PDB DBI source-info substream'
tldr: Ensure PDB DBI source-info substream size is a multiple of 4 bytes, zero-padding
  any excess.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: needs_revision
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Ensures PDB compatibility and determinism by adhering to alignment requirements.
- Introduces minor overhead for alignment calculation and zeroing padding.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes aligning the source-info substream size to four bytes and zeroing
    padding, citing PDB format requirements.
  quote: 'Round the source-info substream size up to four bytes and zero the

    padding.  Extend the test to exercise this case.


    docs/pdb/dbi_sources.md in https://github.com/microsoft/pdb-rs says:

    "Invariant: The size of the DBI Sources Substream (source_info_size) is

    a multiple of 4." and "Determinism: Alignment padding bytes are set to

    zero, if present."'
- author: Jan Beulich
  role: reviewer
  position: Asks a clarifying question about potential issues with MSYS2's environment
    variable handling for path conversions in test cases.
  quote: 'The workaround of course isn''t very nice, and in particular doesn''t scale.

    The page you reference doesn''t address at all whether e.g. some form of

    quoting would also help. That certainly depends on where exactly the

    conversion is being done.'
- author: Jan Beulich
  role: reviewer
  position: Follows up on a previous question, suggesting appending to an environment
    variable rather than overwriting it to maintain global settings.
  quote: 'In case the user has set the env var globally, wouldn''t you better append

    to it (and then restore) rather than fully overwriting (and then deleting)?'
- author: Oleg Tolmatcev
  role: proposer
  position: Acknowledges Jan Beulich's concern about environment variable handling
    and agrees to append to the variable instead of overwriting it.
  quote: 'On 18.09.2026 11:42, Jan Beulich wrote:

    > On 18.09.2026 11:36, Oleg Tolmatcev wrote:

    >> Round the source-info substream size up to four bytes and zero the

    >> padding.  Extend the test to exercise this case.

    >>

    >> docs/pdb/dbi_sources.md in https://github.com/microsoft/pdb-rs says:

    >> "Invariant: The size of the DBI Sources Substream (source_info_size) is

    >> a multiple of 4." and "Determinism: Ali…'
primer_expert: This change modifies `ld/pdb.c` to ensure that the size of the PDB
  DBI source-info substream is a multiple of 4 bytes, as required by the PDB format
  specification. It also ensures padding bytes are zeroed. The test suite is updated
  to cover this alignment.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260918093607.779-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This patch modifies the linker (`ld`) to align the size of the PDB DBI source-info substream to a four-byte boundary, zeroing out any padding. This change ensures compliance with the PDB format's requirement for four-byte alignment and determinism in padding bytes. A test case is extended to verify this behavior.
