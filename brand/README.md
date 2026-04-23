# brand/

This folder holds all creative direction materials for your ad campaigns. Claude reads from here when generating copy and images. Keep it organized — what you put in directly affects what comes out.

---

## Folder Structure

```
brand/
├── brand-book/          ← Your brand guidelines (PDF, Markdown, or DOCX)
├── reference-images/    ← Logos, color swatches, example ads, mood board images
└── generated-briefs/    ← Claude's synthesized creative briefs (save these and reuse them)
```

---

## brand-book/

Place your brand guide here. Accepted formats:

- `brand-guide.pdf` — PDF export of your brand guidelines
- `brand-guide.md` — Markdown version (easiest for Claude to read)
- `brand-guide.docx` — Word document (Claude Code can read this)

If you're a student without a formal brand book, skip this folder and use the questionnaire instead. See `docs/brand-intake.md`.

**Naming convention:** Keep the filename simple. `brand-guide.pdf` is fine.

---

## reference-images/

Drop in any visual reference files that represent how your brand looks or should look. Useful things to include:

- Your logo (PNG with transparent background if possible)
- Brand colour swatches (as an image file)
- Examples of past ads that performed well
- Competitor ads you want to learn from (clearly labelled)
- Mood board images — photos, textures, or compositions that match your aesthetic

**Naming convention:**

```
logo-primary.png
logo-white.png
color-palette.png
example-ad-pain-angle.png
example-ad-offer-angle.png
reference-competitor-01.png
moodboard-lifestyle.png
```

Claude Code can read images directly. Claude Cowork requires you to upload them at the start of the session.

---

## generated-briefs/

This is where Claude saves synthesized creative briefs after reading your brand materials. You can also write briefs directly and save them here.

**The key file:** `brand-brief.md`

At the start of every session, share this file with Claude:

> "Here is my brand brief. Please read it before we start generating."

This keeps creative direction consistent across sessions.

**Other files you might save here:**

- `campaign-brief-[campaign-name].md` — Brief for a specific campaign
- `angle-research-[date].md` — Notes from an angle brainstorming session
- `copy-review-[date].md` — Claude's feedback on a batch of ads

---

## Quick Start

1. **No brand book?** Fill out `templates/brand-questionnaire.md` and save the result here as `brand-brief.md`
2. **Have a brand book?** Drop the PDF into `brand-book/` and any logos or references into `reference-images/`, then ask Claude to synthesize a brief
3. **Both?** Do both — more context = better output

See `docs/brand-intake.md` for the full walkthrough.
