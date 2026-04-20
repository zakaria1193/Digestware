import { defineCollection, z } from 'astro:content';

const seriesPart = z.object({
  title: z.string(),
  url: z.string(),
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
    stakes: z.string().optional(),
    proposer: z.string().optional(),
    consensus: z.string().optional(),
    outcome: z.string().optional(),
    sentiment_score: z.number().nullable().optional(),
    sentiment_rationale: z.string().optional(),
    technical_tradeoffs: z.array(z.string()).optional(),
    primer_expert: z.string().nullable().optional(),
    primer_general: z.string().nullable().optional(),
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
    why_it_matters: z.string().optional(),
    author: z.string().optional(),
    impact_score: z.number().optional(),
    impact_rationale: z.string().optional(),
    outcome: z.string().optional(),
    performance_win: z.boolean().optional(),
    breaking_change: z.boolean().optional(),
    primer_expert: z.string().nullable().optional(),
    primer_general: z.string().nullable().optional(),
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
