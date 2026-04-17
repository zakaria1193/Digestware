# Phase 3 — The Web UI (Astro 6 + Tailwind 4)

Build the "Bento + Commit Stream" frontend. Two Astro Content Collections
(`landings/` and `discussions/`) drive all content — no database, no API.

## Content Collections (`web/src/content/config.ts`)

Two collections, matching the bimodal agent output:

```ts
// landings — merged commits (LandingDigest)
const landings = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    headline: z.string(),
    tldr: z.string(),
    why_it_matters: z.string().optional(),
    impact_score: z.number().optional(),
    impact_rationale: z.string().optional(),
    outcome: z.string().optional(),
    tags: z.array(z.string()).optional(),
    series_id: z.string().nullable().optional(),
    series_parts: z.array(z.object({ title: z.string(), url: z.string() })).optional(),
    author: z.string().optional(),
    url: z.string().url(),
    date: z.coerce.date(),
    // … remaining fields in config.ts
  }),
});

// discussions — proposals / mailing-list threads (DiscussionDigest)
const discussions = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    headline: z.string(),
    tldr: z.string(),
    stakes: z.string().optional(),
    outcome: z.string().optional(),
    sentiment_score: z.number().optional(),
    sentiment_rationale: z.string().optional(),
    technical_tradeoffs: z.array(z.string()).optional(),
    tags: z.array(z.string()).optional(),
    series_id: z.string().nullable().optional(),
    series_role: z.string().nullable().optional(),
    series_parts: z.array(z.object({ title: z.string(), url: z.string() })).optional(),
    url: z.string().url(),
    date: z.coerce.date(),
    // … remaining fields in config.ts
  }),
});
```

"Bento worthy" = `impact_score >= 7` (no `is_bento_worthy` field exists).

## Page Layout (`web/src/pages/index.astro`)

Two-column layout on desktop, stacked on mobile:

```
┌────────────────────────────────┬──────────────┐
│  Bento Grid (discussions)      │  Commit      │
│  — grouped by subsystem        │  Stream      │
│  — clustered by shared tags    │  (landings)  │
│                                │              │
└────────────────────────────────┴──────────────┘
```

### Left: Bento Grid (discussions)

- Pull all `discussions` where `impact_score >= 7` OR `outcome` is
  `"committed"` / `"ready"`.
- **Group into sub-bentos by `subsystem`**. Each sub-bento has a labelled
  header (subsystem name in muted gold caps + thin hairline rule above).
- **Cluster related discussions**: within a sub-bento, discussions that share
  ≥ 1 tag AND whose `date` values are ≤ 7 days apart are collapsed into a
  single cluster card. The card shows the highest-impact headline, a count
  badge ("3 related"), and links to all items. Expandable client-side.
- Individual cards sized by `impact_score` (high score = larger CSS grid cell).
  Clustering overrides sizing — a cluster is always a standard card.
- Tags grouping is data-driven from the `tags` field; additional grouping
  strategies can be layered in later without layout changes.

### Right: Commit Stream (sidebar)

- All `landings` sorted by `date` desc.
- Dense newspaper-index list: date pill | subsystem tag (muted caps) |
  `headline` in serif | `tldr` in smaller sans-serif.
- No card borders — plain rows with a 1px hairline divider.
- Sticky sidebar on desktop (`position: sticky; top: 1rem`).
- Hidden/collapsed on mobile (accordion or "Show commits" toggle).

## Detail Pages

`web/src/pages/discussions/[slug].astro` and
`web/src/pages/landings/[slug].astro`:

- Full summary body.
- Frontmatter metadata block: subsystem breadcrumb, outcome badge, tags list,
  impact score (landings) or sentiment score (discussions).
- `technical_tradeoffs` rendered as a bullet list (discussions only).
- `series_parts` rendered as "Part of a series" expandable list.
- `<prev | next>` navigation within the same collection sorted by date.
- Link to original source (`url`).

## RSS Feed (`web/src/pages/rss.xml.ts`)

Combined feed: interleave discussions and landings sorted by `date` desc.
Use `@astrojs/rss`. Item title = `headline`, description = `tldr`.

## Styling: WSJ Newspaper

**Remove** all Neo-brutalist rules from the original spec.

| Token | Value |
|-------|-------|
| Background | `#ffffff` |
| Body font | `Georgia, 'Times New Roman', serif` |
| Display headlines | `font-size: 2rem–2.5rem; font-weight: 700; font-family: serif` |
| UI labels / metadata | `system-ui, -apple-system, 'Inter', sans-serif` |
| Section accent | `#b8860b` (muted gold) — subsystem labels, tag pills |
| Body text | `#111111` |
| Secondary text | `#555555` |
| Borders | `1px solid #dddddd` hairlines only |
| Card shadows | none, or `0 1px 3px rgba(0,0,0,0.06)` max |
| Border radius | `2px` — minimal rounding |
| Line height | `1.65` for prose, `1.3` for headlines |
| Max prose width | `680px` for detail pages |
| Responsive breakpoint | `md` (768px): single-col mobile → 3-col bento + sidebar desktop |

No gradients. No hard offset shadows. No thick borders. High contrast text only.

### Bento card anatomy (WSJ-style)
```
┌────────────────────────────────────┐
│ GCC / LTO           committed ●    │  ← subsystem label (gold) + outcome dot
│                                    │
│ Headline in large bold serif       │  ← headline
│                                    │
│ Tldr text in smaller sans-serif,   │  ← tldr (2 lines max, truncated)
│ one or two lines max.              │
│                                    │
│ tag1  tag2  tag3        Apr 17     │  ← tags (gold pills) + date
└────────────────────────────────────┘
  1px solid #ddd border, 2px radius
```

## Setup Tasks

### 1. Astro project init
```bash
npm create astro@latest web -- --template minimal --typescript strict --no-install
```
Add integrations: `@astrojs/tailwind`, `@astrojs/rss`.
Configure Tailwind 4 via CSS-first `global.css` (no tailwind.config file).

### 2. Fonts
Load via `<link>` in `<head>` — no build-time font bundling needed:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500&display=swap" rel="stylesheet">
```
Use `Playfair Display` for display headlines, `Inter` for UI/labels.

### 3. Verify
- `npm run dev` inside `web/`: Bento Grid renders with sample Markdown fixtures.
- Commit stream sidebar is sticky and shows landings.
- Sub-bento grouping by subsystem visible with at least 2 subsystems in fixtures.
- Cluster card appears when 2+ discussions share a tag within 7 days.
- Detail page navigates without 404; prev/next works.
- RSS feed is valid XML with `headline` as title and `tldr` as description.
- Mobile view: sidebar hidden, bento collapses to single column.
