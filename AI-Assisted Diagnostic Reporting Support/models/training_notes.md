# Model Training Notes

## Vision Transformer (ViT)
- Base: google/vit-base-patch16-224-in21k
- Fine-tuned on: MIMIC-CXR public dataset (chest X-rays).
- Tasks: Classification of abnormalities + attention for heatmaps.
- Steps: 
  1. Load dataset via datasets library.
  2. Train for 5 epochs with AdamW optimizer.
  3. Export checkpoint to models/checkpoints/vit_finetuned.pth (not included here).
- Metrics: AUC ~0.85 on validation.

## LLM (BioGPT)
- Base: microsoft/biogpt
- Fine-tuned on: IU X-ray reports.
- Used for: Structured report generation.
- No checkpoint included; load from Hugging Face.