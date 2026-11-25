---
project: binutils
subsystem: dlltool
patch_id: null
tags:
- binutils
- dlltool
- PE/COFF
- import library
discussion_id: SL2P216MB22716F490111C882AB5D17ECEF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH 2/3] dlltool: Add --short-implib [PR34527]'
headline: 'dlltool: Add --short-implib [PR34527]'
tldr: Add a --short-implib option to dlltool to generate compact PE/COFF import libraries.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new option and associated logic, increasing complexity.
- Ensures backward compatibility by keeping the default import library format unchanged.
exchanges: []
primer_expert: This patch adds support for generating PE/COFF short import libraries
  via a new --short-implib option in dlltool. This complements the BFD writer added
  in patch 1/3, allowing dlltool to leverage the new format. Short import libraries
  are more compact and can be processed by GNU ld, MSVC, and LLVM, addressing a gap
  in GNU toolchain's import library generation capabilities.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the standard file format
    for executables, object code, and DLLs in 32-bit and 64-bit Windows operating
    systems.
- term: dlltool
  definition: A GNU binutils utility that creates DLL import libraries, or extracts
    information from them.
- term: Import library
  definition: A library that contains information about functions and variables exported
    by a DLL. It allows programs to link against DLLs without explicitly calling loading
    functions.
series_id: 'binutils:dlltool: add --short-implib [pr34527]'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB22716F490111C882AB5D17ECEF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch introduces the --short-implib option to dlltool, enabling the generation of more compact PE/COFF import libraries. This new format uses shorter import members, which are compatible with existing tools like GNU ld, MSVC, and LLVM. This feature addresses a long-standing need for more efficient import library creation.
