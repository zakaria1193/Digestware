---
project: binutils
subsystem: elf
patch_id: null
tags:
- PowerPC
- ELF
- core dump
- BFD
- readelf
discussion_id: 66e0c229-2686-4047-9209-1f84b6a94f71@linux.ibm.com
source_type: public_inbox
title: 'Re: Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
headline: 'Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
tldr: Surya Kumari Jangala is added to a thread discussing a PowerPC core file support
  patch, following multiple pings from the original author.
proposer: Surya Kumari Jangala <jskumari@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding support for new hardware features requires modifications across multiple
  tools (BFD, readelf, GDB).
- Balancing the need for timely feature support with thorough code review.
exchanges:
- author: Surya Kumari Jangala <jskumari@linux.ibm.com>
  role: other
  position: Added to the thread to address a pending patch for PowerPC core file support.
  quote: 'Hi,


    On 17/09/26 3:19 PM, Abhay Kandpal wrote:

    > Adding Surya to this thread.'
- author: Abhay Kandpal <abhay.kandpal@samsung.com>
  role: proposer
  position: Originally submitted a patch to add PowerPC DMR core file support and
    is repeatedly pinging for review.
  quote: 'Hi all,

    Just a gentle ping to see if anyone has had a chance to review this patch,

    or if any further changes are needed on my end.'
primer_expert: This discussion is a follow-up on a patch intended for the GNU Binutils
  project, specifically targeting ELF core file handling for PowerPC processors. The
  patch introduces support for a new note type, `NT_PPC_DMR`, which stores the contents
  of Dense Math Registers (DMR). These registers are part of a future Power ISA revision.
  The patch modifies BFD (the Binary File Descriptor library) and `readelf` to recognize
  and process this new note type during core file analysis. The thread is active due
  to multiple 'ping' messages from the author requesting a review, and the addition
  of a new participa…
primer_glossary:
- term: NT_PPC_DMR
  definition: A specific ELF note type designed to store the contents of Dense Math
    Registers (DMR) for PowerPC processors in core dump files.
- term: core file
  definition: A file that contains a snapshot of a program's memory state at the time
    of a crash, used for debugging.
- term: PowerPC
  definition: A family of RISC microprocessors based on the PowerPC architecture,
    developed by Apple, IBM, and Motorola.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a low-level
    interface for reading and writing various binary file formats, including object
    files and core dumps.
- term: readelf
  definition: A utility from GNU Binutils that displays information about ELF files,
    including their sections, symbols, and notes.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: DMR
  definition: Dense Math Registers, a set of specialized registers on future PowerPC
    processors for accelerating math operations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/66e0c229-2686-4047-9209-1f84b6a94f71@linux.ibm.com
bugzilla_url: null
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This email thread concerns a patch adding support for the `NT_PPC_DMR` note type in PowerPC core files for BFD and readelf. The patch, originally submitted by Abhay Kandpal, has seen multiple pings requesting review. Surya Kumari Jangala has now been added to the discussion, likely to provide review or further input on the proposed changes for handling Dense Math Registers (DMR) in core dumps.
