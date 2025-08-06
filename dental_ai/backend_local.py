from dental_ai.prompts import REWRITE_AND_CLASSIFY_PROMPT
from llama_cpp import Llama

class LocalBackend:
    def __init__(self, model_path):
        # model_path: path to your local LLaMA model (ggml format)
        self.model = Llama(model_path=model_path)

    def process(self, anamnesis_text):
        prompt = REWRITE_AND_CLASSIFY_PROMPT.format(anamnesis_text=anamnesis_text.strip())
        # Generate output with low temperature for consistency
        output = self.model(
            prompt,
            max_tokens=1024,
            temperature=0.2,
            stop=None,
        )
        return output['choices'][0]['text'].strip()
