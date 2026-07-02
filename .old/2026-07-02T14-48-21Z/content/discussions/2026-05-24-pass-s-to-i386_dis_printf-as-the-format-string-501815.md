---
project: binutils
subsystem: x86
patch_id: null
tags:
- security
- x86
- disassembler
- format string vulnerability
- binutils
discussion_id: CAMe9rOoif-2+zZoR1=Vbr3pcGBoCnBhDW84Xy=pJ9agBvQUn6g@mail.gmail.com
source_type: public_inbox
title: '[PATCH] x86: Pass "%s" to i386_dis_printf as the format string'
headline: Pass "%s" to i386_dis_printf as the format string
tldr: The patch modifies the x86 disassembler to pass "%s" as the format string to
  `i386_dis_printf` to prevent format string vulnerabilities.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Passing "%s" to i386_dis_printf ensures safe handling of input strings.
- New tests added to the testsuite cover disassembly comments.
exchanges: []
primer_expert: This patch addresses a potential format string vulnerability in the
  x86 disassembler's `i386_dis_printf` function. The disassembler translates machine
  code to assembly, and `i386_dis_printf` is used for output. By explicitly providing
  `"%s"` as the format string, the code avoids interpreting parts of the input as
  format specifiers, mitigating potential security risks. The testsuite updates add
  new test cases (`comments.d`, `comments.s`, `comments-intel.d`) to verify the correct
  generation of disassembly comments and ensure the fix is effective.
primer_general: This patch addresses a security issue in a tool that translates machine
  code (the binary instructions computers execute) into human-readable assembly code.
  This tool is called a disassembler. The vulnerability stems from a function (`i386_dis_printf`)
  that formats output strings. If the format string isn't carefully controlled, it
  could allow attackers to inject malicious code. This patch ensures the format string
  is fixed, preventing such attacks. New tests are also added to verify the fix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOoif-2+zZoR1=Vbr3pcGBoCnBhDW84Xy=pJ9agBvQUn6g@mail.gmail.com
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch updates the x86 disassembler code to pass `"%s"` as the format string to the `i386_dis_printf` function. This change is intended to prevent potential format string vulnerabilities. The patch also includes testsuite updates with new tests (`comments.d`, `comments.s`, `comments-intel.d`) to ensure the proper generation of disassembly comments.
