# Generator Workflow

This repo now supports a lightweight **generator starter** for students.

What it does today:
- creates a local campaign workspace
- reads your brand brief + campaign request
- uses **OpenAI** or **OpenRouter** for text generation
- outputs:
  - `manifest.generated.json`
  - `concepts.generated.md`
  - `copy-pack.generated.md`

What it does **not** do yet:
- fully render final ad images by itself for every provider/model combination
- replace your design judgment

Use this as a practical v1 workflow:
1. generate concepts and copy with the scripts
2. create images with Claude Code / Claude Cowork + your preferred image tool
3. review everything in the board

---

## Step 1 — Add API keys

Copy `.env.example` to `.env` and fill in:

```bash
cp .env.example .env
```

Set at least:
- `TEXT_PROVIDER`
- `TEXT_MODEL`
- either `OPENAI_API_KEY` or `OPENROUTER_API_KEY`

---

## Step 2 — Prepare inputs

You need two markdown files:

### A. Brand brief
Recommended location:
- `brand/generated-briefs/brand-brief.md`

You can create this by:
- filling in `templates/brand-questionnaire.md`
- or uploading a brand book + references and asking Claude to synthesize a brief

### B. Campaign request
You can write your own or start from:
- `examples/sample-campaign-request.md`

---

## Step 3 — Create a campaign folder

```bash
python3 scripts/bootstrap_campaign.py --name "day1-day2-flagship"
```

That will create a folder like:

```text
campaigns/20260423-2145-day1-day2-flagship/
```

Inside it you will get:
- `briefs/`
- `outputs/`
- `assets/originals/`
- `assets/alternatives/`

---

## Step 4 — Generate concepts + manifest

```bash
python3 scripts/generate_campaign_assets.py \
  --campaign campaigns/20260423-2145-day1-day2-flagship \
  --brand brand/generated-briefs/brand-brief.md \
  --request examples/sample-campaign-request.md
```

This writes:
- `outputs/manifest.generated.json`
- `outputs/concepts.generated.md`
- `outputs/copy-pack.generated.md`

---

## Step 5 — Create or import the images

At this point you have the **brain** of the campaign:
- angles
- hooks
- copy
- manifest structure

Now create the visual assets using:
- Claude Code
- Claude Cowork
- OpenAI image tools
- another image workflow you trust

Save the final PNGs into:
- `assets/originals/`
- `assets/alternatives/`

Then update the manifest file paths if needed.

---

## Step 6 — Review in the board

Use the generated manifest as your working base, then copy or merge it into the root `manifest.json` when you are ready to review in the board.

Start the board locally:

```bash
npx serve .
```

Open:

```text
http://localhost:3000
```

---

## Provider notes

### OpenAI
Best when you want:
- the simplest official setup
- text generation and potentially image-friendly OpenAI flows

### OpenRouter
Best when you want:
- model choice and routing flexibility
- copy and concept generation from many model options

Important:
- this repo's v1 generator is **optimized for text generation**
- if you use OpenRouter, treat it primarily as your concept/copy engine unless your chosen model/provider path clearly supports image workflows you have already tested
