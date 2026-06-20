---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- pic
- plt
- testsuite
- elf
discussion_id: ajN_uxj8OQ2QlW-x@squeak.grove.modra.org
source_type: public_inbox
title: 'PR 29655 test: xfail more targets'
headline: 'PR 29655 test: xfail more targets'
tldr: This patch expands the list of targets that are expected to fail a specific
  linker test related to PIC and PLT call stubs, due to an uncritical linker bug.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Acknowledges a known linker bug rather than resolving it across all affected targets.
- Increases the number of `xfail` targets, potentially masking future regressions
  on these platforms if a genuine fix were to emerge without updating the testcase.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes to `xfail` (expect-to-fail) additional targets for a specific
    linker test that highlights an uncritical linker bug related to PLT call stub
    code, acknowledging the difficulty for target maintainers to fix it.
  quote: On the other hand if the main executable is PIC then there should be no need
    to define function addresses on PLT call stub code, but some linker target support
    still does so. This is a minor bug in the linker as it results in more work in
    ld.so and sligntly slower startup. However, I don't think it is an important issue
    if target maintainers can't fix the problem.
primer_expert: PR 29655 highlights an interaction between Position-Independent Code
  (PIC), the Procedure Linkage Table (PLT), and function address resolution in dynamic
  linking. When a shared library (DSO) defines a function, and the main program (potentially
  non-PIC) calls it, the globally visible address of that function within the main
  executable might be incorrectly set to a PLT call stub. For PIC executables, the
  linker should ideally not define function addresses on PLT call stub code, as this
  adds overhead to `ld.so` (the dynamic linker/loader) and slightly impacts startup
  performance. This patch exp…
primer_general: This discussion is about a small issue in the linker, `ld`, which
  helps combine different parts of a program. Specifically, it relates to how programs
  are built to be "Position-Independent Code" (PIC). PIC means the program can be
  loaded anywhere in memory without needing modification, which is common for shared
  libraries. The "Procedure Linkage Table" (PLT) is a mechanism used by the linker
  to help a program call functions located in other libraries. The problem is that
  sometimes, even for PIC programs, the linker incorrectly sets the address of a function
  to point to a special piece of code called a "PLT stub," instead of the actual function.
  While this isn't a critical error – it just makes the program start a tiny bit slower
  and causes the dynamic loader (`ld.so`) to do a little more work – it's a known
  deviation. This patch simply updates the test suite to mark this behavior as expected
  for several more computer architectures (like RISC-V or S390), rather than failing
  the tests,…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajN_uxj8OQ2QlW-x@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-18'
is_stub: false
---

This proposal extends the list of targets that "xfail" (are expected to fail) a test relating to PR 29655. The underlying issue concerns how some linkers, even for Position-Independent Code (PIC), define function addresses with PLT (Procedure Linkage Table) call stub code. While this is considered a minor bug in the linker, leading to slightly slower startup and more work for `ld.so`, it's acknowledged that fixing it may be challenging for target maintainers, justifying the expanded xfail list.
