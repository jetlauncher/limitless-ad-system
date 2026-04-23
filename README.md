# Limitless Ad System

A lightweight, browser-based ad creative review board. Use it to display, filter, and compare multiple ad concepts — originals vs. alternatives, sorted by angle, format, or message type.

Built for teams and students who want a fast way to review creative output without needing design software or a shared drive.

---

## What This Is

This is a static web app that loads a list of ad concepts from a JSON file and displays them in a filterable gallery. You can:

- View ad images in a grid or full-screen modal
- Filter by creative family (Originals vs. Alternatives)
- Filter by advertising angle (Pain, Offer, Mechanism, Urgency, etc.)
- Navigate through each ad's metadata: hook, CTA, notes, template type

There is no backend. No login. No database. Just a folder of images, a manifest file, and a browser.

---

## Who This Is For

This starter kit is designed for:

- **Marketing students** learning to produce and review ad creative at volume
- **Business owners** who want a simple tool to review and compare ad variations
- **AI automation students** building creative workflows with Claude

If you're in the Limitless workshop, this is your canvas.

---

## Folder Structure

```
limitless-ad-system/
├── index.html              # The review board UI
├── app.js                  # Filtering, modal, and gallery logic
├── styles.css              # Dark theme styling
├── manifest.json           # Your ad data — edit this to add your creatives
│
├── assets/
│   ├── originals/          # Your hero concepts (ad1.png, ad2.png, etc.)
│   └── alternatives/       # Variation images (v01.png, v02.png, etc.)
│
├── examples/
│   └── agent-workshop/     # Sample campaign — use as reference
│       ├── brief.md
│       └── [images]
│
├── templates/
│   ├── ad-brief-template.md          # Fill this out before generating ads
│   └── creative-request-prompt.md    # Use this to prompt Claude
│
└── docs/
    ├── setup-with-claude-code.md     # Workflow for Claude Code users
    └── setup-with-claude-cowork.md   # Workflow for Claude Cowork users
```

---

## Replacing the Sample Content With Your Own

### Step 1 — Write your brief

Copy `templates/ad-brief-template.md` and fill in your campaign details: offer, audience, pain points, angles, and proof points.

### Step 2 — Generate your creatives

Use `templates/creative-request-prompt.md` to prompt Claude (or another AI tool) to produce ad concepts and copy variations. Save your output images into `assets/originals/` and `assets/alternatives/`.

**Naming convention:**
- Original concepts: `ad1-[angle].png`, `ad2-[angle].png`
- Alternative variations: `v01-[slug].png`, `v02-[slug].png`, …

### Step 3 — Update manifest.json

Each ad in `manifest.json` is one object in the array. Copy an existing entry and update it:

```json
{
  "slug": "v01-my-angle",
  "title": "Your ad headline or working title",
  "angle": "Pain",
  "family": "Alternatives",
  "file": "assets/alternatives/v01-my-angle.png",
  "notes": "What makes this angle work",
  "proof": "The evidence or social proof behind this claim",
  "cta": "Book your seat",
  "template": "split"
}
```

`family` must be either `"Originals"` or `"Alternatives"`.
`angle` can be anything — the filters are built automatically from whatever values you use.

### Step 4 — Preview locally

Run a local static server so `manifest.json` loads correctly:


```bash
npx serve .
```

Then open `http://localhost:3000` in your browser.

---

## Deploy to Vercel

You can publish this review board publicly in under two minutes.

### Option A — Vercel CLI

```bash
npm install -g vercel
vercel
```

Follow the prompts. Your site will be live at a `*.vercel.app` URL.

### Option B — Vercel Dashboard

1. Push this folder to a GitHub repository
2. Go to [vercel.com](https://vercel.com) and click **Add New Project**
3. Import your GitHub repo
4. Leave all settings as default — click **Deploy**

No build command needed. Vercel serves static files out of the box.

---

## Workflow Guides

| Tool | Guide |
|------|-------|
| Claude Code (terminal) | [docs/setup-with-claude-code.md](docs/setup-with-claude-code.md) |
| Claude Cowork (browser) | [docs/setup-with-claude-cowork.md](docs/setup-with-claude-cowork.md) |

---

## What Students Can Use This For

- **Ad creative review** — Compare messaging angles before spending on paid media
- **Carousel variants** — Load slide images and review copy treatments side by side
- **Thumbnail testing** — Review YouTube or social thumbnails before publishing
- **Static ad libraries** — Build a searchable archive of past creative output
- **Workshop deliverables** — Present your ad system to clients or instructors

The only thing you need to change is `manifest.json` and your image files.

---

## Tech Stack

- Vanilla JavaScript — no frameworks, no build tools
- CSS Grid and Flexbox
- Loads data from `manifest.json` via `fetch()`
- Works in any modern browser

---

## License

MIT — use it, modify it, share it.
