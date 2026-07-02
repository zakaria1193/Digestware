---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- enums
- performance
- readability
discussion_id: b07af6ec-a74a-8c90-a2c7-38c03664b882@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 0/5] aarch64: Remove aarch64_field_kind indirection'
headline: 'Aarch64: Remove aarch64_field_kind indirection'
tldr: Removes the aarch64_field_kind enum and replaces it with direct use of aarch64_field
  structs, potentially improving readability and performance.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improved readability vs. potential loss of abstraction.
- Potential performance gains vs. possible increased code complexity in the future.
- Reduced code indirection vs. tighter coupling to `aarch64_field` structure.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Proposes removing the `aarch64_field_kind` enum, replacing its uses with
    `aarch64_field` structs for readability and potential performance gains. Retains
    some enum names as macros temporarily and asks for feedback on the approach.
  quote: This patch series remove the aarch64_field_kind enum, and replaces uses of
    the enum with direct use of aarch64_field structs instead. I think this improves
    readability overall, and might also be a marginal performance improvement.
primer_expert: This series touches the aarch64-specific parts of binutils, specifically
  the handling of `aarch64_field` structs. The `aarch64_field_kind` enum likely provides
  an abstraction layer over these fields. Removing this indirection could simplify
  the code and potentially improve performance, but it might also introduce tighter
  coupling or require more code changes in the future if the structure of `aarch64_field`
  changes.
primer_general: Binutils is a collection of tools used to manipulate binary files,
  such as executables and object code. AArch64 is the 64-bit ARM architecture.  This
  patch series modifies the way binutils handles specific fields within AArch64 binaries.  An
  enum is a data type that consists of a set of named integer constants, offering
  a way to represent a fixed, limited set of choices. A struct is structured data
  type. By removing the enum and operating directly on the struct, the code could
  become simpler and faster, although this might make the code harder to change later.
series_id: 'binutils:aarch64: remove aarch64_field_kind indirection'
series_role: cover
series_parts:
- title: 'aarch64: Remove aarch64_field_kind indirection'
  url: https://inbox.sourceware.org/binutils/01196ecb-956b-eb96-2ab2-e5de6fa143c5@e124511.cambridge.arm.com
  n: 1
  total: 5
url: https://inbox.sourceware.org/binutils/b07af6ec-a74a-8c90-a2c7-38c03664b882@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

This patch series removes the `aarch64_field_kind` enum in binutils, replacing it with direct uses of `aarch64_field` structs. The author believes this change improves code readability and may offer a marginal performance improvement.  As an interim measure, some of the `aarch64_field_kind` enum names are retained as macros that expand to the corresponding `aarch64_field` value. The author seeks feedback on this approach before fully inlining the remaining uses.
