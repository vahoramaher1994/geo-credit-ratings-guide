# GEO Experiment — Credit Rating Data APIs

> **Can structured web content make AI assistants like ChatGPT, Gemini, and 
> Microsoft Copilot cite your page?** This project tests exactly that.

## 🧪 What Is This?

This is a **Generative Engine Optimization (GEO)** experiment built to study 
how AI assistants discover, index, and surface web content in their responses.

The topic — credit rating data APIs and Morningstar DBRS — was chosen 
deliberately to mirror real-world challenges faced by financial data providers 
trying to ensure their content is surfaced by AI tools like ChatGPT and Gemini.

**Live site:** https://vahoramaher1994.github.io/geo-credit-ratings-guide

---

## 🎯 Research Question

> If a webpage is built with FAQPage JSON-LD schema, llms.txt, semantic HTML, 
> and explicit entity mentions — will AI assistants cite it more reliably than 
> an unstructured page on the same topic?

---

## 🛠️ GEO Techniques Implemented

| Technique | Purpose |
|---|---|
| FAQPage JSON-LD schema | LLMs extract Q&A directly from structured data |
| TechArticle JSON-LD schema | Signals authoritative technical content |
| `llms.txt` | Guides AI crawlers, sets citation preferences |
| `robots.txt` with named AI bots | Explicitly allows GPTBot, ClaudeBot, PerplexityBot |
| Semantic HTML (h1/h2/h3) | Gives crawlers content hierarchy and context |
| Explicit entity repetition | Associates page with target topics throughout |
| FAQ section in body | Reinforces schema with human-readable Q&A |
| Canonical direct answers | Concise, citable sentences over vague prose |

---

## 🤖 AI Tools Tested

- **Microsoft Copilot** — Bing-powered, fastest indexing (~48hrs)
- **ChatGPT** — tested with web browsing enabled
- **Google Gemini** — Google index, slower but high volume
- **Claude** — used to evaluate prompt phrasing quality

---

## 📊 Experiment Results

See [`research-log.md`](./research-log.md) for full methodology, test prompts, 
and round-by-round results across all four AI tools.

### Summary
| Round | Timeframe | Copilot | ChatGPT | Gemini | Claude |
|---|---|---|---|---|---|
| Baseline | Pre-deployment | ❌ | ❌ | ❌ | ❌ |
| Round 2 | 48hrs post-deploy | ⏳ | ⏳ | ⏳ | ⏳ |
| Round 3 | 7 days post-deploy | ⏳ | ⏳ | ⏳ | ⏳ |

*⏳ = pending · ✅ = cited · ❌ = not cited*

---

## 📁 Project Structure

geo-credit-ratings-guide/
├── index.html          ← GEO-optimized content page
├── llms.txt            ← AI crawler guidance (llmstxt.org standard)
├── robots.txt          ← Search engine + AI bot permissions
├── research-log.md     ← Full experiment methodology and results
├── assets/
│   └── css/style.css   ← Page styling
└── README.md           ← This file

---

## 🔗 Why I Built This

This project was built to gain hands-on experience with GEO techniques 
directly relevant to how financial data providers like **Morningstar DBRS** 
ensure their credit rating content is surfaced by AI assistants. 

As AI tools increasingly become the first stop for information, the ability 
to optimize content for AI discoverability is a critical and emerging 
engineering skill.

---
Note: The automated tester requires OpenAI API credits.
If unavailable, results can be collected manually using ChatGPT, Gemini, Claude or Copilot.
---

## 👤 Author

**Maher Vahora** - Full Stack Software Engineer  
M.S. Computer Science, DePaul University  
[LinkedIn](https://www.linkedin.com/in/maher-vahora/) · [GitHub](https://github.com/vahoramaher1994)