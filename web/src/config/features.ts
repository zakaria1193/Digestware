// Build-time feature flags. Read from `PUBLIC_*` env vars so the values are
// inlined into the static build and the flags can be flipped per environment
// without code edits.
//
// SHOW_IMPACT_SCORE — gates every UI surface that displays the per-item
// impact score (badges, the Impact filter slider, the admin "High Impact ≥8"
// tile and Impact column, score-based highlight/dim treatments). The scoring
// mechanism is not yet reliable, so the default is OFF; set
// `PUBLIC_SHOW_IMPACT_SCORE=true` to re-enable it.

export const SHOW_IMPACT_SCORE =
  import.meta.env.PUBLIC_SHOW_IMPACT_SCORE === 'true';
