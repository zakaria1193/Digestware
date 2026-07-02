---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- disassembler
- comments
- formatting
discussion_id: 9a6fd40f-1081-41e3-8050-e000ba78fcfb@suse.com
source_type: public_inbox
title: '[PATCH] x86: Pass "%s" to i386_dis_printf as the format string'
headline: 'x86: Pass "%s" to i386_dis_printf as the format string'
tldr: The x86 disassembler now passes "%s" as the format string to i386_dis_printf
  to allow comments to be emitted in the same order as operands.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- May require adjustments to existing disassembler tests and scripts.
- The ->print_address_func() hook limits the possible unification of %rip-relative
  comments.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes passing "%s" to i386_dis_printf as the format string to allow
    comments to be emitted in the same order as operands.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Agrees with the approach of modeling after operand handling, but notes
    that unifying %rip-relative comments with others won't be possible while using
    the ->print_address_func() hook.
  quote: Model this after operand handling, such that comments can be emitted in the
    same order as operands. %rip-relative address comments remain separate for now.
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Acknowledges Jan Beulich's feedback.
  quote: null
primer_expert: This patch modifies the x86 disassembler in ``opcodes/i386-dis.c``
  to pass a format string to ``i386_dis_printf`` when printing comments, allowing
  for more flexible comment formatting. The goal is to emit comments in the same order
  as operands during disassembly. The ``print_address_func`` hook is used for printing
  direct addresses, which affects the unification of %rip-relative comments.
primer_general: The disassembler translates machine code into human-readable assembly.  This
  involves formatting the instructions and adding helpful comments to clarify the
  code's purpose. The patch modifies how comments are formatted in the x86 disassembler,
  aiming for a more natural ordering where comments appear alongside the operands
  they describe.  This change improves the readability of the disassembled code, making
  it easier for developers to understand the underlying machine instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOoif-2+zZoR1=Vbr3pcGBoCnBhDW84Xy=pJ9agBvQUn6g@mail.gmail.com
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch modifies the x86 disassembler to pass "%s" as the format string to ``i386_dis_printf``. This change should allow comments to be emitted in the same order as operands for better readability. The patch also includes updates to the testsuite to account for the change in comment formatting.
