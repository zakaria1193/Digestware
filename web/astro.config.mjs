import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

const base = process.env.BASE_URL ?? '';

export default defineConfig({
  base,
  vite: {
    plugins: [tailwindcss()],
  },
  output: 'static',
});
