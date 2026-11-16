import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { PROJECTS, getProject, absoluteUrl } from '../../config/projects';
import { isPublic } from '../../lib/visibility';

export async function getStaticPaths() {
  return PROJECTS.map(p => ({ params: { project: p.slug }, props: { projectSlug: p.slug } }));
}

function xmlEscape(value: string): string {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function urlEntry(loc: string, lastmod?: Date): string {
  const lastmodTag = lastmod ? `\n    <lastmod>${lastmod.toISOString()}</lastmod>` : '';
  return `  <url>\n    <loc>${xmlEscape(loc)}</loc>${lastmodTag}\n  </url>`;
}

export async function GET(context: APIContext) {
  const { projectSlug } = context.props as { projectSlug: string };
  const project = getProject(projectSlug)!;

  const [discussions, landings, lessons] = await Promise.all([
    getCollection('discussions', ({ data }) => data.project === projectSlug && isPublic(data)),
    getCollection('landings', ({ data }) => data.project === projectSlug && isPublic(data)),
    getCollection('lessons', ({ data }) => data.project === projectSlug && isPublic(data)),
  ]);

  const entries: string[] = [
    urlEntry(absoluteUrl(project, `/${projectSlug}/`)),
    urlEntry(absoluteUrl(project, `/${projectSlug}/mcp`)),
    ...discussions.map(e => urlEntry(absoluteUrl(project, `/${projectSlug}/discussions/${e.id}`), e.data.date)),
    ...landings.map(e => urlEntry(absoluteUrl(project, `/${projectSlug}/landings/${e.id}`), e.data.date)),
    ...lessons.map(e => urlEntry(absoluteUrl(project, `/${projectSlug}/lessons/${e.id}`), e.data.date)),
  ];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${entries.join('\n')}\n</urlset>\n`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
}
