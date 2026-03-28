# Timberline Data · Service samples

Private-style portfolio decks we send to prospects. Each client gets a **`-<client-slug>`** folder (leading hyphen keeps sample roots grouped and easy to spot in the file tree).

| Folder | Client | Sample |
|--------|--------|--------|
| `-sticky-wicket/` | Sticky Wicket (Portland) | Interactive analytics concept deck |

## GitHub Pages

Same GitHub account as the main site: [`ErikSvetich/timberlinedata.tech`](https://github.com/ErikSvetich/timberlinedata.tech).

1. Create this repository on GitHub: **`ErikSvetich/service-samples`** (empty, no README if you are pushing from here).
2. **Settings → Pages** → Build and deployment: **Deploy from a branch** → Branch **`main`**, folder **`/` (root)**.
3. After the first deploy, the site will be at:

   **`https://eriksvetich.github.io/service-samples/`**

4. Sticky Wicket deck (direct link):

   **`https://eriksvetich.github.io/service-samples/-sticky-wicket/`**

## Add a new client

1. Create **`-your-client-slug/`** (lowercase, hyphens, no spaces).
2. Add **`index.html`** (and any assets, e.g. logos) in that folder.
3. List the row in the table above and add a card on the root **`index.html`** hub.

## Local preview

Open **`index.html`** in the repo root, or open **`-sticky-wicket/index.html`**, from disk (Chart.js loads from CDN; logo paths are relative).
