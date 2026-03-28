# Timberline Data · Service samples

Private-style portfolio decks we send to prospects. Each client gets a **`-<client-slug>`** folder (leading hyphen keeps sample roots grouped and easy to spot in the file tree).

| Folder | Client | Sample |
|--------|--------|--------|
| `-sticky-wicket/` | Sticky Wicket (Portland) | [V2 recommendations](-sticky-wicket/v2/) · [V1 dashboard](-sticky-wicket/) · [folder README](-sticky-wicket/README.md) · [changelog](docs/sample-versions.md) |

## GitHub connection

Main marketing site remote (for reference):

`https://github.com/ErikSvetich/timberlinedata.tech.git`

This repo is a **separate** GitHub project: **`ErikSvetich/service-samples`**.

### First-time push (from this folder)

If the GitHub repo does not exist yet:

1. On GitHub: **New repository** → name **`service-samples`** → Public → **do not** add README (this repo already has one).
2. In a terminal:

```bash
cd path/to/service-samples
git remote add origin https://github.com/ErikSvetich/service-samples.git
git push -u origin main
```

## GitHub Pages

1. In **`service-samples`** on GitHub: **Settings → Pages** → **Deploy from a branch** → Branch **`main`**, folder **`/` (root)**.
2. After the first deploy, the site will be at:

   **`https://eriksvetich.github.io/service-samples/`**

3. Sticky Wicket deck (direct link):

   **`https://eriksvetich.github.io/service-samples/-sticky-wicket/`**

## Add a new client

1. Create **`-your-client-slug/`** (lowercase, hyphens, no spaces).
2. Add **`index.html`** (and any assets, e.g. logos) in that folder.
3. List the row in the table above and add a card on the root **`index.html`** hub.

## Local preview

Open **`index.html`** in the repo root, or open **`-sticky-wicket/index.html`**, from disk (Chart.js loads from CDN; logo paths are relative).
