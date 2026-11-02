---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- debugging
- DWARF
- testing
discussion_id: b03b9d62-0598-477d-b803-5ffce41bee26@suse.com
source_type: public_inbox
title: 'Re: [PATCH] gas: Name the CU after the primary source file'
headline: 'gas: Name the CU after the primary source file'
tldr: Reviewer confirms extensive testing for the gas patch and agrees to commit it.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improving debug information accuracy can aid developers but might introduce subtle
  changes in build outputs.
- Ensuring comprehensive test coverage across diverse configurations is crucial for
  robust changes but can be time-consuming.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Agrees to commit the patch after confirming that the author ran the full
    gas testsuite across 121 configurations, validating the change.
  quote: "Thanks. \n\nWill do, but please be patient. This is very unlikely to happen\
    \ before\nthe end of the week."
- author: Longjun Luo
  role: proposer
  position: Provided extensive test results covering 121 configurations for the gas
    patch after the reviewer requested broader validation.
  quote: 'I have now run the full gas testsuite with and without the patch on

    top of master bc3e31b590dd, for 121 configurations on an

    x86_64-linux-gnu host. Together they cover every ELF-capable CPU in

    gas/configure.tgt; 117 of them run elf.exp (list below), and the other

    four are bpf-none, i686-vxworks, mmix and x86_64-w64-mingw32. The two

    new tests pass on all 117, and no other test changes its result o…'
primer_expert: This discussion concerns a patch for the GNU Assembler (`gas`) that
  modifies how the Compilation Unit (CU) debug information is named. Specifically,
  it aims to name the CU after the primary source file, which is a change to how DWARF
  debug info is generated. The patch has undergone review, with concerns raised about
  test coverage. The author subsequently provided extensive test results across numerous
  configurations, leading to the reviewer's agreement to commit.
primer_glossary:
- term: gas
  definition: The GNU Assembler, which translates assembly language code into machine
    code.
- term: Compilation Unit (CU)
  definition: In debugging contexts (like DWARF), a CU represents a single source
    file that has been compiled.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about program variables, types, and structure for debugging purposes.
- term: ELF
  definition: Executable and Linkable Format, the standard object file format used
    by GNU/Linux systems.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component or system.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b03b9d62-0598-477d-b803-5ffce41bee26@suse.com
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

Following initial review and a request for more extensive testing, the patch author provided results from running the gas testsuite across 121 configurations. The reviewer, Jan Beulich, acknowledges this comprehensive testing and agrees to commit the patch, noting a slight delay is expected.
