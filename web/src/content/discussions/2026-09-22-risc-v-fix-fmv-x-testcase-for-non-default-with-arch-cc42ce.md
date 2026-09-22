---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- gas
- testsuite
- patch
- architecture
discussion_id: 20260922025915.1361630-1-ycl669@andestech.com
source_type: public_inbox
title: '[PATCH] RISC-V: Fix fmv.x testcase for non-default --with-arch'
headline: 'RISC-V: Fix fmv.x testcase for non-default --with-arch'
tldr: Patch fixes the RISC-V fmv.x testcase to explicitly use -march=rv32i, preventing
  failures with non-default --with-arch configurations.
proposer: '"Ethan Y. C. Liang" <ycl669@andestech.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Hardcoding `-march=rv32i` makes the testcase less flexible but more robust against
  build configuration variations.
- Ensuring test isolation from build-time architecture flags improves test reliability.
exchanges:
- author: Ethan Y. C. Liang <ycl669@andestech.com>
  role: proposer
  position: Submits a patch to fix the RISC-V `fmv.x` testcase by explicitly setting
    `-march=rv32i`.
  quote: 'The testcase doesn''t pass -march, so it inherits the configured default

    architecture, and fails with e.g. --with-arch=rv32e* (no a6) or

    --with-arch=rv32i_zfinx (".option arch, +f" conflicts).  It only checks

    that fmv.x.s/fmv.s.x are aliases of fmv.x.w/fmv.w.x, which doesn''t

    depend on the base ISA.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and the problem description.
  quote: "On 22.09.2026 04:59, Ethan Y. C. Liang via Binutils wrote:\n> The testcase\
    \ doesn't pass -march, so it inherits the configured default\n> architecture,\
    \ and fails with e.g. --with-arch=rv32e* (no a6) or\n> --with-arch=rv32i_zfinx\
    \ (\".option arch, +f\" conflicts).  It only checks\n> that fmv.x.s/fmv.s.x are\
    \ aliases of fmv.x.w/fmv.w.x, which doesn't\n> depend on the base ISA.\n> \n>\
    \ gas/ChangeLog: \n> \n>\t* tes…"
- author: Ethan Y. C. Liang <ycl669@andestech.com>
  role: proposer
  position: Responds to Jan Beulich, confirming the issue and the fix.
  quote: 'On Tue, Sep 22, 2026 at 08:08:16AM +0200, Jan Beulich wrote:


    On 22.09.2026 04:59, Ethan Y. C. Liang via Binutils wrote:

    > The testcase doesn''t pass -march, so it inherits the configured default

    > architecture, and fails with e.g. --with-arch=rv32e* (no a6) or

    > --with-arch=rv32i_zfinx (".option arch, +f" conflicts).  It only checks

    > that fmv.x.s/fmv.s.x are aliases of fmv.x.w/fmv.w.x, which doe…'
primer_expert: This patch addresses a test case in the GNU Assembler's (gas) testsuite
  for the RISC-V architecture. The issue arises because the `fmv.x` instruction testcase,
  specifically `gas/testsuite/gas/riscv/fmv.x.d`, does not explicitly specify the
  target architecture using the `-march` flag. Consequently, it inherits the `--with-arch`
  configuration used during the build. This leads to test failures when `--with-arch`
  is set to something other than the default or a compatible base ISA, such as `rv32e*`
  (which lacks floating-point extensions) or `rv32i_zfinx` (which has conflicting
  options). The fix in…
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on RISC principles,
    widely adopted for custom processor designs.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, which translates
    assembly language into object files.
- term: testcase
  definition: A specific input or scenario designed to verify the correctness of a
    piece of software.
- term: --with-arch
  definition: A configuration option used during the build process of software like
    GCC or Binutils to specify the target architecture.
- term: -march
  definition: A compiler flag used to specify the target architecture and extensions
    for code generation. In the context of gas tests, it sets the assembler's target
    architecture.
- term: rv32i
  definition: The base integer instruction set for the 32-bit RISC-V architecture.
- term: fmv.x.s
  definition: A RISC-V instruction that moves a value from a floating-point register
    to an integer register.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260922025915.1361630-1-ycl669@andestech.com
bugzilla_url: null
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This patch addresses a failing test case in the gas testsuite for RISC-V. The `fmv.x` testcase was not passing the `-march` flag, leading it to inherit the default architecture configured at build time. This caused failures when build configurations used non-default `--with-arch` options, such as `rv32e*` or `rv32i_zfinx`. The fix ensures the test explicitly uses `-march=rv32i` which is sufficient for its purpose of verifying `fmv.x.s`/`fmv.s.x` as aliases of `fmv.x.w`/`fmv.w.x`.
