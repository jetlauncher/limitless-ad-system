# Setting Up Your Ad System with Claude Cowork

Claude Cowork is a browser-based workspace where you can work alongside Claude on projects — uploading files, reviewing output, and giving feedback — without using a terminal.

This guide is for students who prefer a visual, no-terminal workflow. It covers the full setup: API keys, brand intake, ad generation, and reviewing the board.

---

## What Claude Cowork Is Good For

- Reviewing and editing your `manifest.json` without touching code
- Getting Claude to generate ad copy variations from your brief
- Uploading images and having Claude rename or organize them
- Asking questions about how the system works
- Reviewing the review board itself in a side-by-side layout

## About the Generator Scripts

The generator scripts (`scripts/bootstrap_campaign.py` and `scripts/generate_campaign_assets.py`) run in a terminal and are not available inside Claude Cowork. If you have terminal access, see [docs/generator-workflow.md](generator-workflow.md) for a faster way to produce concept and copy drafts before your Cowork session.

If you're working entirely in Cowork, the manual workflow below covers the same ground — it just involves more back-and-forth with Claude directly.

---

## Step 1 — Get the Starter Kit

Download the ZIP file from your instructor's GitHub repository:

1. Go to the repo page on GitHub
2. Click the green **Code** button → **Download ZIP**
3. Unzip it on your computer

You'll have a folder called `limitless-ad-system`.

---

## Step 2 — Add Your API Key

Claude Cowork runs in your browser and doesn't read `.env` files directly. At the start of your session, paste your API key into the session context when Claude asks, or include it explicitly in your first message if you're running a generation workflow outside of Cowork.

Not sure which key to get? See [docs/api-key-setup.md](api-key-setup.md) — you need either an OpenAI key or an OpenRouter key.

Do not paste your key into any file you plan to share or upload to GitHub.

---

## Step 3 — Open Claude Cowork

Go to [claude.ai/cowork](https://claude.ai) and start a new project or session.

Upload the following files from your `limitless-ad-system` folder at the start of every session:

- `manifest.json`
- `brand/generated-briefs/brand-brief.md` (your brand brief — see Step 4)
- `examples/agent-workshop/brief.md` (as a reference example, optional)
- `examples/sample-brand-brief.md` (as a format reference, optional)
- `templates/ad-brief-template.md`

---

## Step 4 — Prepare Your Brand Intake

Before generating anything, give Claude your creative direction.

**Option A — Answer the questionnaire (fastest for new brands):**

Open `templates/brand-questionnaire.md` in any text editor (Notepad, TextEdit, VS Code). Fill in your campaign details:

- What you're offering
- Who you're targeting
- Their mindset, fears, and language
- Your visual style and tone of voice
- Words to use and avoid
- CTA preferences

Save it, then upload the filled-in questionnaire to your Claude Cowork session. Tell Claude:

```
Here's my completed brand questionnaire. Please read it and use it as
the creative brief for everything we generate today.
```

**Option B — Drop in your brand book:**

Upload your brand PDF and any reference images to the session. Tell Claude:

```
Here is our brand guide and some reference images.
Please read them and write a creative brief that captures our brand voice,
visual style, and key messages. I'll reuse this brief across sessions.
```

See [docs/brand-intake.md](brand-intake.md) for the full walkthrough.

---

## Step 5 — Fill In Your Campaign Brief

Open `templates/ad-brief-template.md` in any text editor. Fill in the campaign-specific details (offer, audience, angles to test). This is separate from the brand brief — it's campaign-level context.

Upload it and tell Claude:

```
Here's my campaign brief. I want to build an ad review board for this campaign.
Please review the brief and let me know if anything is unclear before we start.
```

---

## Step 6 — Generate Ad Concepts

Once Claude understands your brief, ask it to produce variations:

```
Based on my brief, generate ad concepts for the following angles:
Pain, Mechanism, Offer, Urgency, and Social Proof.

For each concept, give me:
- A working title (for the manifest)
- The main hook
- 2-3 lines of body copy
- A CTA

I'll use these to brief my designer (or image generation tool).
```

Copy the output into a document. These become your ad titles, notes, and CTAs in `manifest.json`.

---

## Step 7 — Update manifest.json

Ask Claude to update the manifest based on your new concepts:

```
Here are my 10 ad concepts with their titles, angles, and CTAs.
Please update manifest.json to include them.
The image files will be named v01.png through v10.png in assets/alternatives/.
Use "Alternatives" as the family for all of them.

[paste your concept list here]
```

Claude will produce an updated `manifest.json`. Download it and replace the original file in your project folder.

---

## Step 8 — Add Your Images

Put your image files into the right folders:

```
assets/originals/     ← your 2-3 core concept images
assets/alternatives/  ← your variation images
```

Name them to match what's in `manifest.json` — the `file` field in each entry tells you the expected path.

---

## Step 9 — Preview Locally or Deploy

**Local preview:**
You must use a local server — opening `index.html` directly in your browser will not work because the app loads `manifest.json` via `fetch()`, which browsers block on the `file://` protocol. Run this from inside your project folder:

```bash
npx serve .
```

Then open `http://localhost:3000` in your browser.

**Deploy to Vercel:**
If you have a GitHub account, push your folder to a repo and connect it to [vercel.com](https://vercel.com). Your review board will be live at a public URL in under a minute.

Alternatively, ask Claude Cowork:

```
Can you walk me through deploying this to Vercel step by step?
I'm not a developer — please keep it simple.
```

---

## Step 10 — Iterate

As you review your creative board, use Claude Cowork to:

- Rewrite hooks that aren't landing
- Add new angles you want to test
- Update notes and proof points in the manifest
- Ask "which of these angles is most likely to convert and why?"

---

## Tips for Claude Cowork

- **Upload files, don't copy-paste long JSON.** Claude handles files more reliably than walls of pasted text.
- **Be specific about what you want changed.** "Update the title of v03 to X and change the angle to Pain" is better than "fix the manifest."
- **Download updated files immediately.** Cowork sessions can close — always save your updated manifest before leaving.
- **Use it for thinking, not just tasks.** Claude can help you decide which angles to prioritize, which hooks are weakest, and what's missing from your brief.

---

## Sample Conversation

```
You: I've uploaded my brief and the current manifest.json.
     I want to add 5 new variations focused on the Objection Handling angle.
     The objections are: "I'm not technical enough", "It's too expensive",
     "I don't have time", "It won't work for my industry", "I'll do it later."

Claude: Got it. Here are 5 manifest entries for those objections, one per image slot.
        I've used v31 through v35 as the file slugs — update the filenames to match.
        [shows JSON entries]
        Want me to also write the copy for each one?

You: Yes please. Keep each hook under 10 words.
```

---

## Have Terminal Access?

If you can run Python in a terminal, the generator scripts can give you a starting draft before your Cowork session — concepts, copy, and a manifest outline — so you spend your session refining rather than starting from scratch.

See [docs/generator-workflow.md](generator-workflow.md) for how to use them.

---

## Need Help?

You can ask Claude Cowork anything:

```
I'm confused about how manifest.json connects to the images.
Can you explain how the file field works and show me an example?
```

Claude can explain, demo, and fix things in plain language.
