---
project: binutils
subsystem: binutils/libiberty
patch_id: null
tags:
- libiberty
- command-line
- porting
commit_hash: dcca095929a12ac590c62ff3ea680154b7f44705
source_type: public_inbox
author: Richard Earnshaw <rearnsha@sourceware.org>
headline: Binutils ports expandargstr from GCC's libiberty
tldr: Binutils now includes the `expandargstr` function from GCC's libiberty to handle
  response files prefixed with '@' for argument expansion.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libiberty` library provides generic support routines used by GNU
  tools like GCC and Binutils. The `expandargstr` function, now integrated into Binutils,
  is crucial for handling response files specified via the '@file' convention. This
  feature is particularly relevant in command-line parsing, where it directly impacts
  how arguments are interpreted, particularly in scenarios involving complex or lengthy
  command lines that are redirected from a file. Its move into Binutils ensures consistent
  behavior for projects that share `libiberty`.
primer_general: When you run a command on your computer, you usually type arguments
  directly after the command name. For example, `gcc -o myprogram myprogram.c`. Sometimes,
  the list of arguments can get very long, making the command line unwieldy. To solve
  this, many tools support 'response files,' where you put all the arguments into
  a separate file and then tell the command to read its arguments from there. This
  is often indicated by a special character, like `@`, followed by the filename (e.g.,
  `gcc @arguments.txt`). This commit brings a function called `expandargstr` into
  Binutils. This function is responsible for opening and interpreting these response
  files when an argument starts with `@`, effectively substituting the filename with
  the arguments contained within it. This helps keep command lines manageable and
  consistent across different parts of the Binutils toolchain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260615155855.09CE64B92097@sourceware.org
date: '2026-06-15'
is_stub: false
---

The `expandargstr` function has been ported from GCC's libiberty to Binutils. This function expands command-line arguments that begin with an '@' symbol, treating the subsequent string as a response file. It processes the file's contents and returns a shell-quoted string, ensuring consistent argument handling across the toolchain.
