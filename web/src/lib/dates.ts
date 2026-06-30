// Relative-date display helpers.
//
// Dates on the public site are shown relative to the viewer's system date: an
// entry from the current calendar day reads "Today", the previous day reads
// "Yesterday", and anything older falls back to an absolute format. Comparison
// is done by calendar day in local time so it lines up with the absolute
// strings, which are produced with `toLocaleDateString`.

/** Whole calendar days between `date` and `now`, in local time (0 = same day). */
function calendarDaysAgo(date: Date, now: Date): number {
  const start = new Date(date.getFullYear(), date.getMonth(), date.getDate());
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const msPerDay = 24 * 60 * 60 * 1000;
  return Math.round((today.getTime() - start.getTime()) / msPerDay);
}

/**
 * Format `date` for display, substituting "Today" / "Yesterday" when it falls
 * on the current or previous calendar day. Anything else uses
 * `toLocaleDateString('en-US', options)`.
 *
 * `now` defaults to the moment of render; pass it explicitly in tests.
 */
export function relativeDate(
  date: Date,
  options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' },
  now: Date = new Date(),
): string {
  const days = calendarDaysAgo(date, now);
  if (days === 0) return 'Today';
  if (days === 1) return 'Yesterday';
  return date.toLocaleDateString('en-US', options);
}
