import { defineCollection, z } from 'astro:content';

const discussions = defineCollection({
  type: 'content',
  schema: z.object({
    project: z.string(),
    subsystem: z.string(),
    patch_id: z.string().nullable().optional(),
    discussion_id: z.string().nullable().optional(),
    source_type: z.string(),
    title: z.string(),
    proposer: z.string().optional(),
    consensus: z.string().optional(),
    sentiment_score: z.number().optional(),
    technical_tradeoffs: z.array(z.string()).optional(),
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
    author: z.string().optional(),
    impact_score: z.number().optional(),
    performance_win: z.boolean().optional(),
    breaking_change: z.boolean().optional(),
    discussion_id_link: z.string().nullable().optional(),
    bugzilla_pr: z.string().nullable().optional(),
    url: z.string().url(),
    date: z.coerce.date(),
  }),
});

const digests = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subsystem: z.string(),
    impact_score: z.number(),
    summary: z.string(),
    is_bento_worthy: z.boolean(),
    commit_sha: z.string(),
    source_url: z.string().url(),
    date: z.coerce.date(),
  }),
});

export const collections = { discussions, landings, digests };
