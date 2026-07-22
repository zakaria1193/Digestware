---
project: binutils
subsystem: testsuite
patch_id: null
tags:
- binutils
- testsuite
- elf
- symbols
- regression
discussion_id: alpine.DEB.2.21.2607211343170.14485@angie.orcam.me.uk
source_type: public_inbox
title: '[PATCH] testsuite: Also exclude `*-*-kfreebsd*-gnu'' from STB_GNU_UNIQUE tests'
headline: 'testsuite: Exclude `*-*-kfreebsd*-gnu'' from STB_GNU_UNIQUE tests'
tldr: Patch updates binutils testsuite to correctly exclude kfreebsd-gnu targets from
  STB_GNU_UNIQUE symbol tests.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Correctness of test suite exclusions for specific target architectures.
- Ensuring accurate reporting of feature support (STB_GNU_UNIQUE).
exchanges:
- author: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
  role: proposer
  position: Submits a patch to correct testsuite exclusions for kfreebsd-gnu targets
    regarding STB_GNU_UNIQUE symbols.
  quote: "Fix commit 02e0be69012a (\"mbind gas tests and supports_gnu_osabi \ntestsuite\
    \ infrastructure\") and also match `*-*-kfreebsd*-gnu' targets \nwhen determining\
    \ whether STB_GNU_UNIQUE binding is supported for \nsymbols."
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions if the '-gnu' suffix is strictly necessary in the exclusion
    pattern.
  quote: Is the -gnu at the end really needed here? If yes, it'
- author: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
  role: contributor
  position: Clarifies that the '-gnu' suffix is necessary because kfreebsd-gnu targets
    share characteristics with FreeBSD targets regarding ELFOSABI.
  quote: 'On Tue, 21 Jul 2026, Jan Beulich wrote:


    > --- binutils-gdb.orig/binutils/testsuite/lib/binutils-common.exp

    > +++ binutils-gdb/binutils/testsuite/lib/binutils-common.exp

    > @@ -308,7 +308,7 @@ proc is_elf_unused_section_symbols {} {

    >  # This require ELFOSABI_GNU, and `bfd_elf_final_link''.

    >  #

    >  proc supports_gnu_unique {} {

    > -    if { [istarget *-*-freebsd*] } {

    > +    if { [istarget *-*-freeb…'
primer_expert: This patch modifies binutils' test suite, specifically the `supports_gnu_unique`
  function in `binutils-common.exp`. It adds `*-*-kfreebsd*-gnu` to the list of targets
  that do not support `STB_GNU_UNIQUE` symbols. This is because `kfreebsd-gnu` targets
  use the same BFD symbols and `ELFOSABI_FREEBSD` as `*-*-freebsd*` targets, which
  were already excluded. The change addresses regressions seen on `mips-kfreebsd-gnu`
  related to symbol visibility and unique symbol handling.
primer_glossary:
- term: STB_GNU_UNIQUE
  definition: A symbol binding type in the ELF format, used for symbols that must
    be unique across shared libraries.
- term: kfreebsd-gnu
  definition: A target triplet indicating a GNU system running on a FreeBSD kernel.
- term: BFD
  definition: Binary File Descriptor library, used by binutils to handle various object
    file formats.
- term: ELFOSABI_FREEBSD
  definition: An ELF operating system ABI (Application Binary Interface) identifier
    specific to FreeBSD.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2607211343170.14485@angie.orcam.me.uk
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This patch updates the binutils test suite to correctly exclude `*-*-kfreebsd*-gnu` targets from tests related to `STB_GNU_UNIQUE` symbols. It aligns the exclusion logic with FreeBSD targets, which use the same BFD vectors and ELFOSABI_FREEBSD. This fix resolves several regressions observed on mips-kfreebsd-gnu related to symbol visibility and unique symbol handling.
