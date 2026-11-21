// Registry of projects, all served under `/<slug>/` subpaths from a single
// shared production origin (`SITE_ORIGIN`). The `slug` is the canonical
// identifier that matches the `project` frontmatter field in
// web/src/content/{discussions,landings,lessons}/*.md — content is filtered
// strictly by this slug, never merged across projects.

export const SITE_ORIGIN = 'https://digestware.pages.dev';

export interface ProjectDef {
  slug: string;        // matches frontmatter `project`
  name: string;        // masthead wordmark (e.g. "GCC Digest")
  short: string;       // compact label for tabs (e.g. "GCC")
  tagline: string;     // masthead tagline under the wordmark
  footerBlurb: string; // footer "Compiled daily · …" subtext
  description: string; // meta description / RSS description
}

export const PROJECTS: ProjectDef[] = [
  {
    slug: 'gcc',
    name: 'GCC Newspaper',
    short: 'GCC',
    tagline: '— A Daily Record of the GNU Compiler Collection —',
    footerBlurb: 'Compiled daily · GCC mailing list & gcc-mirror commits',
    description: 'Daily newspaper of GCC mailing-list proposals and landed commits.',
  },
  {
    slug: 'binutils',
    name: 'binutils Newspaper',
    short: 'binutils',
    tagline: '— A Daily Record of the GNU Binary Utilities —',
    footerBlurb: 'Compiled daily · binutils mailing list & binutils-cvs commits',
    description: 'Daily newspaper of binutils mailing-list proposals and landed commits.',
  },
];

// gcc is the canonical default project (e.g. root path redirect).
export const DEFAULT_PROJECT = 'gcc';

export function getProject(slug: string): ProjectDef | undefined {
  return PROJECTS.find(p => p.slug === slug);
}

// Return the `/<slug>/` subpath URL a tab should point at for a target project.
export function projectUrl(target: ProjectDef): string {
  return `/${target.slug}/`;
}

// Build a production absolute URL on the shared origin (`SITE_ORIGIN`).
// Used for canonical links, OG/Twitter tags, JSON-LD, sitemaps and llms.txt.
export function absoluteUrl(_project: ProjectDef, path: string): string {
  const normalized = path.startsWith('/') ? path : `/${path}`;
  return `${SITE_ORIGIN}${normalized}`;
}
