---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- optimization
- C++17
- ABI
commit_hash: c30bf3aee78bbe9bd557c7bcd5d2d5533f6a216e
source_type: github
author: Jonathan Wakely
headline: 'Libstdc++: Replace uses of EBO with [[no_unique_address]]'
tldr: The libstdc++ now uses the `[[no_unique_address]]` attribute instead of empty
  base optimization (EBO) to reduce the size of class layouts.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit replaces EBO with `[[no_unique_address]]` in `std::tuple`
  and `_Sp_counted_deleter` within `<bits/shared_ptr_base.h>`. EBO was previously
  used to optimize the layout of classes containing empty base classes. `[[no_unique_address]]`
  provides a more direct way to achieve the same goal. This change simplifies the
  code by removing workarounds for older compilers. The use of the attribute is now
  unconditional for the unstable ABI. Toolchain devs should note the changes to `_Sp_ebo_helper`
  and `_Head_base`.
primer_general: In C++, Empty Base Optimization (EBO) is a compiler optimization technique
  that allows empty base classes to occupy zero space in a derived class. `[[no_unique_address]]`
  is a C++17 attribute that provides a standard way to achieve the same effect, allowing
  empty members to be stored in the same memory location. This commit updates the
  standard library to use this attribute, potentially leading to smaller and more
  efficient data structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c30bf3aee78bbe9bd557c7bcd5d2d5533f6a216e
date: '2026-05-05'
---

The libstdc++ now uses the `[[no_unique_address]]` attribute instead of empty base optimization (EBO) in `<tuple>` and `<bits/shared_ptr_base.h>`.  This modernizes the code and simplifies the implementation on compilers that support the attribute, which includes Clang (since v9) and GCC itself.  This change reduces the size of class layouts by allowing empty base classes to be stored in the same memory location as other members.
