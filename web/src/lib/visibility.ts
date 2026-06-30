// Shared visibility rules for the PUBLIC site.
//
// Admin pages (/admin/**) deliberately bypass these so stubs and spam stay
// visible for ops triage — mirror the existing `is_stub` treatment: marked in
// admin, hidden from the public feed.

interface Filterable {
  is_stub?: boolean;
  tags?: string[] | null;
}

/** True when the entry is spam (tagged `spam` by the digest agent). */
export function isSpam(data: Filterable): boolean {
  return (data.tags ?? []).includes('spam');
}

/**
 * True when an entry should appear on the public site. Stubs are agent-side
 * placeholders for failed LLM batches; spam is unsolicited commercial noise.
 * Neither belongs in the public feed, detail pages, prev/next, or RSS.
 */
export function isPublic(data: Filterable): boolean {
  return !data.is_stub && !isSpam(data);
}
