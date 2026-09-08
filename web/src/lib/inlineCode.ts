// Render the small subset of Markdown that appears in *frontmatter* strings.
//
// Article bodies go through Astro's Markdown pipeline; frontmatter fields
// (primers, glossary definitions, code-tour blurbs) do not, but the agents are
// instructed to write identifiers as `inline code` there too — CLAUDE.md's
// article conventions require function, macro and flag names to survive
// verbatim, and a bare `-fipa-sra` in prose reads as a typo without them.
//
// HTML is escaped first, so the only markup that reaches the page is the
// <code> element this function emits. Callers pass the result to `set:html`.

export function inlineCode(text: string | null | undefined): string {
  if (!text) return '';
  const escaped = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
  return escaped
    .replace(/``([^`\n]+)``/g, '<code>$1</code>')
    .replace(/`([^`\n]+)`/g, '<code>$1</code>');
}
