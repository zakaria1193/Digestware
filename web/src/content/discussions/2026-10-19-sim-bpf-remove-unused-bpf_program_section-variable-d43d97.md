---
project: binutils
subsystem: sim/bpf
patch_id: null
tags:
- cleanup
- build
- bpf
discussion_id: d7deeb1b-f509-48fb-ba06-4d538b06b87f@efficios.com
source_type: public_inbox
title: 'Re: [PATCH 09/18] sim/bpf: remove unused bpf_program_section variable'
headline: 'sim/bpf: remove unused bpf_program_section variable'
tldr: Remove unused bpf_program_section variable from BPF simulator.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the codebase and avoiding potential issues with unused
  variables.
- No functional change is expected as the variable and its related feature were never
  utilized.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes removing the unused `bpf_program_section` variable which causes
    a build error with recent Clang versions.
  quote: "Building the BPF simulator with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/sim/bpf/bpf-sim.c:367:14:\
    \ error: variable 'bpf_program_section' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe --bpf-set-program option stores its argument in this variable, but\nnothing\
    \ ever reads it, the feature was never implemented.  Remove the\nvariable."
primer_expert: This patch removes an unused global variable `bpf_program_section`
  from `sim/bpf/bpf-sim.c`. This variable was intended to store the section name for
  the BPF program to be run, but the associated functionality was never implemented,
  leading to a build error with strict warning flags like `-Werror,-Wunused-but-set-global`.
primer_glossary: []
series_id: 'binutils:sim/bpf: remove unused bpf_program_section variable'
series_role: reply
series_parts:
- title: 'sim/bpf: remove unused bpf_program_section variable'
  url: https://inbox.sourceware.org/binutils/20261019193231.1708375-10-simon.marchi@efficios.com
  n: 9
  total: 18
url: https://inbox.sourceware.org/binutils/d7deeb1b-f509-48fb-ba06-4d538b06b87f@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi proposes removing the unused `bpf_program_section` variable from the BPF simulator. Building with a recent Clang compiler resulted in an error due to this unused variable being flagged. The feature that would have used this variable was never implemented.
