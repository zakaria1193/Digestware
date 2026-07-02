---
project: binutils
subsystem: chore
patch_id: null
tags:
- documentation
- typo
- linker
discussion_id: 20260507112525.540131-1-pranavrjoshi1@gmail.com
source_type: public_inbox
title: '[PATCH] chore: correct misrepresented wording'
headline: Correct misrepresented wording
tldr: Fixes a typo in ld.texi ('subseque nt' -> 'subsequent').
proposer: Pranav Joshi <pranavrjoshi1@gmail.com>
consensus: Committed
outcome: proposed
impact_score: 1
sentiment_score: 10
technical_tradeoffs:
- None. This is a straightforward typo fix.
exchanges:
- author: Pranav Joshi <pranavrjoshi1@gmail.com>
  role: proposer
  position: Proposes a patch to correct the misspelling of "subsequent" in the ld.texi
    file.
  quote: 'The file ld.texi contains two space-separated terms: ''subseque nt''. It
    was probably meant to be ''subsequent''.'
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Acknowledges the patch and notes that there is only one instance of the
    error, which he will correct when committing the patch.
  quote: 'Nit: As per the patch contents it''s only one. I''ll adjust while committing.'
primer_expert: This cleans up a typo in the linker manual's Texinfo source file.  Texinfo
  is a plain-text markup format for producing documentation, and the linker manual
  is a key reference for users of the GNU linker.
primer_general: Binutils includes the GNU linker (`ld`), which combines compiled object
  files into executables and libraries.  The linker's behavior is controlled by command-line
  options and linker scripts, all documented in the manual. This patch corrects a
  typo in the manual, improving the clarity and accuracy of the documentation for
  users.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260507112525.540131-1-pranavrjoshi1@gmail.com
bugzilla_url: null
date: '2026-05-07'
---

This patch corrects a typographical error in the binutils documentation file `ld.texi`.  The misspelled word 'subseque nt' is corrected to 'subsequent'. Jan Beulich notes the patch fixes only one instance, and promises to adjust while committing.
