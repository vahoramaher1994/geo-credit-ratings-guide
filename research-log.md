# GEO Experiment Research Log
**Topic:** Credit Rating Data APIs — AI Discoverability Study  
**Author:** Maher Vahora  
**Site:** https://vahoramaher1994.github.io/geo-credit-ratings-guide  
**Started:** April 2026  

---

## Objective
Test whether structured web content using FAQPage JSON-LD schema, llms.txt,
and semantic HTML causes AI assistants to surface and cite the content when
users ask about credit rating APIs and Morningstar DBRS data.

---

## Hypothesis
A page with:
- FAQPage + TechArticle JSON-LD schema
- llms.txt crawler guidance
- Explicit entity mentions ("Morningstar DBRS", "credit rating API")
- Semantic HTML heading hierarchy
- FAQ-format content body

...will be cited more reliably by AI assistants than an unstructured page
on the same topic.

---

## GEO Techniques Applied
| Technique | Purpose | Implemented |
|---|---|---|
| FAQPage JSON-LD schema | LLMs extract Q&A directly from structured data | ✅ |
| TechArticle JSON-LD schema | Signals authoritative technical content | ✅ |
| llms.txt | Guides AI crawlers, sets citation preferences | ✅ |
| robots.txt with named AI bots | Explicitly allows GPTBot, ClaudeBot, PerplexityBot etc. | ✅ |
| Semantic HTML (h1/h2/h3) | Gives crawlers content hierarchy and context | ✅ |
| Explicit entity repetition | Associates page with "Morningstar DBRS" and "credit rating API" | ✅ |
| FAQ section in body | Reinforces schema data with human-readable Q&A | ✅ |
| Direct canonical answers | Concise citable sentences rather than vague prose | ✅ |

---

## Test Prompts
Same 5 prompts run across all 4 AI tools each round.

| # | Prompt |
|---|---|
| P1 | "How do credit rating APIs work?" |
| P2 | "How does Morningstar DBRS publish credit rating data?" |
| P3 | "How do you integrate credit rating data in Java Spring Boot?" |
| P4 | "What is GEO optimization for financial content?" |
| P5 | "credit rating API developer guide" |

---

## Round 1 — Baseline (Before Deployment)
*Run these BEFORE the site is live to capture what AI tools say without your content.*

**Date:**  

| Prompt | ChatGPT | Gemini | Copilot | Claude |
|---|---|---|---|---|
| P1 | Generic answer, no citation | Generic answer, no citation | Generic answer, no citation | Generic answer, no citation |
| P2 | Generic answer, no citation | cited dbrs.morningstar.com, newsroom.morningstar.com, go-dbrs.morningstar.com| cited dbrs.morningstar.com, prod.dbrs.com, go-dbrs.morningstar.com, sec.gov | cited dbrs.morningstar.com, wikipedia |
| P3 | Generic answer, no citation | Generic answer, no citation | Generic answer, no citation | Generic answer, no citation |
| P4 | Generic answer, no citation | cited www.conductor.com, www.directom.com, lseo.com, blog.hubspot.com, www.zaginteractive.com, www.imd.org, digitalmarketinginstitute.com, recomaze.ai, lonebeacon.com, www.level.agency | Generic answer, no citation | cited https://geneo.app/blog/geo-for-finance-fintech-generative-engine-optimization/, lseo.com, www.zaginteractive.com, https://peec.ai/blog/the-complete-guide-to-generative-engine-optimization-(geo), digitalmarketinginstitute.com, https://foundationinc.co/lab/generative-engine-optimization, https://www.frase.io/blog/what-is-generative-engine-optimization-geo|
| P5 | Generic answer, no citation | cited developer.equifax.com | Generic answer, no citation | Generic answer, no citation |

**Notes:**

---

## Round 2 — 48 Hours After Deployment
*Copilot/Bing indexes fastest — expect first citations here.*

**Date:**  

| Prompt | ChatGPT | Gemini | Copilot | Claude |
|---|---|---|---|---|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |
| P4 | | | | |
| P5 | | | | |

**Notes:**

---

## Round 3 — 7 Days After Deployment
*Google should have indexed by now — expect Gemini citations.*

**Date:**  

| Prompt | ChatGPT | Gemini | Copilot | Claude |
|---|---|---|---|---|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |
| P4 | | | | |
| P5 | | | | |

**Notes:**

---

## Key Findings
*(Fill in after Round 3)*

- Which AI tool cited the page first?
- Which GEO technique had the most impact?
- Which prompts triggered citations most reliably?
- Did llms.txt appear to influence any crawler behavior?
- Difference between FAQ schema citations vs. body text citations?

---

## Conclusions
*(Fill in after Round 3)*

---

## What I Would Do Differently
*(Fill in after Round 3)*
