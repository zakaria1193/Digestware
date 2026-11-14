---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- binutils
- ld
- testsuite
- regression
discussion_id: 20261113152115.79A3B407E34A@pc56224-2341.se.axis.com
source_type: public_inbox
title: '"ERROR:" missing ld_relax_underflow_test in aaf62c2437f48f'
headline: 'Testsuite error: missing ld_relax_underflow_test command'
tldr: A test in the `cris-axis-elf` toolchain failed due to a missing `ld_relax_underflow_test`
  command.
proposer: Hans-Peter Nilsson <hp@axis.com>
consensus: Ready to Land
outcome: ready
impact_score: 3
sentiment_score: 8
technical_tradeoffs:
- Reverted a change to resolve an immediate test failure, delaying the introduction
  of new relaxation tests.
exchanges:
- author: Hans-Peter Nilsson <hp@axis.com>
  role: other
  position: Reports a testsuite error caused by an undefined command.
  quote: 'I think this one is yours (testing cris-axis-elf):


    ERROR: -------------------------------------------

    ERROR: in testcase /src/ld/testsuite/ld-rl78/rl78-relax-underflow.exp

    ERROR:  invalid command name "ld_relax_underflow_test"

    ERROR:  tcl error code TCL LOOKUP COMMAND ld_relax_underflow_test'
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Acknowledged a revert for the issue.
  quote: 'On 13.11.2026 16:21, Hans-Peter Nilsson wrote:

    > I think this one is yours (testing cris-axis-elf):'
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: contributor
  position: Apologized for the error and confirmed that the revert will be in place,
    with future patches including early exits.
  quote: 'Thanks to Jan, for the quick revert.  When the patches go back in, the

    new *-relax-underflow.exp files will return early on other targets.


    Sorry for the noise.'
primer_expert: This discussion concerns a test failure in the `ld` testsuite for the
  `cris-axis-elf` target. The error `invalid command name "ld_relax_underflow_test"`
  indicates that a test procedure, likely introduced in a recent patch series, is
  missing or was not properly installed. This specific error occurred during the execution
  of `rl78-relax-underflow.exp`.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component or system.
- term: cris-axis-elf
  definition: A specific toolchain target configuration, likely for embedded systems,
    using the ELF object file format and targeting a processor family from Axis Communications.
- term: tcl
  definition: Tool Command Language, a scripting language often used for test harnesses
    and build systems.
- term: relax-underflow
  definition: Relates to linker relaxation, a process where the linker adjusts addresses
    and offsets of instructions or data to optimize for code size or position independence.
    An 'underflow' might indicate an issue where the relaxation process cannot satisfy
    constraints.
- term: exp
  definition: Likely refers to '.exp' files, which are Tcl scripts used by DejaGnu,
    a testing framework, to define and run tests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261113152115.79A3B407E34A@pc56224-2341.se.axis.com
bugzilla_url: null
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

Hans-Peter Nilsson reported a test failure in the `cris-axis-elf` toolchain, specifically within the `rl78-relax-underflow.exp` test case. The error indicates that the command `ld_relax_underflow_test` is not defined, suggesting a missing patch or an incomplete commit. The reporter asks for the issue to be amended or reverted and suggests improving the test case's error handling.
