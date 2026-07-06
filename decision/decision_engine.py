def decision_engine(query, original_response, risk):

    # LOW RISK
    if risk == "LOW":
        return (
            original_response,
            "Allow original LLM response",
            "The response is correct and supported by the evidence.",
            ["Wikipedia"]
        )

    # HIGH RISK (also handle MEDIUM as HIGH)
    elif risk in ["MEDIUM", "HIGH"]:

        from rag.retriever import get_retriever
        from rag.prompt_builder import build_prompt
        from rag.generator import generate_rag_response

        retriever = get_retriever()
        docs = retriever.similarity_search(query, k=3)

        if not docs:
            return (
                "I don't know.",
                "Trigger RAG",
                "The response may contain hallucinated or unsupported information.",
                ["Wikipedia"]
            )

        prompt = build_prompt(query, docs)
        rag_response = generate_rag_response(prompt)

        return (
            rag_response,
            "Trigger RAG",
            "The response may contain hallucinated or unsupported information.",
            ["Wikipedia"]
        )

    # fallback
    return (
        original_response,
        "Unknown",
        "Could not determine risk",
        []
    )