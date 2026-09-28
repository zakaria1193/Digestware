---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- operator new
- integer overflow
- alignment
- CVE
lesson_id: gcc:2026-W39
commit_hash: 59d235ffa5a69231eb42e5290d52dc8c90d28b7a
source_type: github
headline: 'The Allocation That Succeeds Too Well: Overflow Checking in Aligned operator
  new'
hook: Rounding a size up to the alignment is two lines of arithmetic. In libstdc++'s
  aligned operator new, those two lines could turn a SIZE_MAX request into a successful
  32-byte allocation.
tldr: libstdc++ now runs every size adjustment inside aligned operator new through
  __builtin_add_overflow, so a wrapped-around size fails instead of allocating.
concept: An allocator's size argument is attacker-reachable arithmetic. Any rounding,
  padding, or header adjustment performed before the call must be overflow-checked,
  or a huge request silently becomes a tiny successful allocation.
prerequisites:
- how operator new relates to malloc
- what alignment means for an allocation
- size_t is unsigned and wraps
- C preprocessor conditional compilation
- C++ exceptions and the nothrow overloads
code_tour:
- path: libstdc++-v3/libsupc++/new_opa.cc
  symbol: aligned_alloc
  lines: 81-92
  why: The C11 branch is now a real function with a comment naming its job — satisfying
    aligned_alloc's preconditions — plus the AIX and OS X alignment fix-ups moved
    down from operator new.
- path: libstdc++-v3/libsupc++/new_opa.cc
  symbol: aligned_alloc
  lines: 93-101
  why: 'The heart of the fix: __builtin_add_overflow guards the round-up, and only
    then does the mask and the call to ::aligned_alloc run.'
- path: libstdc++-v3/libsupc++/new_opa.cc
  symbol: aligned_alloc
  lines: 101-113
  why: The mingw branch checks overflow itself because Wine's _aligned_malloc does
    not, and documents why al + 2 * sizeof(void*) cannot itself overflow.
- path: libstdc++-v3/libsupc++/new_opa.cc
  symbol: aligned_alloc
  lines: 127-130
  why: The no-aligned-allocator fallback, which over-allocates via malloc to store
    the original pointer and therefore needs the same addition checked.
- path: libstdc++-v3/testsuite/18_support/new_aligned_wrap.cc
  symbol: check_aligned_new_overflow
  lines: 1-39
  why: A complete regression test asserting both std::bad_alloc from the throwing
    form and a null return from the nothrow form, with arguments chosen to straddle
    the round-up boundary.
takeaways:
- 'Any size arithmetic between your caller and libc is attacker-reachable: check it
  with __builtin_add_overflow, not a comment.'
- Unsigned wraparound turns a refusal into a success — a huge request becoming a tiny
  valid allocation is worse than a crash.
- Keep precondition-satisfying code in the same function as the call whose preconditions
  it satisfies, so one read can judge it correct.
- An overflow check is only sound if its own arithmetic cannot overflow; state the
  invariant that makes it so.
- A correct libc on your dev machine says nothing about the reimplementation your
  users ship against.
further_reading:
- title: gcc commit 59d235ffa5a69231eb42e5290d52dc8c90d28b7a
  url: https://github.com/gcc-mirror/gcc/commit/59d235ffa5a69231eb42e5290d52dc8c90d28b7a
primer_expert: '`new_opa.cc` in `libsupc++` is the over-aligned `operator new`, and
  it is a configure-driven `#if` chain over `_GLIBCXX_HAVE_POSIX_MEMALIGN` / `_GLIBCXX_HAVE_ALIGNED_ALLOC`
  / `_GLIBCXX_HAVE__ALIGNED_MALLOC` / `_GLIBCXX_HAVE_MEMALIGN` collapsed behind one
  `__gnu_cxx::aligned_alloc`. The non-obvious part is that the branches differ in
  how much arithmetic they do: only the C11 and `malloc` paths round size to a multiple
  of alignment, so the overflow was invisible on glibc targets. The mingw branch must
  also distrust Wine''s `msvcrt.dll` `_aligned_malloc`.'
