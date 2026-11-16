// Registry of projects (one per hostname). The `slug` is the canonical
// identifier that matches the `project` frontmatter field in
// web/src/content/{discussions,landings}/*.md — content is filtered
// strictly by this slug, never merged across projects.
//
// `hostname` is the production domain this project is served from.
// When PUBLIC_USE_HOSTNAMES=true, cross-project tab links use the
// hostname (absolute URL). Otherwise they use `/<slug>/` subpaths so
// local dev and a single-origin preview work out of the box.

export interface ProjectDef {
  slug: string;        // matches frontmatter `project`
  name: string;        // masthead wordmark (e.g. "GCC Digest")
  short: string;       // compact label for tabs (e.g. "GCC")
  hostname: string;    // production hostname (no scheme)
  tagline: string;     // masthead tagline under the wordmark
  footerBlurb: string; // footer "Compiled daily · …" subtext
  description: string; // meta description / RSS description
}

export const PROJECTS: ProjectDef[] = [
  {
    slug: 'gcc',
    name: 'GCC Newspaper',
    short: 'GCC',
    hostname: 'gccdigest.dev',
    tagline: '— A Daily Record of the GNU Compiler Collection —',
    footerBlurb: 'Compiled daily · GCC mailing list & gcc-mirror commits',
    description: 'Daily newspaper of GCC mailing-list proposals and landed commits.',
  },
  {
    slug: 'binutils',
    name: 'binutils Newspaper',
    short: 'binutils',
    hostname: 'binutilsdigest.dev',
    tagline: '— A Daily Record of the GNU Binary Utilities —',
    footerBlurb: 'Compiled daily · binutils mailing list & binutils-cvs commits',
    description: 'Daily newspaper of binutils mailing-list proposals and landed commits.',
  },
];

// gcc is the canonical default when no hostname is resolved (e.g. root
// path fallback).
export const DEFAULT_PROJECT = 'gcc';

export function getProject(slug: string): ProjectDef | undefined {
  return PROJECTS.find(p => p.slug === slug);
}

// Return the URL a tab should point at for a given target project.
// - In hostname mode, links are absolute (`https://<hostname>/`).
// - In subpath mode, links are `/<slug>/`.
export function projectUrl(target: ProjectDef): string {
  const useHostnames = import.meta.env.PUBLIC_USE_HOSTNAMES === 'true';
  if (useHostnames) return `https://${target.hostname}/`;
  return `/${target.slug}/`;
}

// Build a production absolute URL for a path within a project, always on
// that project's own hostname. Used for canonical links, OG/Twitter tags,
// JSON-LD, sitemaps and llms.txt — all of which must stay correct
// regardless of PUBLIC_USE_HOSTNAMES, since one build serves two hosts.
export function absoluteUrl(project: ProjectDef, path: string): string {
  const normalized = path.startsWith('/') ? path : `/${path}`;
  return `https://${project.hostname}${normalized}`;
}
