def build_strict_prompt(query, evidence=None):
    """
    Strict Prompting Module
    Encourages regeneration from evidence before fallback
    """

    # -------------------------
    # BASE RULES
    # -------------------------
    rules = """
You are a factual correction assistant.

Follow these rules strictly:

1. Use ONLY the provided evidence.
2. Regenerate a corrected answer grounded in the evidence.
3. Remove unsupported or hallucinated claims.
4. Do NOT invent facts.
5. If evidence partially supports the answer, answer using available evidence.
6. ONLY if no relevant evidence exists, respond exactly:
Enough information is not available.
7. Keep response concise, factual and verified.
"""

    # -------------------------
    # NO EVIDENCE CASE
    # -------------------------
    if evidence is None:
        return f"""
{rules}

Question:
{query}

Verified Answer:
"""

    # -------------------------
    # HIGH-RISK RAG CASE
    # -------------------------
    return f"""
{rules}

Question:
{query}

Evidence:
{evidence}

Using ONLY this evidence,
generate a corrected verified answer.

Verified Answer:
"""