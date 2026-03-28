# Sample versions

Changelog for prospect samples in [`service-samples`](https://github.com/ErikSvetich/service-samples). Use git tags when you need a reproducible snapshot.

---

## Sticky Wicket

Folder: [`-sticky-wicket/`](../-sticky-wicket/)

### V2 (recommendation-first)

- **Path:** `-sticky-wicket/v2/index.html`
- **Intent:** Address feedback that V1 felt like “more POS-style charts” on top of Square. V2 leads with **explicit recommendations**: estimated monthly savings, **current vs streamlined** staffing pattern (demo calendar), and **what changed** bullets. Optional small proof chart below the fold only to justify a single claim.
- **Tag:** (optional) `sticky-wicket-v2` after stable client review.

### V1 (interactive dashboard / service menu)

- **Path:** `-sticky-wicket/index.html` (default URL for the folder)
- **Description:** Dark-theme interactive deck: KPIs, Chart.js (overview, events, labor gap, menu, inventory, market, briefing). Mobile-tuned; Chart.js from CDN.
- **Feedback (client):** They already use **Square dashboards**; the sample was perceived as overlapping with POS charts rather than a distinct “do this” story. Led to V2.
- **Git tag:** `sticky-wicket-v1` marks the repo state where V1 is the primary `index.html` at `-sticky-wicket/` (see `git show sticky-wicket-v1:-sticky-wicket/index.html`).

---

## Adding a new client

1. Create `-client-slug/` with `index.html` (+ assets).
2. Add a subsection here and a row in the root [README](../README.md).
3. Tag optional: `client-slug-v1`.
