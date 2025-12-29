from backend.image_processing.anonymizer import anonymize_dataset
import pydicom
from pydicom.dataset import Dataset

def test_anonymize_removes_patient_name():
    ds = Dataset()
    ds.PatientName = "John Doe"
    ds.PatientID = "12345"
    anonymized = anonymize_dataset(ds)
    assert "PatientName" not in anonymized
    assert "PatientID" not in anonymized