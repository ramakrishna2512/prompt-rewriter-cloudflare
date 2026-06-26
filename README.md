# ✍️ Prompt Rewriter — Cloudflare Workers AI

Rewrites a rough prompt into a clearer one while preserving the original intent. Streamlit UI on top of a Cloudflare Worker running [Workers AI](https://developers.cloudflare.com/workers-ai/) (Mistral-7B-Instruct), deployed serverlessly — no GPU, no server to manage.

**🔗 Live demo:** https://prompt-rewriter-cloudflare.vullagantiramakrishna.workers.dev
*(the URL above is the live API; run the Streamlit UI locally to talk to it — see below)*

## Architecture

```
Streamlit UI (app.py)  →  POST /  →  Cloudflare Worker (src/index.js)  →  Workers AI (Mistral-7B)
```

The worker takes a `prompt`, sends it to Mistral-7B with a system instruction to rewrite clearly, and returns the result as JSON.

## Stack

`Streamlit` `Cloudflare Workers` `Workers AI` `Mistral 7B` `JavaScript` `Python` `Vitest`

## Running the frontend locally

```bash
pip install streamlit requests
streamlit run app.py
```

The UI calls the deployed Worker directly, so no backend setup is needed to try it.

## Deploying the Worker yourself

```bash
npm install
npx wrangler login
npx wrangler deploy
```

Update `API_URL` in `app.py` to point at your own deployed Worker URL.

## API

**POST /**

```json
{ "prompt": "ai agents are confusing" }
```

**Response**

```json
{ "ok": true, "result": { "response": "Explain what AI agents are..." } }
```

## Tests

```bash
npm test
```

## Roadmap

- Multiple rewrite styles (concise / detailed / creative)
- Before-vs-after prompt scoring
- Prompt history
- Configurable rewrite rules
