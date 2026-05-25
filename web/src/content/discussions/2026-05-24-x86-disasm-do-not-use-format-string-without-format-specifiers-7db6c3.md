---
project: binutils
subsystem: x86/disasm
patch_id: null
tags:
- x86
- disassembler
- format string
- security
- build failure
discussion_id: 20260524030619.1313131-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] x86/disasm: do not use format string without format specifiers'
headline: 'x86/disasm: Do not use format string without format specifiers'
tldr: The x86 disassembler is updated to avoid using format strings without format
  specifiers, fixing a build failure with -Werror=format-security.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- The patch adds format specifiers to existing calls, ensuring that the code remains
  functional and secure.
exchanges:
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Proposes a patch to fix a build failure due to using format strings without
    format specifiers.
  quote: null
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Suggests dropping the patch on i686, as the issue should be present on
    all platforms. Also requests mentioning that the patch fixes PR binutils/34168
    in the commit log.
  quote: Drop on i686.   It should fail with -Werror=format-security on all platforms.
- author: Will Hawkins <hawkinsw@obs.cr>
  role: other
  position: Agrees to drop the i686-specific fix and include the PR number in the
    commit message.
  quote: Agree and will do!
primer_expert: This patch modifies ``opcodes/i386-dis.c`` to address a format string
  vulnerability. The disassembler uses ``i386_dis_printf`` to print output, and the
  patch ensures that format strings are always accompanied by appropriate format specifiers.
  This resolves a build error triggered by ``-Werror=format-security``.
primer_general: A disassembler translates machine code into human-readable assembly
  language. Format string vulnerabilities occur when a program uses user-controlled
  input as a format string in functions like ``printf``. This patch fixes such a vulnerability
  in the x86 disassembler by ensuring that all format strings are properly specified,
  thereby preventing potential security issues and build failures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260524030619.1313131-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch modifies the x86 disassembler to avoid using format strings without format specifiers, which fixes a build failure when compiling with ``-Werror=format-security`` on i686. The patch addresses issue PR binutils/34168.
