---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- Xtensa
- security
- buffer overflow
- relocation
discussion_id: aum7neb5qQ87r3z9@squeak.grove.modra.org
source_type: public_inbox
title: xtensa_insnbuf_from_chars buffer overflow checking
headline: xtensa_insnbuf_from_chars buffer overflow checking
tldr: Patch adds buffer overflow checking to xtensa_insnbuf_from_chars in binutils,
  gas, and gdb to handle malformed relocations.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: under_review
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Adds checks and wrappers, potentially increasing code complexity and slightly impacting
  performance in non-error cases.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a fix for a buffer overflow in xtensa_insnbuf_from_chars by adding
    size checks and updating its usage in gas and gdb.
  quote: R_XTENSA_ASM_SIMPLIFY has size zero, thus it can appear right at the end
    of a section without failing bfd_reloc_offset_in_range. Of course the reloc should
    never appear at the end of a section let alone in debug sections, but fuzzers
    do horrible things.
- author: Max Filippov <jcmvbkbc@gmail.com>
  role: reviewer
  position: Acknowledges the issue with R_XTENSA_ASM_SIMPLIFY and the proposed solution,
    discussing the use of a wrapper function for gas.
  quote: 'On Tue, Nov 3, 2026 at 2:46 AM Alan Modra <amodra@gmail.com> wrote:

    > R_XTENSA_ASM_SIMPLIFY has size zero, thus it can appear right at the

    > end of a section without failing bfd_reloc_offset_in_range. Of course

    > the reloc should never appear at the end of a section let alone in

    > debug sections, but fuzzers do horrible things.'
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Clarifies the implementation details of the `xtensa_insnbuf_from_frag`
    wrapper and its relation to gas frags.
  quote: '+/* Wrapper for xtensa_insnbuf_from_chars to convert frag bytes

    +   to xtensa_insnbuf.  */


    +static bool

    +xtensa_insnbuf_from_frag (xtensa_isa isa, xtensa_insnbuf insnbuf,

    +                         const fragS *frag, size_t off)

    +{

    +  const unsigned char *buf = (const unsigned char *) frag->fr_literal + off;

    +  size_t len = frag-'
- author: Max Filippov <jcmvbkbc@gmail.com>
  role: reviewer
  position: Responds to Alan's clarification, indicating that the changes look reasonable.
  quote: 'On Tue, Nov 3, 2026 at 3:04 PM Alan Modra <amodra@gmail.com> wrote:

    On Tue, Nov 03, 2026 at 05:22:26AM -0800, Max Filippov wrote:

    > On Tue, Nov 3, 2026 at 2:46 AM Alan Modra <amodra@gmail.com> wrote:

    > > +/* Wrapper for xtensa_insnbuf_from_chars to convert frag bytes

    > > +   to xtensa_insnbuf.  */

    > > +

    > > +static bool

    > > +xtensa_insnbuf_from_frag (xtensa_isa isa, xtensa_insnbuf insnbuf,

    > > +…'
primer_expert: A buffer overflow vulnerability in the Xtensa ELF backend's `xtensa_insnbuf_from_chars`
  function is being addressed. The issue arises from R_XTENSA_ASM_SIMPLIFY relocations
  with zero size, which can bypass range checks and lead to reading beyond allocated
  buffers when `num_chars` is zero. The patch updates the function and its callers
  in gas and gdb to correctly handle buffer sizes and check return values, preventing
  overflows.
primer_glossary:
- term: xtensa_insnbuf_from_chars
  definition: A function within binutils used for Xtensa processors to convert character
    data into an instruction buffer, potentially susceptible to buffer overflows.
- term: R_XTENSA_ASM_SIMPLIFY
  definition: A relocation type specific to the Xtensa architecture, used in assembly
    processing.
- term: relocation
  definition: A symbol or pointer in an object file that needs to be resolved by the
    linker before the program can be executed. Relocations contain information about
    how to modify addresses or other data.
- term: gas
  definition: The GNU Assembler, a component of the GNU toolchain that translates
    assembly language code into machine code.
- term: bfd
  definition: The Binary File Descriptor library, a GNU library used by binutils components
    to provide a common interface to various object file formats.
- term: fuzzer
  definition: A tool that automatically generates malformed or random data as input
    to a program to discover bugs, such as buffer overflows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aum7neb5qQ87r3z9@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This patch addresses a buffer overflow vulnerability in binutils' xtensa_insnbuf_from_chars function, which can be triggered by malformed R_XTENSA_ASM_SIMPLIFY relocations. The fix modifies xtensa_insnbuf_from_chars to return buffer size validity, updates gas and gdb to pass actual buffer lengths, and adds status checks. This prevents potential overflows when processing zero-sized buffers, which fuzzers might generate.
