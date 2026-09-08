import { defineCollection, z } from 'astro:content';

const seriesPart = z.object({
  title: z.string(),
  url: z.string(),
});

const exchange = z.object({
  author: z.string(),
  role: z.string().nullable().optional(),
  position: z.string(),
  quote: z.string().nullable().optional(),
});

const glossaryEntry = z.object({
  term: z.string(),
  definition: z.string(),
});

const discussions = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    patch_id: z.string().nullable().optional(),
    discussion_id: z.string().nullable().optional(),
    source_type: z.string(),
    title: z.string(),
    headline: z.string(),
    tldr: z.string(),
    proposer: z.string().nullable().optional(),
    consensus: z.string().nullable().optional(),
    outcome: z.string().nullable().optional(),
    impact_score: z.number().nullable().optional(),
    sentiment_score: z.number().nullable().optional(),
    technical_tradeoffs: z.array(z.string()).optional(),
    exchanges: z.array(exchange).optional(),
    primer_expert: z.string().nullable().optional(),
    primer_glossary: z.array(glossaryEntry).optional(),
    series_id: z.string().nullable().optional(),
    series_role: z.string().nullable().optional(),
    series_parts: z.array(seriesPart).optional(),
    tags: z.array(z.string()).optional(),
    url: z.string().url(),
    bugzilla_url: z.string().url().nullable().optional(),
    date: z.coerce.date(),
    is_stub: z.boolean().optional().default(false),
    stub_reason: z.string().optional().default(""),
  }),
});

const landings = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    patch_id: z.string().nullable().optional(),
    commit_hash: z.string().nullable().optional(),
    source_type: z.string(),
    headline: z.string(),
    tldr: z.string(),
    author: z.string().nullable().optional(),
    impact_score: z.number().nullable().optional(),
    outcome: z.string().nullable().optional(),
    performance_win: z.boolean().nullable().optional(),
    breaking_change: z.boolean().nullable().optional(),
    primer_expert: z.string().nullable().optional(),
    primer_glossary: z.array(glossaryEntry).optional(),
    series_id: z.string().nullable().optional(),
    series_parts: z.array(seriesPart).optional(),
    tags: z.array(z.string()).optional(),
    discussion_id_link: z.string().nullable().optional(),
    bugzilla_pr: z.string().nullable().optional(),
    url: z.string().url(),
    date: z.coerce.date(),
    is_stub: z.boolean().optional().default(false),
    stub_reason: z.string().optional().default(""),
  }),
});

// A lesson is the week's in-depth piece: one commit that merged, explained
// against the project's real source tree. Unlike discussions and landings it
// carries an article structure (sections become the Markdown body) plus the
// evidence for its claims (`code_tour` — files the agent actually opened).
//
// `date` is the END of the week covered, not the commit's own date — a weekly
// piece should sort with its week, and `commit_date` carries the real landing
// date for display.
const lessonSection = z.object({
  heading: z.string(),
  body: z.string(),
});

const codeRef = z.object({
  path: z.string(),
  symbol: z.string().nullable().optional(),
  lines: z.string().nullable().optional(),
  why: z.string(),
});

const furtherReading = z.object({
  title: z.string(),
  url: z.string(),
});

const lessons = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    patch_id: z.string().nullable().optional(),
    lesson_id: z.string(),
    commit_hash: z.string(),
    source_type: z.string(),
    headline: z.string(),
    hook: z.string(),
    tldr: z.string(),
    concept: z.string(),
    prerequisites: z.array(z.string()).optional().default([]),
    code_tour: z.array(codeRef).optional().default([]),
    takeaways: z.array(z.string()).optional().default([]),
    further_reading: z.array(furtherReading).optional().default([]),
    primer_expert: z.string().nullable().optional(),
    primer_glossary: z.array(glossaryEntry).optional(),
    tags: z.array(z.string()).optional(),
    landing_slug: z.string().nullable().optional(),
    url: z.string().url(),
    week_start: z.coerce.date(),
    week_end: z.coerce.date(),
    commit_date: z.coerce.date(),
    date: z.coerce.date(),
    is_stub: z.boolean().optional().default(false),
    stub_reason: z.string().optional().default(""),
  }),
});

export const collections = { discussions, landings, lessons };
