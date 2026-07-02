---
project: gcc
subsystem: gcc/c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
- debug
commit_hash: 64627d4f8349af24f5a84c0936eb00256769b534
source_type: github
author: Marek Polacek
headline: C++ reflection avoids Internal Compiler Error with constructor parameters.
tldr: GCC fixes an Internal Compiler Error (ICE) that occurred when compiling C++
  reflection features with debug information for constructor parameters.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ICE was triggered in `write_reflection` when processing reflection
  information for constructor parameters under `-g` (debug info generation). The issue
  revolved around the `DECL_ARGUMENTS` of a constructor `DECL` being nulled out by
  `cgraph_node::release_body` during early compilation phases (e.g., in `finalize_compilation_unit
  -> analyze_functions`). This made `FUNCTION_FIRST_USER_PARM` crash, as it expected
  valid arguments. By switching to `DECL_PARM_INDEX` in `mangle.cc`, the code correctly
  retrieves parameter indexing without relying on the potentially deallocated `DECL_ARGUMENTS`
  str…
primer_general: Compilers translate human-readable code into machine instructions.
  When you add debug information (`-g` flag), the compiler includes extra details
  that allow debuggers to show you what's happening inside your program. This fix
  addresses a bug in the C++ part of GCC where it crashed (an "Internal Compiler Error"
  or ICE) when trying to generate debug information for a new C++ feature called "reflection,"
  specifically for the parameters of a constructor (a special function that sets up
  new objects). The crash happened because some internal information about function
  arguments was being removed too early, causing the part of the compiler generating
  debug info to try and access something that no longer existed. The fix changes how
  the compiler looks up this information, making it more robust and preventing the
  crash, so developers can use reflection features with debuggers without issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/64627d4f8349af24f5a84c0936eb00256769b534
date: '2026-06-09'
is_stub: false
---

This commit addresses an Internal Compiler Error (ICE) that arose when generating debug information (`-g`) for C++ reflection of constructor parameters. The previous code relied on `FUNCTION_FIRST_USER_PARM` which could encounter a null tree because `DECL_ARGUMENTS` was prematurely set to `NULL` during compilation. The fix involves using `DECL_PARM_INDEX` instead to determine the parameter index, ensuring that valid parameter information is always available during reflection, even after function bodies are optimized away.
