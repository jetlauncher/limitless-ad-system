# Limitless Ad System

A lightweight, browser-based ad creative review board — with a full setup flow for generating ads using Claude.

Students use this repo to set up their API keys, define their brand, generate ad concepts with Claude, and review the output in a filterable gallery.

---

## What This Is

This is a static web app that loads a list of ad concepts from a JSON file and displays them in a filterable gallery. You can:

- View ad images in a grid or full-screen modal
- Filter by creative family (Originals vs. Alternatives)
- Filter by advertising angle (Pain, Offer, Mechanism, Urgency, etc.)
- Navigate through each ad's metadata: hook, CTA, notes, template type

There is no backend. No login. No database. Just a folder of images, a manifest file, and a browser.

The generation side — writing copy, creating images, updating the manifest — is done through Claude Code or Claude Cowork. This repo gives you the structure and templates to make that workflow repeatable.

---

## Who This Is For

- **Marketing students** learning to produce and review ad creative at volume
- **Business owners** who want a simple tool to review and compare ad variations
- **AI automation students** building creative workflows with Claude

If you're in the Limitless workshop, this is your canvas.

---

## Full Workflow

### Step 1 — Add Your API Keys

Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
```

You need either an OpenAI key or an OpenRouter key. See [docs/api-key-setup.md](docs/api-key-setup.md) for which to use and where to get one.

### Step 2 — Fill Your Brand Intake

Tell Claude who you are before asking it to generate anything. Two options:

**Option A — Answer the questionnaire** (fastest for new brands):
Fill out `templates/brand-questionnaire.md` and save it to `brand/generated-briefs/brand-brief.md`.

**Option B — Drop in your brand book** (best for established brands):
Place your brand PDF in `brand/brand-book/` and reference images in `brand/reference-images/`. Ask Claude to synthesize a brief.

See [docs/brand-intake.md](docs/brand-intake.md) for the full walkthrough.

### Step 3 — Generate Your Creatives With Claude

Use `templates/creative-request-prompt.md` to prompt Claude (Code or Cowork) to produce ad concepts and copy variations. Save your output images into `assets/originals/` and `assets/alternatives/`.

**Naming convention:**
- Original concepts: `ad1-[angle].png`, `ad2-[angle].png`
- Alternative variations: `v01-[slug].png`, `v02-[slug].png`, …

### Step 4 — Update manifest.json

Each ad in `manifest.json` is one object in the array. Copy an existing entry and update it, or ask Claude to do it for you:

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

### Step 5 — Review in the Board

Run a local static server so `manifest.json` loads correctly:

```bash
npx serve .
```

Open `http://localhost:3000` in your browser. Filter by angle, compare originals vs. alternatives, and use the modal to review metadata.

### Step 6 — Deploy and Share

Publish your review board publicly in under two minutes.

**Option A — Vercel CLI:**
```bash
npm install -g vercel
vercel
```

**Option B — Vercel Dashboard:**
1. Push this folder to a GitHub repository
2. Go to [vercel.com](https://vercel.com) and click **Add New Project**
3. Import your GitHub repo
4. Leave all settings as default — click **Deploy**

No build command needed. Vercel serves static files out of the box.

---

## Folder Structure

```
limitless-ad-system/
├── index.html              # The review board UI
├── app.js                  # Filtering, modal, and gallery logic
├── styles.css              # Dark theme styling
├── manifest.json           # Your ad data — edit this to add your creatives
├── .env.example            # API key placeholders — copy to .env and fill in
│
├── assets/
│   ├── originals/          # Your hero concepts (ad1.png, ad2.png, etc.)
│   └── alternatives/       # Variation images (v01.png, v02.png, etc.)
│
├── brand/
│   ├── brand-book/         # Drop your brand PDF or guidelines here
│   ├── reference-images/   # Logos, swatches, mood board images
│   └── generated-briefs/   # Claude's synthesized brand briefs (save and reuse)
│
├── examples/
│   └── agent-workshop/     # Sample campaign — use as reference
│       ├── brief.md
│       └── [images]
│
├── templates/
│   ├── ad-brief-template.md          # Campaign brief to fill before generating
│   ├── creative-request-prompt.md    # Prompt templates for Claude
│   ├── brand-questionnaire.md        # Full brand intake questionnaire
│   ├── brand-profile-template.md     # Short brand profile for quick context
│   └── brand-book-checklist.md       # What to extract from a brand book
│
└── docs/
    ├── api-key-setup.md              # How to add your OpenAI or OpenRouter key
    ├── brand-intake.md               # How to prepare your creative direction
    ├── setup-with-claude-code.md     # Full workflow for Claude Code users
    └── setup-with-claude-cowork.md   # Full workflow for Claude Cowork users
```

---

## Workflow Guides

| Tool | Guide |
|------|-------|
| Claude Code (terminal) | [docs/setup-with-claude-code.md](docs/setup-with-claude-code.md) |
| Claude Cowork (browser) | [docs/setup-with-claude-cowork.md](docs/setup-with-claude-cowork.md) |
| API key setup | [docs/api-key-setup.md](docs/api-key-setup.md) |
| Brand intake | [docs/brand-intake.md](docs/brand-intake.md) |

---

## What Students Can Use This For

- **Ad creative review** — Compare messaging angles before spending on paid media
- **Carousel variants** — Load slide images and review copy treatments side by side
- **Thumbnail testing** — Review YouTube or social thumbnails before publishing
- **Static ad libraries** — Build a searchable archive of past creative output
- **Workshop deliverables** — Present your ad system to clients or instructors

---

## Tech Stack

- Vanilla JavaScript — no frameworks, no build tools
- CSS Grid and Flexbox
- Loads data from `manifest.json` via `fetch()`
- Works in any modern browser

---

## License

MIT — use it, modify it, share it.
