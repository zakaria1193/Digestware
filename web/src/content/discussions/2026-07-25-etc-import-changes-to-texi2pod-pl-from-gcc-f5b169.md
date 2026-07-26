---
project: binutils
subsystem: etc
patch_id: null
tags:
- documentation
- scripting
- Perl
- Texinfo
- binutils
discussion_id: 91dfc026f843cfb510445198bbc9b63552b04e4a.1784980082.git.aburgess@redhat.com
source_type: public_inbox
title: '[PATCH] etc: import changes to texi2pod.pl from gcc'
headline: 'etc: import changes to texi2pod.pl from gcc'
tldr: Binutils' texi2pod.pl script updated by importing changes from GCC, including
  improved @option and @table support, with necessary local adjustments.
proposer: Andrew Burgess <aburgess@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Syncing with GCC's script reduces maintenance effort for `texi2pod.pl` but requires
  handling differences and local modifications.
- The license change from GPLv2 to GPLv3 might have implications for compatibility
  with other components under different licenses.
exchanges:
- author: Andrew Burgess <aburgess@redhat.com>
  role: proposer
  position: Proposes updating Binutils' `texi2pod.pl` by syncing with GCC's version,
    detailing the necessary local modifications and explaining the rationale.
  quote: 'I was looking at making some cleanup in the GDB documentation and I

    ran into a limitation of the texi2pod.pl script, it is not able to

    correctly format: ''@option{--text}'' or ''@table @option''.


    Patching our copy of texi2pod.pl is easy enough, but it is probably

    better to just sync with gcc''s version of the script, which already

    has some @option support in place.'
primer_expert: This patch updates the `texi2pod.pl` script within the Binutils repository,
  which is responsible for converting Texinfo documentation into Pod format (used
  by Perl and others). The update primarily synchronizes with GCC's `texi2pod.pl`,
  bringing in fixes for handling `@option` directives and `@table @option` constructs.
  The author had to re-introduce several local changes specific to Binutils' build
  and documentation system, including support for `--no-split`, `TARGET` sections,
  and reverting a problematic GCC commit.
primer_glossary:
- term: texi2pod.pl
  definition: A Perl script used in GNU projects to convert Texinfo documentation
    format into Pod (Plain Old Documentation) format, which is used by Perl and other
    tools.
- term: Texinfo
  definition: A documentation system and format used by the GNU project. It can output
    to multiple formats, including HTML, PDF, and Info files.
- term: Pod
  definition: Plain Old Documentation. A simple markup language used for documenting
    Perl modules and scripts, and also used by other projects like GNU's texi2pod.pl.
- term: '@option'
  definition: A Texinfo command used to format command-line options within documentation.
- term: '@table'
  definition: A Texinfo command used to create lists or tables of items, often used
    for options or commands.
- term: GPLv2 / GPLv3
  definition: GNU General Public License version 2 and version 3. Open-source licenses
    that govern the distribution and modification of software. GPLv3 is a later, more
    comprehensive version.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/91dfc026f843cfb510445198bbc9b63552b04e4a.1784980082.git.aburgess@redhat.com
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

The `texi2pod.pl` script in Binutils has been updated by importing recent changes from GCC's version. This addresses limitations in handling `@option{--text}` and `@table @option` for documentation generation. Several local adjustments were made to accommodate Binutils-specific needs, such as support for `--no-split` and `TARGET` sections, and reverting a GCC commit that broke list formatting. The change also updates the script's license from GPLv2 to GPLv3.
