from datetime import datetime
import os

def save_draft_report(draft_text, image_info="unknown"):
    output_dir = "generated_drafts"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"draft_report_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Generated at: {timestamp}\n")
        f.write(f"Input: {image_info}\n")
        f.write("=" * 70 + "\n\n")
        f.write(draft_text.strip())
        f.write("\n\n" + "=" * 70 + "\n")
        f.write("DRAFT ONLY – Requires clinician review. Not diagnostic.\n")
    
    print(f"Saved: {filepath}")
    return filepath

# Quick test
if __name__ == "__main__":
    sample = "Sample findings: lungs clear. Impression: normal."
    save_draft_report(sample, "test_image.dcm")
