import pydicom
from pydicom.uid import generate_uid
import datetime
import random

# Basic Application Level Confidentiality Profile (partial)
PHI_TAGS = [
    (0x0010, 0x0010),  # Patient Name
    (0x0010, 0x0020),  # Patient ID
    (0x0010, 0x0030),  # Patient Birth Date
    (0x0008, 0x0050),  # Accession Number
    (0x0008, 0x0090),  # Referring Physician
    (0x0010, 0x1000),  # Other Patient IDs
    (0x0020, 0x000D),  # Study Instance UID (replace)
    (0x0020, 0x000E),  # Series Instance UID (replace)
]

def anonymize_dataset(ds: pydicom.Dataset):
    # Remove/replace PHI
    for tag in PHI_TAGS:
        if tag in ds:
            if tag in [(0x0020, 0x000D), (0x0020, 0x000E)]:
                ds[tag].value = generate_uid()
            else:
                del ds[tag]

    # Date shifting
    if hasattr(ds, "PatientBirthDate") and ds.PatientBirthDate:
        shift_days = random.randint(30, 365)
        original = datetime.datetime.strptime(ds.PatientBirthDate, "%Y%m%d")
        shifted = original + datetime.timedelta(days=shift_days)
        ds.PatientBirthDate = shifted.strftime("%Y%m%d")

    # Clean burned-in annotations (simple blackout of common areas)
    if "PixelData" in ds:
        # Placeholder – in production use OpenCV + Tesseract
        pass

    ds.remove_private_tags()
    return ds