---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- instruction
- cpu-measurement
discussion_id: 9ccba8a3-9ea8-4408-8bfa-3088cb7ea2d5@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] s390: Add store CPU counter multiple instruction'
headline: 's390: Add store CPU counter multiple instruction'
tldr: Jens Remus confirms the "store CPU counter multiple" instruction has been committed.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Confirms the patch adding the 'store CPU counter multiple' instruction
    has been committed.
  quote: Thank you for the review!  Committed to mainline.
primer_expert: This patch adds support for the `stcctm` instruction on s390, part
  of the CPU-Measurement Facilities (CPUMF) for the IBM z13. Support includes the
  opcode table entry, documentation, and a gas test suite.
primer_glossary:
- term: store CPU counter multiple
  definition: An instruction that reads multiple CPU performance counters, introduced
    with the Store-CPU-Counter-Multiple Facility on IBM z13.
- term: CPU-Measurement Facilities (CPUMF)
  definition: A set of features on IBM mainframes that allow for the measurement of
    CPU performance and activity.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/9ccba8a3-9ea8-4408-8bfa-3088cb7ea2d5@linux.ibm.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Jens Remus confirms that a patch adding the "store CPU counter multiple" instruction for the IBM z13 processor has been committed to mainline. The patch also adds comments to the s390 opcode table for existing CPUMF instructions and includes a test case.
