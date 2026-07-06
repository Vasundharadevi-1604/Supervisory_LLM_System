from supervisory.hallucination_model import detect_hallucination

def re_verify(query, answer):
    return detect_hallucination(query, answer)