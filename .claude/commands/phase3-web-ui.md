# Phase 3 — The Web UI (Astro 6 + Tailwind 4)

Build the "Bento + Stream" frontend. The Markdown files written by the agent
(in `web/src/content/digests/`) drive all content via Astro Content Collections.

## Tasks

### 1. Astro project init
- Run `npm create astro@latest web -- --template minimal --typescript strict --no-install`
  inside the repo root (replace the existing stub `web/package.json`).
- Add integrations: `@astrojs/tailwind`, `@astrojs/rss`.
- Configure Tailwind 4 (no config file needed — use CSS-first config in `global.css`).

### 2. Content Collection (`web/src/content/config.ts`)
Define a `digests` collection that matches the `BentoDigest` frontmatter schema:
```ts
const digests = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subsystem: z.string(),
    impact_score: z.number().min(1).max(10),
    summary: z.string(),
    is_bento_worthy: z.boolean(),
    commit_sha: z.string(),
    source_url: z.string().url(),
    date: z.coerce.date(),
  }),
});
```

### 3. Homepage (`web/src/pages/index.astro`)
Two sections, no JavaScript required (static):

**Bento Grid** (top)
- Query all digests where `is_bento_worthy === true`, sorted by `impact_score` desc.
- Render as a CSS Grid with varying card sizes (high-impact = larger cell).
- Neo-brutalist style: thick black borders, off-white background, tight padding,
  monospace font for subsystem labels, bold impact score badge.

**Pulse Stream** (below)
- All digests sorted by date desc.
- Clean vertical list: date pill | subsystem tag | title | 1-line summary excerpt.
- Subtle left border accent color per subsystem family (gcc=blue, kernel=red, binutils=green).

### 4. Detail page (`web/src/pages/digests/[slug].astro`)
- Full summary text.
- Link to original commit (`source_url`).
- Subsystem breadcrumb.
- `<prev | next>` navigation between digests.

### 5. RSS feed (`web/src/pages/rss.xml.ts`)
- Standard Atom/RSS feed of all digests using `@astrojs/rss`.

### 6. Styling guidelines (Neo-brutalist + developer aesthetic)
- Background: `#f5f0e8` (warm off-white)
- Accent: `#000000` borders, 2–3 px solid
- Font: `JetBrains Mono` or `IBM Plex Mono` for code/labels; system-ui for prose
- Cards: no border-radius or very small (2px), hard box shadows (`4px 4px 0 #000`)
- High contrast; no gradients; flat colors only
- Responsive: single column on mobile, 3-col bento on desktop (md breakpoint)

### 7. Verify
- Run `npm run dev` inside `web/` and check:
  - Bento Grid renders with sample Markdown fixture.
  - Pulse Stream scrolls correctly.
  - Detail page navigates without 404.
  - RSS feed is valid XML.
