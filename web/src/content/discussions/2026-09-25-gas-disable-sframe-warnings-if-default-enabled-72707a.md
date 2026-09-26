---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- binutils
- warnings
- portability
- sframe
discussion_id: 874ifdbpt0.fsf@gentoo.org
source_type: public_inbox
title: 'Re: [PATCH v2 2/2] gas: disable SFrame warnings if default-enabled'
headline: 'gas: Disable SFrame warnings if default-enabled'
tldr: A discussion on removing a GCC extension for variable argument lists (`__VA_ARGS__`)
  from gas's SFrame warning macro to improve portability.
proposer: Sam James <sam@gentoo.org>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensuring portability by avoiding compiler-specific extensions.
- Maintaining the intended warning suppression logic across different C standards.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Requests the removal of a GCC extension (`__VA_ARGS__`) from the `sframe_as_warn`
    macro, citing a previous commit that already addressed this issue.
  quote: 'As per 26ea095fa700 ("gas/gen-sframe: avoid gcc extension using __VA_ARGS__")

    please avoid using a gcc extension here.'
- author: Sam James
  role: proposer
  position: Acknowledges the feedback regarding the GCC extension and agrees to correct
    the macro, attributing the oversight to a long-running development branch.
  quote: The perils of long-running branches. Thanks.
primer_expert: This patch for the GNU Assembler (gas) aims to modify how SFrame warnings
  are handled. The macro `sframe_as_warn` is intended to only issue warnings when
  SFrames are explicitly enabled via a command-line flag, not when they are the default
  behavior. The discussion centers on removing a GCC-specific `__VA_ARGS__` syntax
  from this macro to ensure compatibility with other C compilers.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language code into machine code.
- term: SFrame
  definition: Likely refers to a mechanism for generating stack frame unwind information,
    possibly related to debugging or exception handling. The exact nature is not fully
    specified but relates to code generation in gas/ld.
- term: Warning
  definition: A diagnostic message issued by a compiler or assembler indicating a
    potential problem or non-standard code construct, but not necessarily an error
    that prevents compilation.
- term: __VA_ARGS__
  definition: A GCC-specific preprocessor extension that represents all arguments
    passed to a variadic macro.
- term: Macro
  definition: A fragment of code that is given a name. When the code is compiled,
    the macro name is replaced by the contents of the macro.
series_id: 'binutils:gas: disable sframe warnings if default-enabled'
series_role: reply
series_parts:
- title: 'gas: disable SFrame warnings if default-enabled'
  url: https://inbox.sourceware.org/binutils/7412e0a0-bb47-456e-a655-01d5f4c77e09@suse.com
  n: 2
  total: 2
- title: 'gas: disable SFrame warnings if default-enabled'
  url: https://inbox.sourceware.org/binutils/cc7fa897c458eff874dd765b51361b98d3688623.1790321423.git.sam@gentoo.org
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/874ifdbpt0.fsf@gentoo.org
bugzilla_url: null
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

Sam James is asked by Jan Beulich to remove a GCC-specific `__VA_ARGS__` extension from the `sframe_as_warn` macro in gas. The macro is intended to suppress warnings when SFrames are enabled by default. James acknowledges the issue, attributing it to a long-running branch, and agrees to fix it.
