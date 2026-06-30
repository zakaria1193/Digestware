import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { PROJECTS, getProject } from '../../config/projects';
import { isPublic } from '../../lib/visibility';

export async function getStaticPaths() {
  return PROJECTS.map(p => ({ params: { project: p.slug }, props: { projectSlug: p.slug } }));
}

export async function GET(context: APIContext) {
  const { projectSlug } = context.props as { projectSlug: string };
  const project = getProject(projectSlug)!;

  const [discussions, landings] = await Promise.all([
    getCollection('discussions', ({ data }) => data.project === projectSlug && isPublic(data)),
    getCollection('landings', ({ data }) => data.project === projectSlug && isPublic(data)),
  ]);

  const discussionItems = discussions.map(e => ({
    title: e.data.headline,
    description: e.data.tldr,
    link: `/${projectSlug}/discussions/${e.id}`,
    pubDate: e.data.date,
  }));

  const landingItems = landings.map(e => ({
    title: e.data.headline,
    description: e.data.tldr,
    link: `/${projectSlug}/landings/${e.id}`,
    pubDate: e.data.date,
  }));

  const items = [...discussionItems, ...landingItems].sort(
    (a, b) => b.pubDate.getTime() - a.pubDate.getTime()
  );

  return rss({
    title: project.name,
    description: project.description,
    site: context.site ?? `https://${project.hostname}`,
    items,
    customData: '<language>en-us</language>',
  });
}
