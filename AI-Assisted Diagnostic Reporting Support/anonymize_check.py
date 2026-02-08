import re
from datetime import datetime

def check_and_warn_phi(draft_text):
    """
    Simple PHI detection patterns (basic – expand as needed).
    Returns (has_phi: bool, warning: str)
    """
    patterns = [
        r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',          # Possible full names
        r'\b\d{2}/\d{2}/\d{4}\b',                # DOB dd/mm/yyyy
        r'\bNHS\s*\d{10}\b',                     # NHS number
        r'\b[A-Z]{3}\d{7}\b',                    # Possible hospital number
        r'\b\d{4}-\d{2}-\d{2}\b'                 # ISO dates
    ]
    
    has_phi = any(re.search(p, draft_text) for p in patterns)
    
    if has_phi:
        warning = (
            "\n\n*** PRIVACY WARNING ***\n"
            "Potential Protected Health Information (PHI) detected in draft.\n"
            "This is a draft tool only – ensure full anonymization before any use.\n"
            "Complies with UK GDPR principles – clinician responsibility."
        )
    else:
        warning = "\n\nDraft appears anonymized (basic check passed)."
    
    return has_phi, warning

# Example usage in save_draft_report (add to your function)
# has_phi, warning = check_and_warn_phi(draft_text)
# Then append warning to the file content
