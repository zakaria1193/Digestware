---
project: gcc
subsystem: lto
patch_id: null
tags:
- gcc
- lto
- avr
- backend
- static variable
discussion_id: 63787b08-10ac-4200-af5c-433de283d2b8@gjlay.de
source_type: public_inbox
title: 'lto: from insert_attributes to file_end?'
headline: 'Lto: How to handle static variables in LTO compilations?'
tldr: The avr backend uses a static variable set in TARGET_INSERT_ATTRIBUTES and used
  in TARGET_ASM_FILE_END, but this doesn't work in LTO compilations.  The author…
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Need to find a way to share state between different stages of the LTO compilation
  process.
- Consider alternatives to static variables for storing state.
- Potential performance impact of different state sharing mechanisms.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Asks for the recommended way to handle a static variable that is set in
    `TARGET_INSERT_ATTRIBUTES` and used in `TARGET_ASM_FILE_END`, which doesn't work
    as expected in LTO compilations because the two targets run in different compilation
    stages.
  quote: 'In the avr backend there is a static variable avr_no_call_main_p that is
    set in TARGET_INSERT_ATTRIBUTES and used in TARGET_ASM_FILE_END.


    This works as expected in non-LTO compilations, with LTO however, TARGET_INSERT_ATTRIBUTES
    runs in cc1[plus] but TARGET_ASM_FILE_END is run by lto1, hence the variable is
    not set as expected.'
- author: Richard Biener <richard.guenther@gmail.com>
  role: other
  position: Acknowledges the problem without offering a solution.
  quote: null
- author: Georg-Johann Lay <avr@gjlay.de>
  role: other
  position: Repeats the problem description.
  quote: null
- author: Sam James <sam@gentoo.org>
  role: other
  position: Repeats the problem description.
  quote: null
primer_expert: In the AVR backend, the `TARGET_INSERT_ATTRIBUTES` hook sets `avr_no_call_main_p`,
  which is later used in `TARGET_ASM_FILE_END`. During LTO, these hooks execute in
  different stages (`cc1plus` vs. `lto1`), breaking the expected behavior due to the
  static variable's scope. Handling state consistently across LTO stages requires
  careful consideration of variable scope and data persistence.
primer_general: '`TARGET_INSERT_ATTRIBUTES` and `TARGET_ASM_FILE_END` are target-specific
  hooks in GCC that allow backends (like AVR) to modify attributes of functions and
  emit final assembly instructions, respectively.  LTO splits the compilation process
  into multiple stages, some of which happen in separate processes.  This split can
  cause issues when target hooks rely on static variables to share state between stages,
  as those variables may not be visible in all stages. The challenge lies in ensuring
  that the necessary information is available in both the initial compilation stage
  and the final assembly generation stage when LTO is enabled. This requires alternative
  mechanisms for sharing data, such as explicitly passing it through the LTO pipeline.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/63787b08-10ac-4200-af5c-433de283d2b8@gjlay.de
bugzilla_url: null
date: '2026-05-05'
---

The avr backend defines a static variable, `avr_no_call_main_p`, in `TARGET_INSERT_ATTRIBUTES` and uses it in `TARGET_ASM_FILE_END`. This works for non-LTO compilations, but in LTO, `TARGET_INSERT_ATTRIBUTES` runs in `cc1[plus]` while `TARGET_ASM_FILE_END` runs in `lto1`, so the variable is not set as expected. The author is asking for the recommended way to handle this issue.
