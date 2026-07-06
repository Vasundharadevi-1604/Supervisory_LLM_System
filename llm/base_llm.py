import requests
import os

# Load API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def generate_llm_response(prompt: str):
    try:
        # -----------------------------
        # CHECK API KEY
        # -----------------------------
        if not GROQ_API_KEY:
            return "LLM Error: GROQ API key not set"

        # -----------------------------
        # API CONFIG
        # -----------------------------
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",   # ✅ working free model
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7
        }

        # -----------------------------
        # API CALL
        # -----------------------------
        response = requests.post(url, headers=headers, json=data, timeout=30)

        # -----------------------------
        # ERROR HANDLING
        # -----------------------------
        if response.status_code != 200:
            return f"LLM API Error: {response.text}"

        result = response.json()

        # -----------------------------
        # SAFE RESPONSE EXTRACTION
        # -----------------------------
        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0]["message"]["content"]
            return content.strip()
        else:
            return "LLM Error: Invalid response format"

    except requests.exceptions.Timeout:
        return "LLM Error: Request timed out"

    except requests.exceptions.RequestException as e:
        return f"LLM Error: {str(e)}"

    except Exception as e:
        return f"LLM Error: {str(e)}"