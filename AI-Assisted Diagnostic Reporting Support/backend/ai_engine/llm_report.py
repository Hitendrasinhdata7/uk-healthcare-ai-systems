from transformers import pipeline
import torch

# BioGPT or any biomedical LLM
generator = pipeline(
    "text-generation",
    model="microsoft/biogpt",
    device=0 if torch.cuda.is_available() else -1
)

def generate_report(findings: str, modality: str = "Chest PA"):
    prompt = f"""Generate a structured radiology report.

Technique: {modality}
Findings: {findings}
Impression:

"""
    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    return result[0]["generated_text"].split("Impression:")[0] + "Impression: [To be completed by clinician]"