primer_glossary:
- term: libsupc++
  definition: 'The C++ runtime support library inside libstdc++, holding the pieces
    the compiler emits calls to rather than the pieces users call by name: operator
    new and delete, the exception unwinding glue, RTTI, and types like std::bad_alloc.'
- term: std::align_val_t
  definition: A C++17 scoped enumeration type used solely to tag the alignment argument
    of the over-aligned operator new and operator delete overloads, so they do not
    collide with the plain size_t forms.
- term: __cpp_aligned_new
  definition: A feature-test macro the compiler predefines when aligned operator new
    is available in the current dialect, letting portable code compile out over-aligned
    allocation paths.
- term: posix_memalign
  definition: A POSIX aligned-allocation function that returns the pointer through
    an out-parameter. It requires the alignment be a power of two multiple of sizeof(void*)
    but places no multiple-of-alignment requirement on the size.
- term: C11 aligned_alloc
  definition: The standard C aligned allocator. Unlike posix_memalign it imposes a
    precondition that the requested size be an integral multiple of the alignment,
    which forces callers to round the size up before calling.
- term: _aligned_malloc
  definition: The Microsoft C runtime's aligned allocation function, taking size then
    alignment. Memory from it must be released with _aligned_free rather than free,
    and it performs its own internal padding.
- term: memalign
  definition: An older non-standard aligned allocation function found on some Unix
    systems; libstdc++ uses it as a fallback and assumes its result can be passed
    to free.
- term: __builtin_add_overflow
  definition: A GCC built-in that adds two integers in infinite precision, stores
    the truncated result through a pointer argument, and returns true if the mathematical
    result did not fit the destination type. It is the standard way to write portable
    checked arithmetic without relying on wraparound behaviour.
- term: '[[unlikely]]'
  definition: A C++20 attribute placed on a statement or branch to tell the optimiser
    that path is rarely taken, influencing block layout and branch prediction hints.
- term: _GLIBCXX_HAVE_ALIGNED_ALLOC
  definition: One of libstdc++'s configure-generated feature macros, defined when
    the build-time probe found the corresponding libc function. The family of these
    macros selects which aligned-allocation backend new_opa.cc compiles in.
landing_slug: 2026-09-23-libstdc-59d235ff
url: https://github.com/gcc-mirror/gcc/commit/59d235ffa5a69231eb42e5290d52dc8c90d28b7a
week_start: '2026-09-21'
week_end: '2026-09-27'
commit_date: '2026-09-23'
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

## Where aligned new lives, and why it is a portability layer

C++17 added over-aligned allocation: `operator new (std::size_t sz, std::align_val_t al)`. A type declared `alignas(64)` no longer has to be hand-placed by the programmer; the compiler emits a call to the aligned form of `operator new`, and the library is responsible for returning a pointer that is both large enough and suitably aligned. The freestanding half of that contract lives in libstdc++'s `libsupc++` directory — the runtime support library that also holds the exception machinery and `std::bad_alloc` itself.

The file that implements it is `libstdc++-v3/libsupc++/new_opa.cc`. `new_opa` is not one implementation; it is a chain of preprocessor alternatives, because "give me 64-byte-aligned memory" is spelled differently on every platform libstdc++ targets. The diff shows the shape of that chain directly: `_GLIBCXX_HAVE_POSIX_MEMALIGN`, then `#elif _GLIBCXX_HAVE_ALIGNED_ALLOC`, then `#elif _GLIBCXX_HAVE__ALIGNED_MALLOC`, then `#elif _GLIBCXX_HAVE_MEMALIGN`, and finally a hand-rolled fallback built on plain `malloc`.

Each of those macros is set by configure when it detects the corresponding libc function. So the code any particular user actually runs depends on which branch their target selected at build time — and, crucially, the branches do not do equal amounts of arithmetic. That asymmetry is the whole story of this commit.

The unifying device is a single internal entry point, `__gnu_cxx::aligned_alloc (std::size_t al, std::size_t sz)`. Whatever the platform, `operator new` calls that one name. Before this week, on one important branch, that name was not a function at all.

