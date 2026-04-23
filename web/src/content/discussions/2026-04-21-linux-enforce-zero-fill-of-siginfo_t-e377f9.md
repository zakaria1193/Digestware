---
project: glibc
subsystem: linux
patch_id: null
tags:
- glibc
- signal handling
- ABI
- zero-initialization
- LoongArch32
discussion_id: 20260120131337.2574254-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v2] linux: Enforce zero fill of siginfo_t'
headline: 'linux: Enforce zero fill of siginfo_t'
tldr: This patch enforces zero-filling of the siginfo_t struct in glibc to avoid issues
  caused by differences between the glibc struct size and the kernel ABI.
stakes: Ensures correct signal handling and avoids potential false positives in tests,
  particularly on architectures like armhf and LoongArch32.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a `memset` call, which introduces a small runtime overhead.
- Avoids potential compatibility issues arising from compiler-specific struct initialization.
- Ensures adherence to kernel ABI requirements for signal handling.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Asks for the patch to be pushed to master, noting that tst-pidfd fails
    on LoongArch32 without it.
  quote: 'Can this patch be pushed to master?

    tst-pidfd also failed on LoongArch32 without this patch.'
- author: Florian Weimer <fweimer@redhat.com>
  role: reviewer
  position: Believes the explanation of the change is wrong but agrees that the code
    change itself is correct.
  quote: 'I still think the explanation of this change is wrong (I think it''s that

    designated initializers with unions do not necessary zero-initialize

    inactive members), but the code change itself is correct.'
- author: mengqinggang <mengqinggang@loongson.cn>
  role: contributor
  position: Points out that GCC can zero-initialize the whole struct.
  quote: 'Gcc zero-initialize the whole struct like this:

    https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124356'
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: maintainer
  position: Asks for suggestions about the explanation in the commit message.
  quote: 'What about: '
primer_expert: The glibc defines a `siginfo_t` struct, used for signal handling. Its
  size may exceed the kernel ABI's expectation, leading to discrepancies in zero-initialization.  Specifically,
  the kernel expects trailing bytes to be zeroed when the `si_code` field is unknown.  Compiler
  variations (e.g., gcc-15 on armhf) exacerbate this. The patch adds `memset` to ensure
  consistent zero-filling, working around potential ABI mismatches.
primer_general: Signals are a fundamental mechanism for inter-process communication
  and for the kernel to notify processes of events. When a signal is sent, a `siginfo_t`
  struct carries details about the signal.  To ensure compatibility and security,
  the kernel expects this struct to be zero-filled in certain cases. However, differences
  in compiler versions and architecture-specific implementations can lead to inconsistent
  initialization of the `siginfo_t` struct, causing unexpected behavior or security
  vulnerabilities. This patch explicitly initializes the struct with zeros to avoid
  these issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/a033e4c0-24fe-4e8b-b381-bb06f810414c@loongson.cn
bugzilla_url: null
date: '2026-04-21'
---

The glibc siginfo struct is larger than the kABI one, and the kernel enforces zero-filling of extra bytes for unknown si_code values. This patch adds a memset to explicitly zero-fill the struct before use, avoiding potential issues with compiler optimizations or architecture-specific behavior. A LoongArch32 failure is also resolved by this patch.
