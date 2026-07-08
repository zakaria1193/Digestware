---
project: gcc
subsystem: gcc/editorconfig
patch_id: null
tags:
- editorconfig
- yaml
- style
- configuration
commit_hash: 8b00dc7bd29bc43ef9e85d46a372647b0a826b77
source_type: github
author: Richard Earnshaw
headline: Add editorconfig rules for YAML/YML files
tldr: Editorconfig now includes rules for .yaml and .yml files.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Adds entries for `*.yaml` and `*.yml` to the root `.editorconfig` file.
  This standardizes code style, such as indentation and spacing, for YAML configuration
  files used within the GCC project, ensuring consistency across developer environments.
primer_glossary:
- term: .editorconfig
  definition: A file format and set of conventions for automatically enforcing consistent
    coding styles for files in different directories or projects. It supports various
    properties like indentation style, line endings, and character sets.
- term: YAML
  definition: YAML Ain't Markup Language, a human-readable data serialization standard
    often used for configuration files and data exchange. It's known for its readability
    compared to formats like JSON or XML.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8b00dc7bd29bc43ef9e85d46a372647b0a826b77
date: '2026-06-24'
is_stub: true
stub_reason: low_score
---

This commit adds new rules to the `.editorconfig` file to format `.yaml` and `.yml` files. EditorConfig helps maintain consistent coding styles across different editors and IDEs by defining formatting rules such as indentation and whitespace. This change ensures that YAML files within the GCC project adhere to a defined style.
