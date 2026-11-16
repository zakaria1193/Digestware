import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { PROJECTS, getProject, absoluteUrl } from '../../config/projects';
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
    headline: e.data.headline,
    summary: e.data.tldr,
    url: absoluteUrl(project, `/${projectSlug}/discussions/${e.id}`),
    date: e.data.date,
  }));
  const landingItems = landings.map(e => ({
    headline: e.data.headline,
    summary: e.data.tldr,
    url: absoluteUrl(project, `/${projectSlug}/landings/${e.id}`),
    date: e.data.date,
  }));
  const lessonItems = lessons.map(e => ({
    headline: e.data.headline,
    summary: e.data.hook,
    url: absoluteUrl(project, `/${projectSlug}/lessons/${e.id}`),
    date: e.data.date,
  }));

  const recent = [...discussionItems, ...landingItems, ...lessonItems]
    .sort((a, b) => b.date.getTime() - a.date.getTime())
    .slice(0, 30);

  const lines = [
    `# ${project.name}`,
    `> ${project.description}`,
    '',
    `${project.name} covers daily mailing-list proposals and landed commits for this project. Articles summarise upstream sources that readers should check for the full, authoritative record.`,
    '',
    '## Sections',
    `- [Home](${absoluteUrl(project, `/${projectSlug}/`)})`,
    `- [RSS feed](${absoluteUrl(project, `/${projectSlug}/rss.xml`)})`,
    `- [MCP](${absoluteUrl(project, `/${projectSlug}/mcp`)})`,
  ];

  if (recent.length > 0) {
    lines.push('', '## Recent articles');
    for (const item of recent) {
      lines.push(`- [${item.headline}](${item.url}): ${item.summary}`);
    }
  }

  const body = lines.join('\n') + '\n';

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
