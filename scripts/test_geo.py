"""
GEO Experiment — Automated AI Response Tester

Tests whether AI (with web search) surfaces/cites your GEO-optimized page.
Stores structured JSON results for research analysis.
"""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI

# ── CONFIG ────────────────────────────────────────────────
API_KEY = os.getenv("OPENAI_API_KEY")
ROUND = "automated_testing_round"
MODEL = "gpt-4.1"

TARGET_URL = "https://vahoramaher1994.github.io/geo-credit-ratings-guide"
TARGET_DOMAIN = "vahoramaher1994.github.io"

PROMPTS = {
    "P1": "How do credit rating APIs work?",
    "P2": "How does Morningstar DBRS publish credit rating data?",
    "P3": "How do you integrate credit rating data in Java Spring Boot?",
    "P4": "What is GEO optimization for financial content?",
    "P5": "credit rating API developer guide"
}

RESULTS_DIR = Path("results")


# ── HELPERS ───────────────────────────────────────────────
def now():
    return datetime.now(timezone.utc).isoformat()


def extract_text(response):
    """Extract text from OpenAI Responses API."""
    if hasattr(response, "output_text") and response.output_text:
        return response.output_text

    texts = []
    for item in getattr(response, "output", []):
        for content in getattr(item, "content", []):
            if hasattr(content, "text") and content.text:
                texts.append(content.text)

    return "\n".join(texts).strip()


def normalize(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def check_citation(response_text):
    """Detect whether the target site appears to be referenced."""
    text = normalize(response_text)

    signals = {
        "exact_url": TARGET_URL.lower() in text,
        "domain": TARGET_DOMAIN.lower() in text,
        "name_reference": "vahoramaher1994" in text,
        "title_hint": "credit rating data apis" in text
    }

    cited = any(signals.values())
    return cited, signals


def analyze_keywords(text):
    keywords = [
        "morningstar", "dbrs", "credit rating", "json-ld",
        "geo", "llms.txt", "faqpage", "spring boot",
        "resttemplate", "webclient", "postgresql"
    ]
    text_lower = text.lower()
    return [k for k in keywords if k in text_lower]


def preview(text, length=200):
    text = re.sub(r"\s+", " ", text).strip()
    return text[:length] + ("..." if len(text) > length else "")


def run_prompt(client, prompt):
    """Call OpenAI with web search enabled."""
    try:
        response = client.responses.create(
            model=MODEL,
            input=prompt,
            tools=[{"type": "web_search_preview"}],
            temperature=0.2
        )

        return {
            "ok": True,
            "text": extract_text(response),
            "id": getattr(response, "id", None),
            "error_type": None
        }

    except Exception as e:
        message = str(e).strip()
        lower_message = message.lower()

        if "exceeded your current quota" in lower_message:
            error_type = "quota_error"
        else:
            error_type = "request_error"

        return {
            "ok": False,
            "text": message,
            "id": None,
            "error_type": error_type
        }


# ── MAIN ──────────────────────────────────────────────────
def main():
    if not API_KEY:
        print("❌ ERROR: Set OPENAI_API_KEY first")
        print("PowerShell:")
        print('$env:OPENAI_API_KEY="your-key-here"')
        return

    client = OpenAI(api_key=API_KEY)

    print(f"\n🔍 GEO Experiment — {ROUND.upper()}")
    print(f"Model: {MODEL}")
    print(f"Time: {now()}")
    print(f"Target: {TARGET_URL}")
    print("=" * 60)

    results = {
        "round": ROUND,
        "model": MODEL,
        "timestamp": now(),
        "target_url": TARGET_URL,
        "prompts": {},
        "summary": {}
    }

    cited_count = 0
    success_count = 0
    error_count = 0

    for pid, prompt in PROMPTS.items():
        print(f"\n{pid}: {prompt}")
        print("Running...")

        res = run_prompt(client, prompt)
        text = res["text"]

        # Handle request failures correctly
        if not res["ok"]:
            error_count += 1

            print(f"Status: ❌ ERROR ({res['error_type']})")
            print(f"Preview: {preview(text)}")

            results["prompts"][pid] = {
                "prompt": prompt,
                "response": None,
                "response_id": None,
                "ok": False,
                "error_type": res["error_type"],
                "error_message": text,
                "cited": None,
                "signals": None,
                "keywords": [],
                "preview": preview(text)
            }
            continue

        success_count += 1

        cited, signals = check_citation(text)
        keywords = analyze_keywords(text)

        if cited:
            cited_count += 1

        print(f"Status: {'✅ CITED' if cited else '❌ NOT CITED'}")
        print(f"Signals: {signals}")
        print(f"Keywords: {keywords if keywords else 'none'}")
        print(f"Preview: {preview(text)}")

        results["prompts"][pid] = {
            "prompt": prompt,
            "response": text,
            "response_id": res["id"],
            "ok": True,
            "error_type": None,
            "error_message": None,
            "cited": cited,
            "signals": signals,
            "keywords": keywords,
            "preview": preview(text)
        }

    # ── SUMMARY ───────────────────────────────────────────
    results["summary"] = {
        "successful_calls": success_count,
        "error_calls": error_count,
        "total_prompts": len(PROMPTS),
        "cited_count": cited_count,
        "citation_rate": f"{cited_count}/{len(PROMPTS)}"
    }

    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"Success: {success_count}/{len(PROMPTS)}")
    print(f"Errors:  {error_count}/{len(PROMPTS)}")
    print(f"Cited:   {cited_count}/{len(PROMPTS)}")

    # ── SAVE ──────────────────────────────────────────────
    RESULTS_DIR.mkdir(exist_ok=True)
    filename = RESULTS_DIR / f"{ROUND}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Saved to: {filename}")


if __name__ == "__main__":
    main()