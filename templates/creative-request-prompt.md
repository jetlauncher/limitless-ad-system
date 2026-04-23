# Creative Request Prompt Template

Use this template to prompt Claude (or another AI) to generate ad copy and creative concepts from your brief.

Copy the section you need, fill in the `[brackets]`, and paste it into Claude Code, Claude Cowork, or Claude.ai.

---

## Prompt 1 — Generate Ad Concepts From a Brief

Use this after filling in your `ad-brief-template.md`.

```
I'm running a paid ad campaign and need to generate creative concepts.

Here's my campaign brief:

OFFER: [What you're selling]
AUDIENCE: [Who it's for]
PAIN POINTS: [Their top 2-3 problems]
KEY PROOF: [Your strongest credibility or results]
CTA: [What you want them to do]

Please generate one ad concept for each of these angles:
[list your angles — e.g. Pain, Mechanism, Offer, Urgency, Objection Handling]

For each concept, give me:
1. Working title (for the manifest — max 8 words)
2. Hook / headline (max 10 words)
3. Body copy (2-3 sentences)
4. CTA line
5. Suggested visual direction (one sentence)
6. Angle label (for filtering)

Format as a numbered list, one concept per block.
```

---

## Prompt 2 — Generate Variations on a Single Angle

Use this when you want to explore one angle deeply.

```
I want to test multiple variations of the [ANGLE] angle for my ad campaign.

Offer: [What you're selling]
Audience: [Who it's for]
The core tension for this angle: [Describe the pain, objection, or idea you're working with]

Generate 5 different variations of this angle. Each one should feel distinct —
different opening, different framing, different tone if needed.

For each variation:
- Hook (max 10 words)
- Body copy (2-3 sentences)
- CTA

Number them 1-5. No preamble, just the output.
```

---

## Prompt 3 — Update manifest.json From a Concept List

Use this after generating concepts to get a ready-to-use manifest update.

```
I've generated ad concepts and need to add them to my manifest.json.

Here are my concepts:
[paste your list of concepts here]

My image files will be named [v01.png, v02.png, ...] and stored in assets/alternatives/.

Please produce the manifest.json entries for each concept.
Each entry needs:
- slug (kebab-case, based on title)
- title
- angle
- family: "Alternatives"
- file: "assets/alternatives/[filename]"
- notes (a short description of the concept)
- proof (the key proof point or claim)
- cta (the call to action text)
- template (one of: "split", "statement", "poster")

Return the entries as valid JSON, formatted as an array.
```

---

## Prompt 4 — Review and Rank Ad Concepts

Use this when you have a set of concepts and want help deciding which to produce first.

```
I have [NUMBER] ad concepts. I want your help deciding which to prioritize for production.

Here they are:
[paste or describe your concepts]

Please evaluate each concept on:
1. Clarity — Does the message land in under 3 seconds?
2. Relevance — How well does it match the audience's current mindset?
3. Differentiation — Does it say something competitors wouldn't say?
4. Conversion potential — How likely is it to make someone take action?

Score each one out of 5 for each dimension. Then recommend which 3 to produce first and why.
```

---

## Prompt 5 — Improve a Specific Ad

Use this when one of your ads isn't performing or you want to strengthen a concept.

```
Here's one of my ad concepts that isn't working as well as I'd like:

Title: [title]
Hook: [current hook]
Body: [current body copy]
CTA: [current CTA]
Angle: [angle]

The problem: [describe what's not working — e.g. "the hook is too vague",
"it sounds like every other ad", "the CTA doesn't create urgency"]

Please give me 3 improved versions. Keep the same angle and CTA unless you have
a specific reason to change it. Explain briefly what you changed and why.
```

---

## Tips for Better Prompting

- **Paste your brief directly** rather than summarizing it — specifics produce better output
- **Give Claude the format you need** — if you need a table, ask for a table
- **Ask for reasoning** — "explain why you chose this hook" helps you learn and iterate faster
- **Reject and redirect** — if the first output misses the mark, say what's wrong: "too formal", "too long", "not specific enough to my audience"
- **Test multiple prompts** — the best copy rarely comes from the first attempt
