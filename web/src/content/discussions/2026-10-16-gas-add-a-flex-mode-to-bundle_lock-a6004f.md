---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- optimization
- performance
- instruction-alignment
discussion_id: 0a5ff4f1-a186-44fc-9e9d-c22fe4df6f60@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] gas: add a flex mode to .bundle_lock'
headline: 'gas: add a flex mode to .bundle_lock'
tldr: Proposes a flexible .bundle_lock directive for aligning hot code regions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased flexibility for hot-region alignment vs. potential complexity in handling
  arbitrary overlaps and nested regions.
- Allows compilers to better optimize for fetch efficiency when instruction encoding
  size is dynamic, at the cost of more complex assembler logic.
exchanges:
- author: Sarvesh Chandra
  role: proposer
  position: Proposes to allow .bundle_lock flex N to accept a locked sequence larger
    than the bundle size, maintaining start alignment while tolerating unknown region
    lengths.
  quote: 'Allow .bundle_lock flex N to accept a locked sequence larger than the bundle

    size.  Ordinary .bundle_lock keeps its strict behaviour.


    The motivation is hot-region alignment: a compiler may want the entry of a

    hot region (for example a loop) to start on a bundle/fetch boundary so the

    front end fetches it in as few cycles as possible, even when the region is

    larger than a single bundle.  The stric…'
- author: Jan Beulich
  role: reviewer
  position: Questions whether arbitrary overlaps between bundle_lock regions are intended
    and feasible, and how nested flex regions with different size parameters would
    function.
  quote: 'From looking at the code, this doesn''t look to be just nesting. It instead

    appears as if arbitrary overlaps are permitted. That, I fear, can''t work

    very well.


    I also can''t see how nested flex regions with differing size values can

    work. You can only possibly satisfy one of the sizes which are in effect.'
primer_expert: This patch proposes a new directive, `.bundle_lock flex N`, for the
  GNU Assembler (GAS). It aims to address hot-region alignment by allowing a sequence
  to be aligned to an N-bundle boundary while permitting it to exceed N bundles. This
  differs from the existing strict `.bundle_lock` which requires the entire sequence
  to fit within a single bundle. The core issue is aligning code sections for optimal
  instruction fetching when their final size is not known at assembly time. A reviewer
  is concerned about the implications of arbitrary region overlaps and nested flex
  regions.
primer_glossary:
- term: bundle
  definition: In the context of some instruction set architectures (like VLIW or specific
    embedded processors), a bundle is a group of instructions that are fetched and
    executed together. Aligning code to bundle boundaries can optimize instruction
    fetch efficiency.
- term: hot-region alignment
  definition: Aligning frequently executed code blocks (hot regions) to specific boundaries,
    such as cache lines or instruction fetch boundaries, to improve performance by
    reducing instruction fetch latency.
- term: directive
  definition: A command within an assembly language source file that provides information
    to the assembler, such as defining data, controlling the assembly process, or
    specifying alignment.
- term: frag
  definition: A 'fragment' in the context of an assembler. It represents a piece of
    output, such as code or data, that will eventually be part of the object file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0a5ff4f1-a186-44fc-9e9d-c22fe4df6f60@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch introduces a new 'flex' mode for the .bundle_lock directive in gas, intended to improve hot-region alignment. The current strict mode requires the entire sequence to fit within a single bundle, which is problematic when the exact instruction encoding is unknown. The 'flex' mode allows alignment to a specified bundle size while permitting the sequence to span multiple bundles, addressing the compiler's need to optimize for fetch-window alignment without precise length knowledge. A reviewer raises concerns about arbitrary overlaps and the handling of nested flex regions with differing sizes.
