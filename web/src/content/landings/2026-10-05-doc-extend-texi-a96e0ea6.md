---
project: gcc
subsystem: doc/extend.texi
patch_id: null
tags:
- documentation
commit_hash: a96e0ea68af7a9fbc312e3b4ba22b6a784fdd59d
source_type: github
author: Andreas Schwab
headline: Typo corrected in GCC extend.texi documentation
tldr: A typographical error in the GCC extend.texi documentation has been fixed.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects a typo within the `doc/extend.texi` file, specifically
  in the section detailing 'Other Builtins'. The fix ensures the documentation accurately
  reflects the intended information.
primer_glossary:
- term: extend.texi
  definition: A TeXinfo file used in GCC documentation to describe language extensions,
    attributes, and other advanced features beyond the standard language specification.
- term: Other Builtins
  definition: A section in GCC's documentation that describes various built-in functions
    provided by the compiler, which are not part of the standard language but offer
    extended capabilities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a96e0ea68af7a9fbc312e3b4ba22b6a784fdd59d
date: '2026-10-05'
is_stub: true
stub_reason: low_score
---

A minor typo in the GCC `extend.texi` documentation has been corrected. The change updates text under the 'Other Builtins' section, improving the accuracy of the documentation.
