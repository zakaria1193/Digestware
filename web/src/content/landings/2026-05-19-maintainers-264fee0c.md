---
project: gcc
subsystem: maintainers
patch_id: null
tags:
- maintainers
- sort
commit_hash: 264fee0cb090f1d084872f3f24be7f7c38d24e69
source_type: github
author: Richard Earnshaw
headline: 'MAINTAINERS: Sort the OS Port Maintainers.'
tldr: The `OS Port Maintainers` section in `MAINTAINERS` is now sorted by operating
  system and then user.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the MAINTAINERS file, specifically the 'OS Port
  Maintainers' section. The entries are now sorted by operating system and then user,
  which improves organization.
primer_general: The `MAINTAINERS` file lists who is responsible for different parts
  of the GCC project, and who should review patches. This commit sorts the list to
  make it easier to find the right person.  Specifically, the 'OS Port Maintainers'
  are now sorted first by operating system and then by username.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/264fee0cb090f1d084872f3f24be7f7c38d24e69
date: '2026-05-19'
is_stub: false
---

The MAINTAINERS file's "OS Port Maintainers" section is now sorted by operating system and then user. This change improves the organization and readability of the list, making it easier to locate specific maintainers.