## The mechanism: preconditions, rounding, and unsigned wraparound

The interesting branch is `_GLIBCXX_HAVE_ALIGNED_ALLOC`, the C11 `aligned_alloc`. C11 does not simply say "allocate `sz` bytes with alignment `al`". As the new comment in the file puts it: "C11: the value of size shall be an integral multiple of alignment." That is a *precondition* on the caller. A request for 100 bytes at 64-byte alignment is not a valid C11 `aligned_alloc` call; the size has to be bumped to 128 first.

So libstdc++ rounds. The idiom is the standard power-of-two round-up:

```c
sz = (sz + align - 1) & ~(align - 1);
```

That line used to sit inside `operator new` itself, guarded by the same `#elif _GLIBCXX_HAVE_ALIGNED_ALLOC`, while the branch below it simply wrote `using ::aligned_alloc;` — a using-directive pulling the libc symbol straight into `__gnu_cxx`. The adjustment and the call were in different places.

Now look at the arithmetic as an attacker would. `sz` and `align` are both `std::size_t`, unsigned, so `sz + align - 1` does not trap and does not saturate: it wraps modulo 2^64. Feed in `sz == SIZE_MAX` and `align == 32` and the sum wraps to 30; masking with `~(align - 1)` yields 0. The library then asks libc for zero bytes at 32-byte alignment, gets a perfectly valid non-null pointer back, and hands it to a caller who believes it owns `SIZE_MAX` bytes. The commit message states the consequence plainly: "we return a non-null pointer but not of the requested size."

The fallback branch has the same shape for a different reason. When no aligned allocation function exists at all, libstdc++ over-allocates with `malloc` and aligns by hand — "We need extra bytes to store the original value returned by malloc" — which means adding `al` to `sz` before the `malloc` call. Same unsigned addition, same wraparound.

Note which branch is *not* affected: `posix_memalign` has no size-multiple precondition, so libstdc++ does no rounding there. The commit says so: "This doesn't affect most modern targets because they use the posix_memalign implementation, which doesn't do that rounding."

## The change: move the arithmetic next to the call, then check it

The fix, filed as CVE-2026-95619, does two things at once, and the ordering matters pedagogically. First it eliminates the using-directive. `using ::aligned_alloc;` becomes a real wrapper, headed by the comment "We have C11 aligned_alloc but we need to satisfy its preconditions." The platform fix-ups that had been stranded in `operator new` — including the AIX 7.2.0.0 and OS X 10.15 quirk where `aligned_alloc` "incorrectly has posix_memalign's requirement that alignment is a multiple of sizeof(void*)" — move down into that wrapper. Precondition-satisfying code now lives adjacent to the call whose preconditions it satisfies.

Second, the rounding becomes checked:

```c
  /* C11: the value of size shall be an integral multiple of alignment.  */
  if (__builtin_add_overflow(sz, al - 1, &sz)) [[unlikely]]
    return nullptr;
  sz &= ~(al - 1);
  return ::aligned_alloc(al, sz);
```

`__builtin_add_overflow` performs the addition in infinite precision, stores the truncated result through the pointer, and returns `true` if the true result did not fit. Here the destination is `sz` itself, so the success path is exactly the old code; the failure path returns `nullptr`, which is the contract `operator new` already understands. `[[unlikely]]` tells the optimiser which way to lay out the branch.

The `malloc` fallback gets the same treatment: `if (__builtin_add_overflow(sz, al, &sz)) [[unlikely]] return nullptr;` replaces the inline `malloc(sz + al)`, and the subsequent null check on `malloc_ptr` picks up an `[[unlikely]]` too.

The mingw branch is the subtle one. Windows' `_aligned_malloc` checks for overflow correctly — but, per the commit message, "the Wine version of that function does not and has the same overflow problem so we need to do our own checks before calling it." Since libstdc++ cannot know at compile time whether its `msvcrt.dll` is Microsoft's or Wine's, it checks unconditionally and conservatively:

