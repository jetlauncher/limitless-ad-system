# API Key Setup

To generate ad copy and images with Claude, you need an API key from at least one of the two supported providers. This guide explains both options so you can choose the one that fits your situation.

---

## Which Key Do You Need?

| If you want to… | Use |
|-----------------|-----|
| Use ChatGPT / GPT-4 models directly | OpenAI API key |
| Access many models (GPT-4, Claude, Gemini, Flux, etc.) through one account | OpenRouter key |
| Use DALL-E for image generation | OpenAI API key |
| Use open-source image models (SDXL, Flux) | OpenRouter key |

You only need one. Start with whichever you already have access to.

---

## Option A — OpenAI API Key

### Get your key

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign in (or create a free account)
3. Click **Create new secret key**
4. Give it a name (e.g. "limitless-ad-system")
5. Copy the key — you will not be able to see it again

Your key will look like: `sk-proj-...` or `sk-...`

### When to use OpenAI

- You're already paying for ChatGPT Plus and want to use the same account
- You want DALL-E 3 for image generation
- You prefer the official OpenAI ecosystem

---

## Option B — OpenRouter API Key

### Get your key

1. Go to [openrouter.ai/keys](https://openrouter.ai/keys)
2. Create an account or sign in
3. Click **Create Key**
4. Copy the key

Your key will look like: `sk-or-...`

### When to use OpenRouter

- You want to switch between models (Claude, GPT-4, Mistral, Llama, etc.) without managing multiple accounts
- You want access to open-source image models like Flux or SDXL
- You want a single billing dashboard for all AI usage

---

## Adding Your Key to the Project

### For Claude Code users

1. Copy `.env.example` to a new file called `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` in any text editor and fill in your key:

   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

   or

   ```
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

3. Set the provider and model to match:

   ```
   IMAGE_PROVIDER=openai
   IMAGE_MODEL=dall-e-3
   ```

4. Save the file. Claude Code will read it automatically.

### For Claude Cowork users

Claude Cowork runs in your browser and does not read `.env` files directly. Instead, paste your key into the Claude Cowork session when prompted, or include it in your setup instructions at the start of the session.

Do not paste your API key into any file you plan to share or upload to GitHub.

---

## Keeping Your Key Safe

- `.env` is already listed in `.gitignore` — it will not be committed to git
- Never share your key in a public repo, a Slack channel, or a screenshot
- If you accidentally expose a key, revoke it immediately from the provider's dashboard and generate a new one
- Use separate keys for different projects so you can revoke one without affecting others

---

## Next Steps

Once your key is in place, follow the brand intake process:

- [docs/brand-intake.md](brand-intake.md) — Prepare your creative direction before generating ads
