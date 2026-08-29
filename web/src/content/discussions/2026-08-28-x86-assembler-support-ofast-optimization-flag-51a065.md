---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- optimization
- floating-point
- AVX
discussion_id: 7d179589-0048-4308-ba04-e259b646c022@suse.com
source_type: public_inbox
title: '[PATCH] x86: support -Ofast'
headline: 'x86 assembler: support -Ofast optimization flag'
tldr: Adds support for the -Ofast optimization flag in the x86 assembler, analogous
  to GCC's option, allowing potentially unsafe floating-point optimizations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 6
technical_tradeoffs:
- Enables aggressive optimizations that may break strict floating-point compliance.
- Allows for potential code size reduction or performance improvements through instruction
  encoding changes.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes adding `-Ofast` support to the x86 assembler to enable potentially
    unsafe floating-point optimizations.
  quote: '... in analogy to gcc''s option of the same name: It relaxes constraints

    on (the lack of) commutativity of V{ADD,MAX,MIN,MUL}{P,S}{S,D}. They''re

    not fully commutative solely because of their NaN treatment. If the

    programmer indicates that''s benign to them, we can apply the VEX3->VEX2

    encoding transformation for these AVX insns as well.'
- author: Jiang, Haochen
  role: reviewer
  position: Indicates they are not against the option but asks for clarification on
    whether it should also control optimization of NOP-like instructions.
  quote: I am not against the option and the behavior of this patch since it f
- author: Jan Beulich
  role: proposer
  position: Responds to reviewer's question about NOP instructions, suggesting it's
    a separate topic and clarifying the scope of the current patch.
  quote: 'NOP insns might be another topic. It is still vague to me. I will lean on
    if we

    have -Ofast, we could include that. And which variable would want renaming?

    I did not get that'
- author: H.J. Lu
  role: reviewer
  position: Questions the potential renaming of a variable if NOP-like instruction
    optimizations were to be included, implying it might be a separate concern.
  quote: 'If we wanted to also use this to control optimization of NOP-like insns

    (e.g. the XCHG -> MOV one), the variable would want renaming. Question is:

    _Do_ we (perhaps) want that?'
- author: Jan Beulich
  role: proposer
  position: Acknowledges H.J. Lu's point about NOP instructions and seeks clarification
    on which variable might need renaming.
  quote: 'On 28.08.2026 11:51, H.J. Lu wrote:

    > On Fri, Aug 28, 2026 at 4:39 PM Jan Beulich <jbeulich@suse.com> wrote:

    >>

    >> ... in analogy to gcc''s option of the same name: It relaxes constraints

    >> on (the lack of) commutativity of V{ADD,MAX,MIN,MUL}{P,S}{S,D}. They''re

    >> not fully commutative solely because of their NaN treatment. If the

    >> programmer indicates that''s benign to them, we can apply the VE…'
- author: H.J. Lu
  role: reviewer
  position: Reiterates the point about NOP instruction optimization and its potential
    impact on variable naming.
  quote: 'On Fri, Aug 28, 2026 at 8:02 PM Jan Beulich <jbeulich@suse.com> wrote:


    > On 28.08.2026 11:51, H.J. Lu wrote:

    > > On Fri, Aug 28, 2026 at 4:39 PM Jan Beulich <jbeulich@suse.com> wrote:

    > >>

    > >> ... in analogy to gcc''s option of the same name: It relaxes constraints

    > >> on (the lack of) commutativity of V{ADD,MAX,MIN,MUL}{P,S}{S,D}. They''re

    > >> not fully commutative solely because of their NaN…'
primer_expert: This patch introduces support for the `-Ofast` optimization level in
  the GNU Assembler (`as`) for the x86 target. This flag mirrors GCC's `-Ofast` by
  enabling optimizations that may violate strict IEEE 754 floating-point compliance,
  specifically concerning NaN (Not a Number) handling and the commutativity of certain
  floating-point operations (e.g., `V{ADD,MAX,MIN,MUL}{P,S}{S,D}`). The primary benefit
  is enabling transformations like VEX3 to VEX2 encoding for AVX instructions, potentially
  reducing code size or improving performance. The discussion also touches upon whether
  this flag should ext…
primer_glossary:
- term: -Ofast
  definition: An optimization level flag for compilers and assemblers that enables
    aggressive optimizations, potentially at the cost of strict adherence to standards
    like IEEE 754 floating-point.
- term: NaN
  definition: Not a Number. An IEEE 754 floating-point value used to represent the
    result of operations that are undefined or unrepresentable, such as division of
    zero by zero.
- term: Commutativity
  definition: In mathematics, a property of a binary operation where the order of
    operands does not affect the result (e.g., a + b = b + a). Floating-point arithmetic
    may not always be commutative due to precision and NaN handling.
- term: AVX
  definition: Advanced Vector Extensions. A set of SIMD (Single Instruction, Multiple
    Data) instructions for x86 processors that allow operations on multiple data points
    simultaneously.
- term: VEX
  definition: Vector Extension. A prefix used in x86 instructions to encode operations
    that use vector registers, with different versions (e.g., VEX2, VEX3) offering
    different capabilities and encoding lengths.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/7d179589-0048-4308-ba04-e259b646c022@suse.com
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

Jan Beulich proposes adding support for the `-Ofast` optimization flag to the x86 assembler. This flag, similar to GCC's `-Ofast`, signals that the programmer accepts potentially incorrect floating-point behavior, such as the lack of strict NaN handling, to enable optimizations like VEX3->VEX2 encoding for certain AVX instructions. The change introduces a `fast_math` flag in `tc-i386.c` and updates the assembler's documentation to reflect this new option.