```c
  std::size_t check;
  if (__builtin_add_overflow(sz, al + 2 * sizeof(void*), &check)) [[unlikely]]
    return nullptr;
  return _aligned_malloc(sz, al);
```

Two details reward attention. The result goes into a throwaway `check`, not into `sz` — this branch is validating a bound, not computing the size to pass on, because `_aligned_malloc` does its own padding internally. And the comment explains why the added term is itself safe: "We know al + 2 * sizeof(void*) won't overflow because has_single_bit(al) was already checked by the caller." An overflow check whose own arithmetic can overflow is not a check, so the author documents the invariant that makes it sound.

## What this means if you don't work on libsupc++

The behavioural change is narrow and easy to state. On targets that use C11 `aligned_alloc`, Windows `_aligned_malloc`, or the `malloc` fallback, an over-aligned allocation whose size cannot be legally rounded now fails: the throwing `operator new` raises `std::bad_alloc`, and the `std::nothrow` overload returns null. Previously such a request could succeed with an undersized block. On a glibc-class target using `posix_memalign`, nothing changes, because nothing was wrong.

The transferable lesson is about where a size becomes untrusted. Most programmers treat `operator new (n)` as a black box that either gives them `n` bytes or throws. That guarantee is only as strong as the arithmetic between the caller's `n` and libc's parameter. Every adjustment in that gap — align round-up, a header for bookkeeping, a `+ 1` for the zero-size case, an over-allocate-and-align dance — is an opportunity for an unsigned sum to wrap into a small, plausible, allocatable number. Audit your own allocators on exactly this axis: if you compute `size + something` before calling down, ask what happens when `size` is `SIZE_MAX`.

The second lesson is structural. The bug was reachable partly because the arithmetic lived in `operator new` while the call lived thirty lines away behind a using-directive, so no single function could be read and judged correct. Collapsing both into `__gnu_cxx::aligned_alloc` makes each platform branch independently auditable: one function, one set of preconditions, one overflow check. Wrappers that exist only to "satisfy preconditions" are worth their indirection precisely because they localise this kind of reasoning.

Third: a correct upstream implementation on the platform you develop on does not mean a correct implementation on the platform you ship to. `_aligned_malloc` checks overflow on Windows; the Wine reimplementation does not. Defensive duplication of a cheap check across an ABI boundary you do not control is the right trade.

## Seeing it yourself

The commit ships `libstdc++-v3/testsuite/18_support/new_aligned_wrap.cc`, a `{ dg-do run }` test that is short enough to read in full and instructive in how it is parameterised. `check_aligned_new_overflow(std::size_t size, std::size_t align)` casts the alignment to `std::align_val_t`, calls the throwing `::operator new(size, alignv)` inside a `try`, and asserts with `VERIFY(false)` that control never reaches the statement after the call. It then calls the `std::nothrow` overload and asserts `VERIFY(p == 0)`. Both halves of the contract, one helper.

The argument table is the interesting part, because it is chosen to straddle the round-up boundary rather than just to be large:

```c
  check_aligned_new_overflow(-9, 32);
  check_aligned_new_overflow(SIZE_MAX, 8);
  check_aligned_new_overflow(SIZE_MAX - 1025, 1024);
  check_aligned_new_overflow(SIZE_MAX - 1024, 1024);
  check_aligned_new_overflow(SIZE_MAX - 65536, 65536);
```

`-9` as a `std::size_t` is `SIZE_MAX - 8`; the neighbouring `SIZE_MAX - 1025` and `SIZE_MAX - 1024` pairs probe just either side of where `sz + al - 1` tips over for a 1024-byte alignment. That is how you test a boundary condition: pick the value before, the value at, and the value after.

The whole body is wrapped in `#if __cpp_aligned_new`, the feature-test macro the compiler defines when aligned `operator new` is available, so the test compiles to an empty function in dialects without it. And note line 7, `#pragma GCC diagnostic ignored "-Walloc-size-larger-than="` — the compiler will otherwise warn about these deliberately absurd requests, which is a small reminder that GCC already diagnoses statically visible versions of this mistake.
