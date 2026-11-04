---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- sframe
- initialization
- ABI
discussion_id: 20261103114812.3157530-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] gas: sframe: Init x86_fp_deref_p to false'
headline: 'gas: sframe: Init x86_fp_deref_p to false'
tldr: Patch initializes x86_fp_deref_p to false in gas's sframe module.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Corrects an initialization bug, potentially fixing incorrect frame pointer handling
  in generated FDE information, with no negative performance impact.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submits a patch to initialize `x86_fp_deref_p` to `false` in the gas sframe
    module.
  quote: bool x86_fp_deref_p = true;
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and the observed issue, agreeing with the proposed
    change.
  quote: "On 03.11.2026 12:48, mengqinggang wrote:\n> ---\n>  gas/gen-sframe.c | 2\
    \ +-\n>  1 file changed, 1 insertion(+), 1 deletion(-)\n>\n> diff --git a/gas/gen-sframe.c\
    \ b/gas/gen-sframe.c\n> index 031421d8ab7..8121939f43e 100644\n> --- a/gas/gen-sframe.c\n\
    > +++ b/gas/gen-sframe.c\n> @@ -1889,7 +1889,7 @@ sframe_xlate_do_escape_expr\
    \ (struct sframe_xlate_ctx *xlate_ctx,\n>  \n>    unsigned opcode = items[2];\n\
    >    un…"
primer_expert: The `sframe_xlate_do_escape_expr` function in `gas/gen-sframe.c` incorrectly
  initializes the `x86_fp_deref_p` flag to `true`. This flag determines whether frame
  pointer dereferencing is used, which is dependent on the ABI architecture and whether
  flex FDE support is enabled. The correct default value for this flag, especially
  for non-AMD64 little-endian architectures or when flex FDE is not supported, should
  be `false`. This patch corrects the initialization to `false`, ensuring proper frame
  pointer handling according to the SFrame ABI specifications.
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the GNU toolchain that translates
    assembly language code into machine code.
- term: sframe
  definition: A module within gas related to the generation of FDE (Frame Description
    Entry) information, used for stack unwinding.
- term: x86_fp_deref_p
  definition: A boolean flag within the sframe module that indicates whether frame
    pointer dereferencing is being used on x86 architectures.
- term: FDE
  definition: Frame Description Entry. Data structures used by debuggers and exception
    handling mechanisms to describe the stack frame layout and unwind information
    for a function.
- term: ABI
  definition: Application Binary Interface. Defines how low-level code, such as compiled
    object files, should interact, including function calling conventions and data
    layout.
- term: AMD64
  definition: The 64-bit version of the x86 instruction set architecture.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261103114812.3157530-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This patch corrects an initialization error in the gas assembler's sframe module. The boolean variable `x86_fp_deref_p` was incorrectly initialized to `true` when it should be `false` for certain ABI architectures. By changing the default initialization to `false`, the patch ensures correct behavior for frame pointer dereferencing based on the ABI and architecture support.
