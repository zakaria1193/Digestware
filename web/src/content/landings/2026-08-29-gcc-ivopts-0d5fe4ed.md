---
project: gcc
subsystem: gcc/ivopts
patch_id: null
tags:
- optimization
- gcc
- loops
commit_hash: 0d5fe4ed0540cca156754a905387c3420465b210
source_type: github
author: Jovan Dmitrovic
headline: 'ivopts: Refine register pressure estimate for loop invariants'
tldr: Register pressure estimation in loop invariant optimization is adjusted for
  more accurate spilling costs.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `ivopts_estimate_reg_pressure` function in `tree-ssa-loop-ivopts.cc`
  previously set the register pressure cost for spilling invariants to exactly half
  that of spilling IV candidates. This commit corrects this by recognizing that invariants
  are loaded once, whereas IVs are loaded and stored each iteration. The estimate
  is adjusted to reflect this difference, aiming for more accurate cost-based decisions
  in the loop invariant optimization pass, particularly regarding register allocation
  trade-offs.
primer_glossary:
- term: ivopts
  definition: The GCC optimization pass focused on loop-invariant code motion and
    induction variable analysis and optimization.
- term: loop invariant
  definition: An expression within a loop whose value does not change from one iteration
    to the next. Compilers can often hoist these expressions out of the loop to improve
    performance.
- term: induction variable
  definition: A variable within a loop whose value is modified by a constant or other
    simple arithmetic progression in each iteration, typically used for loop control
    or array indexing.
- term: register pressure
  definition: A measure of how many registers are simultaneously needed by the program.
    High register pressure can lead to more spills (storing register values to memory),
    impacting performance.
- term: spilling
  definition: The process by which a compiler moves values from registers to memory
    when there are not enough registers available to hold all the live values.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:ivopts: adjust reg pressure estimate for spilling invariants compared
  to iv cands'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0d5fe4ed0540cca156754a905387c3420465b210
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

The `ivopts` pass has adjusted its register pressure estimation to more accurately reflect the cost of spilling loop invariants versus induction variables. Previously, it assumed spilling loop invariants was half the cost of spilling induction variables. This change corrects the calculation to account for the fact that invariants only need to be loaded once, while induction variables must be loaded and stored per loop iteration.
