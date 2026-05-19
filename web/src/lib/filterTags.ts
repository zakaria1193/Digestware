// Shared helpers for computing the data the <FilterBar /> component
// needs: a ranked list of tags (with per-tag score/date arrays for live
// recounting) and the same list bucketed into UI categories.
//
// Both the project home page and the commit detail page feed this from
// their own source collections, so the filter bar shows a consistent
// set of chips with consistent counts no matter which view you're on.

export const CATEGORY_ORDER = [
  'architectures',
  'components',
  'topics',
  'news',
  'other',
] as const;

export type Category = typeof CATEGORY_ORDER[number];

export type RankedTag = {
  name: string;
  count: number;
  scores: number[];
  dates: number[];
};

type Entry = {
  data: {
    date: Date;
    tags?: string[] | null;
    impact_score?: number | null;
    sentiment_score?: number | null;
  };
};

// Aggregate impact scores per tag across one or more collections. The
// full score list (not just the count) is shipped to the client so each
// chip can recompute its live count as the impact slider moves.
export function rankTags(entries: Iterable<Entry>): RankedTag[] {
  const scoresByTag = new Map<string, number[]>();
  const datesByTag = new Map<string, number[]>();
  for (const entry of entries) {
    const score = entry.data.impact_score ?? entry.data.sentiment_score ?? -1;
    const ts = entry.data.date.getTime();
    for (const tag of entry.data.tags ?? []) {
      if (!scoresByTag.has(tag)) scoresByTag.set(tag, []);
      scoresByTag.get(tag)!.push(score);
      if (!datesByTag.has(tag)) datesByTag.set(tag, []);
      datesByTag.get(tag)!.push(ts);
    }
  }
  return [...scoresByTag.entries()]
    .map(([name, scores]) => ({
      name,
      count: scores.length,
      scores,
      dates: datesByTag.get(name) ?? [],
    }))
    .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
}

// Bucket ranked tags into the fixed CATEGORY_ORDER list. Anything
// without an assignment (or with an unknown one) falls into "other".
export function groupTags(
  rankedTags: RankedTag[],
  assignments: Record<string, string>,
): Array<{ category: Category; tags: RankedTag[] }> {
  const categoryFor = (tag: string): Category => {
    const raw = assignments[tag];
    return (CATEGORY_ORDER as readonly string[]).includes(raw) ? (raw as Category) : 'other';
  };
  const grouped: Array<{ category: Category; tags: RankedTag[] }> = [];
  for (const cat of CATEGORY_ORDER) {
    const bucket = rankedTags.filter(t => categoryFor(t.name) === cat);
    if (bucket.length > 0) grouped.push({ category: cat, tags: bucket });
  }
  return grouped;
}
