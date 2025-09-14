import os
from openai import OpenAI
from dental_ai.prompts import REWRITE_AND_CLASSIFY_PROMPT, PATIENT_FRIENDLY_EXPLANATION_PROMPT

class APIBackend:
    def __init__(self, api_key=None, model_name="gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided or set in environment variable OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.model_name = model_name

    def process(self, anamnesis_text, mode="clinician"):
        anamnesis_text = anamnesis_text.strip()

        if mode == "clinician":
            prompt = REWRITE_AND_CLASSIFY_PROMPT.format(anamnesis_text=anamnesis_text)
        elif mode == "patient":
            prompt = PATIENT_FRIENDLY_EXPLANATION_PROMPT.format(anamnesis_text=anamnesis_text)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
