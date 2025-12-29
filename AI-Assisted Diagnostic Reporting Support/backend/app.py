from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.image_processing.ingest import load_dicom
from backend.image_processing.anonymizer import anonymize_dataset
from backend.ai_engine.orchestrator import run_full_pipeline
import tempfile
import os

app = FastAPI(title="AI Diagnostic Reporting Support API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".dcm"):
        raise HTTPException(400, "Only DICOM files supported")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".dcm") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        ds = load_dicom(tmp_path)
        ds_anonymized = anonymize_dataset(ds)

        result = run_full_pipeline(ds_anonymized)
        return result
    finally:
        os.unlink(tmp_path)