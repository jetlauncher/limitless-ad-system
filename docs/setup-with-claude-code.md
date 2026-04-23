# Setting Up Your Ad System with Claude Code

Claude Code is an AI coding assistant that runs in your terminal. You give it instructions in plain English, and it reads, writes, and edits files in your project folder. You do not need to know how to code to use it.

This guide walks you through setting up your own ad creative review board using Claude Code.

---

## Prerequisites

- [Node.js](https://nodejs.org) installed (version 18 or higher)
- Claude Code installed: `npm install -g @anthropic-ai/claude-code`
- A folder with your ad images ready (PNG or JPG)

---

## Step 1 — Clone the Starter Kit

```bash
git clone https://github.com/your-instructor/limitless-ad-system.git my-ad-system
cd my-ad-system
```

Or download the ZIP from GitHub and open that folder in your terminal.

---

## Step 2 — Launch Claude Code

Inside your project folder, run:

```bash
claude
```

Claude Code will open and read your project. You'll see a prompt where you can type instructions.

---

## Step 3 — Tell Claude About Your Campaign

Paste this into the Claude Code prompt (fill in your own details):

```
I'm setting up an ad review board for my business. Here's my campaign:

Offer: [What you're selling — e.g. "1-day AI workshop for business owners"]
Audience: [Who it's for — e.g. "Non-technical entrepreneurs aged 35-55 in Bangkok"]
Key pain points: [List 2-3 — e.g. "Behind on AI, think it's only for developers"]
Core angles I want to test: [e.g. "Pain, Offer, Social Proof, Urgency"]

My images are in: assets/originals/ and assets/alternatives/

Please update manifest.json to reflect my campaign. Use the existing entries as a format guide.
```

Claude Code will read your image files, check the folder structure, and update `manifest.json` to match your content.

---

## Step 4 — Generate Ad Copy Variations

Once your brief is in place, ask Claude to generate variations:

```
Based on my campaign brief, generate 10 ad copy variations — one for each of these angles:
Pain, Mechanism, Offer, Objection Handling, Urgency, Social Proof, Outcome, Reframe, Founder Authority, Awareness.

For each variation, give me:
- A working title
- The hook (first line of the ad)
- Body copy (2-3 sentences)
- CTA text

Format it as a table so I can review it easily.
```

Review the output, pick the strongest variations, and use them when briefing your designer or image generation tool.

---

## Step 5 — Add Your Images

Drop your image files into:

```
assets/originals/     ← your 2-3 hero concepts
assets/alternatives/  ← your variation images
```

Use this naming format:
- `ad1-pain.png`
- `v01-no-code.png`, `v02-offer.png`, etc.

Then ask Claude Code to sync the manifest:

```
My images are now in assets/originals/ and assets/alternatives/.
Please scan those folders and update manifest.json to include all the images.
Use my campaign angles and notes from the brief we discussed.
```

---

## Step 6 — Preview the Board

```bash
npx serve .
```

Open `http://localhost:3000` in your browser. You should see your ad gallery with filters working.

If something looks off, describe it to Claude Code:

```
The angle filters aren't showing up. Can you check manifest.json and make sure each ad has an angle field?
```

---

## Step 7 — Deploy to Vercel

When you're happy with the board:

```bash
vercel
```

Follow the prompts. You'll get a public URL you can share with clients, teammates, or your instructor.

---

## Tips for Working With Claude Code

- **Be specific about files.** Say "update manifest.json" not "update the data."
- **Show examples.** If you want a particular format, paste an example from the existing manifest.
- **Review before accepting.** Claude Code will show you what it plans to change. Read it before confirming.
- **Ask questions freely.** If you don't understand something in the code, ask Claude to explain it.

---

## Sample Conversation Flow

```
You: I have 30 images in assets/alternatives/. They're named v01 through v30.
     Can you add them all to manifest.json? Use "Alternatives" as the family.
     I'll fill in the angles and notes later.

Claude: Sure. I'll scan the folder and add an entry for each image with placeholder
        angles. You can update the angle and notes fields afterwards.
        [shows proposed changes]

You: Looks good. Go ahead.
```

---

## Need Help?

Ask Claude Code directly:

```
I'm stuck. Here's what I'm trying to do: [describe your goal].
Here's what's happening instead: [describe the problem].
```

Claude Code can read your files, check for errors, and suggest fixes.
