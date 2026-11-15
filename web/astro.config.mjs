import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
  output: 'static',
  // Astro 7 defaults compressHTML to 'jsx' output, which changes whitespace
  // handling; keep the Astro 5/6 behaviour so the built HTML doesn't change.
  compressHTML: true,
});
