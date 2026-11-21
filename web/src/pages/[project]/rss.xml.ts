import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { PROJECTS, SITE_ORIGIN, getProject } from '../../config/projects';
import { isPublic } from '../../lib/visibility';

export async function getStaticPaths() {
  return PROJECTS.map(p => ({ params: { project: p.slug }, props: { projectSlug: p.slug } }));
}

export async function GET(context: APIContext) {
  const { projectSlug } = context.props as { projectSlug: string };
  const project = getProject(projectSlug)!;

  const [discussions, landings, lessons] = await Promise.all([
    getCollection('discussions', ({ data }) => data.project === projectSlug && isPublic(data)),
    getCollection('landings', ({ data }) => data.project === projectSlug && isPublic(data)),
    getCollection('lessons', ({ data }) => data.project === projectSlug && isPublic(data)),
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

  // The lesson leads with its hook rather than its tldr: in a reader's feed
  // the hook is what distinguishes it from the commit digest beside it.
  const lessonItems = lessons.map(e => ({
    title: `Lesson: ${e.data.headline}`,
    description: e.data.hook,
    link: `/${projectSlug}/lessons/${e.id}`,
    pubDate: e.data.date,
  }));

  const items = [...discussionItems, ...landingItems, ...lessonItems].sort(
    (a, b) => b.pubDate.getTime() - a.pubDate.getTime()
  );

  return rss({
    title: project.name,
    description: project.description,
    site: context.site ?? SITE_ORIGIN,
    items,
    customData: '<language>en-us</language>',
  });
}
