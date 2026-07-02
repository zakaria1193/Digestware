---
project: binutils
subsystem: readelf
patch_id: null
tags:
- binutils
- readelf
- ELF
- bugfix
- GOT
discussion_id: 9ba3a26a-2cff-411a-8629-dc1e073e6182@suse.com
source_type: public_inbox
title: 'Re: [PATCH] readelf: Also set do_got_section_contents to false'
headline: 'readelf: Also set do_got_section_contents to false'
tldr: Fixes readelf to correctly set do_got_section_contents to false when section
  headers fail to load.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves robustness of `readelf` when handling ELF files with invalid section headers.
- Ensures consistent behavior regardless of section header loading success.
exchanges:
- author: H.J. Lu
  role: contributor
  position: Suggests setting do_got_section_contents to false if section headers fail
    to load, referencing PR binutils/34323.
  quote: 'Also set do_got_section_contents to false if section headers are failed

    to load.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges and agrees with the proposed change.
  quote: Okay.
primer_expert: This patch modifies `readelf.c` to conditionally set `do_got_section_contents`
  to false. Previously, this flag was only set to false if section headers were successfully
  processed. The change ensures this flag is also set to false if section header loading
  fails, aligning with the fix for PR binutils/34323 and likely preventing incorrect
  processing or output related to the GOT section in error scenarios.
primer_general: This is a small correction to the `readelf` utility, which is part
  of the binutils suite. `readelf` is used to display information about ELF files
  (a common executable file format on Linux and other Unix-like systems). The change
  ensures that if `readelf` encounters an error while trying to read the section headers
  of a file, it will correctly mark that it should not attempt to process the contents
  of the Global Offset Table (GOT). This prevents potential errors or misleading output
  when dealing with corrupted or unusual ELF files.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/9ba3a26a-2cff-411a-8629-dc1e073e6182@suse.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This change ensures that the `do_got_section_contents` flag in `readelf` is set to `false` not only when section headers are successfully loaded but also when their loading fails. This correction, prompted by PR binutils/34323, prevents potential issues by accurately reflecting the state of section header processing.
