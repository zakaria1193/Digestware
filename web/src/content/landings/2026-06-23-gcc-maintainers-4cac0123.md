---
project: gcc
subsystem: gcc/maintainers
patch_id: null
tags:
- maintenance
- governance
commit_hash: 4cac01232fc42db21b514b74549190773abe8a55
source_type: github
author: Richard Earnshaw
headline: MAINTAINERS lists missing write-after accounts.
tldr: The MAINTAINERS file has been updated to include missing 'write-after' entries
  for several maintainer accounts.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `MAINTAINERS` file in GCC, specifically the
  'Write After' section. This section declares specific Sourceware accounts authorized
  for post-commit actions (e.g., commit approvals or branch pushes). The change adds
  missing entries for various individuals whose roles previously lacked this explicit
  authorization. Concurrently, an inactive maintainer has been removed from the `nds32`
  CPU port section, improving the accuracy of maintainer associations.
primer_general: Open-source projects like GCC (the GNU Compiler Collection) have a
  `MAINTAINERS` file that lists who is responsible for different parts of the code.
  This file helps organize development, clarifies who can approve changes, and ensures
  accountability. This commit updates that `MAINTAINERS` file to add a 'Write After'
  section for several people. This 'Write After' entry links a maintainer's name to
  their specific account on `sourceware.org`, the system used for GCC development.
  It's a formal way of ensuring that the right people have the necessary permissions
  for their roles. Additionally, one person who is no longer active in maintaining
  the 'nds32 CPU Ports' section has been removed to keep the file current.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4cac01232fc42db21b514b74549190773abe8a55
date: '2026-06-23'
is_stub: false
---

This commit updates the GCC MAINTAINERS file to correctly list several maintainers' associated Sourceware accounts in the 'Write After' section. This ensures that the record of who is authorized to commit changes to specific areas of the GCC codebase is accurate and complete. Additionally, one maintainer no longer active in the 'nds32 CPU Ports' section has been removed.
