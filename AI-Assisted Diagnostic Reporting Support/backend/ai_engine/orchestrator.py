import numpy as np
from backend.ai_engine.vit_inference import get_vit_heatmap
from backend.ai_engine.llm_report import generate_report

def run_full_pipeline(ds_anonymized):
    pixel_data = ds_anonymized.pixel_array
    if len(pixel_data.shape) == 3:
        pixel_data = pixel_data[..., 0]  # take first frame

    # Normalize for display
    img_norm = (pixel_data - pixel_data.min()) / (pixel_data.max() - pixel_data.min() + 1e-6)
    img_norm = (img_norm * 255).astype(np.uint8)

    heatmap, findings = get_vit_heatmap(img_norm)
    report = generate_report(findings, modality=ds_anonymized.Modality if "Modality" in ds_anonymized else "Unknown")

    return {
        "findings": findings,
        "report_draft": report,
        "heatmap": heatmap.tolist(),  # JSON serializable
        "image_shape": img_norm.shape
    }