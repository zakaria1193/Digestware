import { PROJECTS, absoluteUrl } from '../config/projects';

export async function GET() {
  const lines = [
    '# OS Pulse',
    '> Daily newspapers of open-source toolchain development.',
    '',
    'This domain hosts two sibling projects, each with its own llms.txt:',
    '',
    ...PROJECTS.map(p => `- [${p.name}](${absoluteUrl(p, `/${p.slug}/llms.txt`)})`),
    '',
  ];

  const body = lines.join('\n') + '\n';

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
