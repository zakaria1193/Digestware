---
project: gcc
subsystem: gcc/libgfortran
patch_id: null
tags:
- libgfortran
- coarrays
- parallelism
- bugfix
commit_hash: 89058eb24376fe0d25ed586fab86b691672eb45d
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: Assign unique IDs to teams in caf_shmem for PR127738'
tldr: Fixes team ID collisions in libgfortran's caf_shmem by assigning unique IDs.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The caf_shmem implementation in libgfortran uses a supervisor process
  to manage coarray teams. This commit fixes a bug where team IDs were not unique,
  causing issues with coarray operations. The fix involves introducing a per-team
  ID counter in the supervisor and correctly deriving coarray IDs from the team's
  unique identifier.
primer_glossary:
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran). It provides
    support for Fortran language features, including coarray parallel programming.
- term: caf_shmem
  definition: A component within libgfortran that implements Fortran's Coarray API
    using shared memory for communication.
- term: Coarray API
  definition: A Fortran language feature for parallel programming, allowing processes
    (images) to directly access data in other processes (coarrays).
- term: FORM TEAM
  definition: A Fortran statement used to create a new team of images for coarray
    execution.
- term: image
  definition: In the context of Fortran coarrays, an image represents an independent
    process or thread participating in parallel execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/89058eb24376fe0d25ed586fab86b691672eb45d
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This change addresses PR127738 by ensuring that each team in libgfortran's caf_shmem module receives a unique identifier. Previously, team IDs were derived from team numbers and the count of FORM TEAM statements, leading to collisions and inconsistencies across different images of the same team. The fix introduces a supervisor-managed counter for team IDs, ensuring correct identification and enabling proper coarray ID derivation.
