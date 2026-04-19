import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const [discussions, landings] = await Promise.all([
    getCollection('discussions'),
    getCollection('landings'),
  ]);

  const discussionItems = discussions.map(e => ({
    title: e.data.headline,
    description: e.data.tldr,
    link: `/discussions/${e.id}`,
    pubDate: e.data.date,
  }));

  const landingItems = landings.map(e => ({
    title: e.data.headline,
    description: e.data.tldr,
    link: `/landings/${e.id}`,
    pubDate: e.data.date,
  }));

  const items = [...discussionItems, ...landingItems].sort(
    (a, b) => b.pubDate.getTime() - a.pubDate.getTime()
  );

  return rss({
    title: 'OS Pulse',
    description: 'Daily digest of open-source OS-level changes — GCC, binutils, glibc, kernel',
    site: context.site ?? 'https://os-pulse.dev',
    items,
    customData: '<language>en-us</language>',
  });
}
