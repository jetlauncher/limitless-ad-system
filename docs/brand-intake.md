# Brand Intake

Before you ask Claude to generate ads, you need to give it creative direction. This document explains the two ways to do that and when to use each one.

---

## Why This Matters

Generic prompts produce generic ads. The more context Claude has about your brand — your voice, your audience, what you look like, what you never say — the more on-brand and usable the output will be.

Brand intake is not optional. It is the difference between ads that could belong to any business and ads that feel unmistakably yours.

---

## Two Ways to Prepare Creative Direction

### Path 1 — Answer the Questionnaire

**Best for:** New brands, businesses without a formal brand book, students building a brand from scratch.

Fill out `templates/brand-questionnaire.md`. It covers:

- Your audience and their mindset
- Your offer and key proof points
- Visual style and aesthetic references
- Tone of voice and words to use or avoid
- Forbidden looks and off-brand directions
- CTA preferences

This takes 20–40 minutes the first time. Save your completed questionnaire as `brand/generated-briefs/brand-brief.md` so Claude can reference it across sessions.

**How to use it with Claude:**

> "I've filled out my brand questionnaire. Please read it and use it as the creative brief for everything we build today."

Upload or share the file, then start generating.

---

### Path 2 — Drop In a Brand Book and Reference Images

**Best for:** Established brands with existing brand guidelines, agencies working with client brands.

Place your files in the `brand/` folder:

```
brand/
├── brand-book/          ← PDF or markdown brand guidelines
├── reference-images/    ← Logos, color swatches, example ads, mood board images
└── generated-briefs/    ← Claude's output after reading your brand materials
```

See `brand/README.md` for naming conventions and what to include.

**How to use it with Claude:**

> "I've added our brand book to brand/brand-book/ and some reference images to brand/reference-images/.
> Please read the brand book, study the visual references, and write a creative brief
> that captures our brand voice, visual style, and key messages.
> Save it to brand/generated-briefs/brand-brief.md."

Claude will synthesize your materials into a structured brief you can reuse.

---

## Which Path Should You Choose?

| Situation | Recommended path |
|-----------|------------------|
| No formal brand guidelines exist | Questionnaire |
| Brand is new or in development | Questionnaire |
| Client has a PDF brand guide | Brand book drop |
| You have strong visual references | Brand book drop + questionnaire |
| You want the fastest start | Questionnaire |
| You want the most accurate output | Both paths combined |

You can use both. Fill the questionnaire *and* drop in brand materials — Claude will synthesize everything.

---

## Using Your Brief Across Sessions

Once you have a completed brief (either from the questionnaire or from Claude synthesizing your brand book), save it to:

```
brand/generated-briefs/brand-brief.md
```

At the start of any new Claude session, share this file first:

> "Here is my brand brief. Please read it before we start generating anything."

This ensures every session builds on the same creative foundation.

---

## Templates and Checklists

| File | Purpose |
|------|---------|
| `templates/brand-questionnaire.md` | Full creative direction questionnaire |
| `templates/brand-profile-template.md` | Shorter brand profile for quick context |
| `templates/brand-book-checklist.md` | What to look for when reviewing a brand book |
