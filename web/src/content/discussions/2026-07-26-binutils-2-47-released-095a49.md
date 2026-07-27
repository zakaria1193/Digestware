---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release
- binutils
- new features
- risc-v
discussion_id: 87o6fty5pz.fsf@redhat.com
source_type: public_inbox
title: Release 2.47 of the GNU Binutils is now available
headline: Binutils 2.47 released
tldr: Announces the release of GNU Binutils version 2.47, highlighting new features
  and bug fixes.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 7
technical_tradeoffs:
- New features and bug fixes in version 2.47 enhance functionality and stability.
- Exclusion of GOLD linker sources from this release adheres to a policy but might
  require users needing GOLD to stick to even-numbered releases or use separate sources.
- Concerns about release tarball integrity due to a development flag being present.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Announces the release of Binutils 2.47, detailing new features like `--reloc-section-sym`
    and RISC-V extensions, and providing download links and checksums.
  quote: "We are pleased to announce that version 2.47 of the GNU Binutils project\n\
    sources have been released and are now available for download at:\n\n  https://ftp.gnu.org/gnu/binutils\n\
    \  https://sourceware.org/pub/binutils/releases/"
- author: Matthias Klose <doko@debian.org>
  role: reviewer
  position: Notes that `bfd/development.sh` still shows `development=true` in the
    tarballs, suggesting they might be development snapshots.
  quote: "bfd/development.sh still has development=true set in the tarballs, so \n\
    this looks like a snapshot."
primer_expert: This is an announcement for the release of GNU Binutils 2.47. It calls
  out significant new features such as the `--reloc-section-sym` option for more granular
  control over section symbol processing in relocations, and the addition of several
  new RISC-V standard extensions. The announcement also mentions that GOLD linker
  sources are not included in this release, consistent with the project's release
  cadence for odd-numbered versions. A follow-up comment raises a concern about the
  reproducibility or stability of the release tarballs, citing the presence of `development=true`
  in an internal scri…
primer_glossary:
- term: relocation
  definition: The process of updating symbolic machine code references (like function
    or variable addresses) in an object file or executable to their final memory addresses
    during the linking or loading phase.
- term: PLT
  definition: Procedure Linkage Table. A table used in executable files and shared
    libraries to resolve indirect function calls to functions that are not defined
    in the current module, typically used for dynamic linking.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA). The release notes
    mention support for specific standard extensions of RISC-V.
- term: GOLD linker
  definition: A newer, faster linker developed by the GNU Project as a replacement
    for the traditional `ld`. Its sources are not included in odd-numbered Binutils
    releases as per project policy.
- term: tarball
  definition: A compressed archive file, typically created using the tar utility,
    which bundles software source code or files for distribution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87o6fty5pz.fsf@redhat.com
bugzilla_url: null
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

This announcement details the release of GNU Binutils version 2.47, available for download. Key new features include a new command-line option `--reloc-section-sym` for controlling relocation for local symbols and expanded support for RISC-V standard extensions. As an odd-numbered release, it does not include sources for the GOLD linker. Concerns are raised in a reply that `bfd/development.sh` still indicates `development=true` in the tarballs, suggesting they might be development snapshots rather than stable releases.
