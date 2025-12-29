import numpy as np
from backend.ai_engine.vit_inference import get_vit_heatmap

def test_heatmap_generation():
    dummy_img = np.zeros((224, 224), dtype=np.uint8)
    heatmap, findings = get_vit_heatmap(dummy_img)
    assert heatmap.shape == (224, 224)
    assert isinstance(findings, str)