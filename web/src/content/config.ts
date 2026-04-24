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
    sentiment_score: z.number().nullable().optional(),
    technical_tradeoffs: z.array(z.string()).optional(),
    exchanges: z.array(exchange).optional(),
    primer_expert: z.string().nullable().optional(),
    primer_general: z.string().nullable().optional(),
    primer_glossary: z.array(glossaryEntry).optional(),
    series_id: z.string().nullable().optional(),
    series_role: z.string().nullable().optional(),
    series_parts: z.array(seriesPart).optional(),
    tags: z.array(z.string()).optional(),
    url: z.string().url(),
    bugzilla_url: z.string().url().nullable().optional(),
    date: z.coerce.date(),
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
    primer_general: z.string().nullable().optional(),
    primer_glossary: z.array(glossaryEntry).optional(),
    series_id: z.string().nullable().optional(),
    series_parts: z.array(seriesPart).optional(),
    tags: z.array(z.string()).optional(),
    discussion_id_link: z.string().nullable().optional(),
    bugzilla_pr: z.string().nullable().optional(),
    url: z.string().url(),
    date: z.coerce.date(),
  }),
});

export const collections = { discussions, landings };
