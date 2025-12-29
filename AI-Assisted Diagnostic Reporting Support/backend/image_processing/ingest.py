import pydicom

def load_dicom(path: str):
    try:
        return pydicom.dcmread(path)
    except Exception as e:
        raise ValueError(f"Invalid DICOM file: {e}")