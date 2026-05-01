---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- plugin
- enum
- reflection
- c
discussion_id: CAK3_KpMGe9WQ4iOEistwQKgNrcVaMp=RoE0WD-Dq=SBFpsu+mA@mail.gmail.com
source_type: public_inbox
title: Access to enum definition at run time
headline: Access to enum definition at run time
tldr: Yair Lenga seeks feedback on a GCC plugin that generates enum metadata at compile
  time for runtime access in C.
proposer: Yair Lenga <yair.lenga@gmail.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased compile time due to plugin execution.
- Potential for increased object file size due to injected metadata.
- Complexity of maintaining a GCC plugin.
- Alternative approaches exist, such as using C++26 reflection or post-compile DWARF
  analysis.
exchanges:
- author: Yair Lenga
  role: proposer
  position: Seeks feedback on a GCC plugin that enables runtime access to enum definitions
    by generating metadata at compile time.
  quote: 'Looking for any feedback about the

    1, Idea/concept.

    2. The implementation of the pugin (Github URL)

    3. Is there a path for making it an experimental/official GCC

    extension? (after cleanup, reviews, adding test cases/, etc.)'
- author: Richard Biener
  role: other
  position: Responded to the initial email but the content is not included in the
    provided data.
  quote: null
- author: Jakub Jelinek
  role: contributor
  position: Suggests that C++26 reflection features might eliminate the need for a
    plugin for this functionality.
  quote: BTW, in C++26 one doesn't need a plugin for such things, in a few line
- author: Yair Lenga
  role: proposer
  position: Clarifies that the focus is on the C compiler and asks if C programs can
    access enum metadata stored in structures/variables.
  quote: 'My focus is on the C compiler. Assuming the enum "metadata" is stored

    in a structure/variables that are readable by the program - can C

    programs access it ? Does it apply to "C" enums, or only to "C++" enum

    classes.'
- author: Jakub Jelinek
  role: contributor
  position: Explains how C enums can be accessed using reflection in C++26.
  quote: "Any kind of enum.\nIt is roughly\n#include <meta>\n\ntemplate <typename\
    \ E>\nconstexpr const char *\nenum_to_string (E v)\n{\n  template for (constexpr\
    \ auto e : std::define_static_array (enumera"
- author: David Malcolm
  role: contributor
  position: Points to a list of known GCC plugins.
  quote: null
primer_expert: This thread discusses a GCC plugin that uses compile-time reflection
  to generate metadata for C enums, enabling runtime access to enum names and values.  GCC
  plugins are loaded by the compiler at startup.  The plugin would inject data structures
  into the object file, mapping enum values to their names. Inspection of DWARF is
  an alternative approach for post-compile analysis.
primer_general: Enumerations (enums) in C allow programmers to define a set of named
  integer constants.  By default, the names of these constants are only available
  at compile time.  This proposal aims to provide a way to access the names of enum
  constants at runtime, which can be useful for debugging, serialization, and other
  tasks. The approach involves creating a GCC plugin, which is a way to extend the
  compiler's functionality with custom code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAK3_KpMGe9WQ4iOEistwQKgNrcVaMp=RoE0WD-Dq=SBFpsu+mA@mail.gmail.com
bugzilla_url: null
date: '2026-04-30'
---

Yair Lenga is seeking feedback on a GCC plugin that extracts enum definitions and generates C structures to support runtime lookup and enumeration. The current implementation relies on a Python tool to extract enum definitions from the DWARF section, but Lenga is experimenting with a GCC plugin to perform this generation at compile time. He is looking for feedback on the idea, the plugin implementation, and the possibility of making it an official GCC extension.
