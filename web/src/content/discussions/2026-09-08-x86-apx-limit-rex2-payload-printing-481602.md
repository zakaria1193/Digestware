---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- disassembler
- x86
- patch
discussion_id: 86e08518-0e97-49ac-95d6-93f288759309@suse.com
source_type: public_inbox
title: '[PATCH] x86/APX: limit printing of REX2 payload'
headline: 'x86/APX: Limit REX2 payload printing'
tldr: Patch refines the printing of REX2 prefixes in the x86 disassembler to be more
  concise.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Conciseness of disassembler output vs. verbosity of REX2 prefix details.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Submitted a patch to simplify the output of REX2 prefixes in the disassembler,
    showing '{rex2}' when appropriate.
  quote: 'When set bits were properly consumed (and hence all we want is an

    indication that REX2-encoding is in use), print merely {rex2}, thus also

    better matching original input.


    While effectively copying parts of an existing conditional, also simplify

    the original: There''s no need to apply the 3-bit mask twice.


    While adjusting testcases, also escape curly braces.'
- author: Jiang, Haochen
  role: other
  position: Commented on the patch, starting a discussion about its implications.
  quote: null
- author: Jan Beulich
  role: other
  position: Responded to Haochen Jiang's comment.
  quote: null
- author: H.J. Lu
  role: other
  position: Participated in the discussion.
  quote: null
- author: Jan Beulich
  role: other
  position: Continued the discussion with H.J. Lu.
  quote: null
primer_expert: This patch modifies the i386-dis.c file in binutils to refine how REX2
  prefixes are displayed. Specifically, when the REX2 prefix is used but its specific
  bits are consumed or irrelevant for detailed display (e.g., just indicating REX2
  usage), the disassembler will now output '{rex2}' instead of a more verbose representation
  like '{rex2 0x0}'. This aims to improve output clarity and consistency.
primer_glossary:
- term: REX2 prefix
  definition: An extended prefix byte used in x86-64 architecture to encode additional
    addressing modes and features beyond the original REX prefix. It allows for features
    like REX.W, REX.R, REX.X, REX.B, and REX2.SPECIAL.
- term: Disassembler
  definition: A program that translates machine code (binary) back into assembly language.
- term: Payload
  definition: In this context, refers to the specific data or bits within the REX2
    prefix that convey detailed information.
- term: x86/APX
  definition: Refers to extensions or specific features related to the x86 architecture,
    possibly including Advanced Performance Extensions or similar.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/86e08518-0e97-49ac-95d6-93f288759309@suse.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Jan Beulich proposes a patch to the x86 disassembler that limits the printing of REX2 payloads. When REX2 bits are consumed and only indicate the encoding is in use, the output will now simply show '{rex2}' for better matching of original input. The patch also simplifies conditional logic and updates test cases.
