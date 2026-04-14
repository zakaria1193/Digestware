# Phase 4 — Newsletter & GitHub Actions Automation

Wire the agent to run on a schedule, commit its output, and email the daily
Bento highlights via Resend + React Email.

## Tasks

### 1. GitHub Actions workflow (`.github/workflows/daily-digest.yml`)
```yaml
name: Daily Digest
on:
  schedule:
    - cron: '0 6,18 * * *'   # runs every 12 hours at 06:00 and 18:00 UTC
  workflow_dispatch:           # manual trigger for testing
```

Steps:
1. Checkout repo.
2. Set up Python 3.12.
3. Install agent deps: `pip install -r agents/requirements.txt`.
4. Run agent: `python -m agents.main --since-hours 12`.
5. If new Markdown files were created, commit and push them:
   ```bash
   git config user.name  "OS Pulse Bot"
   git config user.email "bot@ospulse.dev"
   git add web/src/content/digests/
   git diff --cached --quiet || git commit -m "digest: $(date -u +%Y-%m-%d) batch"
   git push
   ```
6. Run the newsletter sender (see step 3 below).

Secrets needed (add in GitHub repo settings):
- `OPENROUTER_API_KEY`
- `RESEND_API_KEY`

### 2. React Email template (`agents/email/digest_email.tsx`)
- Use `@react-email/components`.
- Layout mirrors the web Bento Grid but email-safe (table layout).
- Sections:
  - Header: "OS Pulse — {date}" with logo placeholder.
  - Bento highlights: top 3–5 `is_bento_worthy` items as styled cards.
  - "Full stream" link pointing to the deployed web URL.
  - Footer: unsubscribe link placeholder.

### 3. Newsletter sender (`agents/newsletter.py`)
- Reads today's Markdown digests from `web/src/content/digests/`.
- Filters `is_bento_worthy == true`.
- Renders the React Email template to HTML via `react-email` CLI
  (`npx react-email export`).
- Sends via Resend API (`POST https://api.resend.com/emails`).
- Subscriber list: read from `agents/subscribers.txt` (one email per line, gitignored).
- **Ask the user for their Resend API key before running a live send.**

### 4. `subscribers.txt` setup
- Add `agents/subscribers.txt` to `.gitignore`.
- Create `agents/subscribers.example.txt` with placeholder:
  ```
  you@example.com
  ```

### 5. Local test
- Run `python agents/newsletter.py --dry-run` to print the rendered HTML
  without sending.
- Confirm the Resend API key is valid with a single test send to your own address
  before enabling the workflow.

### 6. Deployed URL
Once the Astro site is deployed (Vercel / Netlify / GitHub Pages), update
`SITE_URL` in `.env.example` so the newsletter footer link is correct.

## Budget reminder
Each 12-hour batch should cost < €0.02 in LLM tokens.
Monitor `agents/output/usage.log` after the first few runs.
If costs spike, reduce `--since-hours` or increase the impact_score threshold
for triggering the premium model.
