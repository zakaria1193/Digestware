---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gpg
- release
- security
- metalink
- rfc3156
discussion_id: ac5c7bd3ee629107db92ebe4099e74fc9aa983f7.camel@posteo.net
source_type: public_inbox
title: A couple usability hurdles with GCC release signatures
headline: Usability issues with GCC release signatures
tldr: GCC release signatures are not PGP-standard, and use outdated crypto, impacting
  automated use and trust.
proposer: John Scott <jscott@posteo.net>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adopting ASCII-armored signatures increases file size but improves interoperability
  with metadata formats.
- Updating to modern cryptographic standards (key size, hash algorithm) enhances security
  but may require significant infrastructure changes and user key management updates.
exchanges:
- author: John Scott
  role: proposer
  position: Reports that GCC release signatures are binary PGP, not ASCII-armored
    as required by RFC 3156, hindering integration with formats like Metalink. Also
    notes the use of a 1024-bit DSA key and SHA-1 for signatures, which are insecure
    and distrusted.
  quote: 'The signature has file extension .sig and is served over HTTP with Content-Type:
    application/pgp-signature, but this doesn''t conform to the accepted convention
    for a detached OpenPGP signature. In RFC 3156 [1], which is still the authoritative
    specification for this media type [2], it states the detached signature must always
    be in US-ASCII "armored" text format, but this detached signature is ac…'
primer_expert: The GCC release signing process uses OpenPGP signatures. This discussion
  highlights issues with the format of the signature files and the cryptographic strength
  of the keys and algorithms used. The binary format prevents direct inclusion in
  XML-based metadata formats like Metalink, and the outdated cryptography (1024-bit
  DSA, SHA-1) undermines trust in the signatures.
primer_glossary:
- term: Metalink
  definition: An XML-based file format for distributing files, specifying checksums,
    origins, and PGP signatures to improve download reliability and security.
- term: RFC 3156
  definition: Defines the 'application/pgp-signature' media type for detached PGP
    signatures, requiring them to be in ASCII-armored format.
- term: ASCII-armored
  definition: A text-based encoding format for binary data, typically used for PGP
    signatures, making them easily transportable via email and text files.
- term: 1024-bit DSA key
  definition: A deprecated type of digital signature algorithm key, considered too
    small and insecure by modern standards.
- term: SHA-1
  definition: A cryptographic hash function that has known collision vulnerabilities,
    making it unsuitable for security-critical applications like digital signatures.
- term: OpenPGP
  definition: A standard for encrypting and signing data, commonly used for email
    and file security.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ac5c7bd3ee629107db92ebe4099e74fc9aa983f7.camel@posteo.net
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

John Scott reports two usability and security issues with GCC release signatures. The .sig files are binary PGP, not ASCII-armored as per RFC 3156, preventing their direct inclusion in formats like Metalink via XInclude. Additionally, the primary key used for signing is a 1024-bit DSA key from 2001, and signatures use SHA-1, both considered insecure and distrusted by modern software.
