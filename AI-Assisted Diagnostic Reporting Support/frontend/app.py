import streamlit as st
import requests
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="AI Diagnostic Reporting Support", layout="wide")
st.title("AI-Assisted Diagnostic Reporting Support")
st.markdown("**AI-Assisted Draft – Mandatory Clinical Review Required**")

uploaded_file = st.file_uploader("Upload DICOM file", type=["dcm"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    with st.spinner("Processing..."):
        response = requests.post("http://127.0.0.1:8000/process", files=files)
    
    if response.status_code == 200:
        result = response.json()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image with AI Highlight")
            heatmap = np.array(result["heatmap"])
            # Simple overlay
            overlay = cv2.applyColorMap((heatmap * 255).astype(np.uint8), cv2.COLORMAP_JET)
            overlay = cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB)
            st.image(overlay, caption="AI Attention Heatmap", use_column_width=True)
        
        with col2:
            st.subheader("AI-Generated Draft Report")
            st.warning("AI-Assisted – Requires Review & Approval")
            edited_report = st.text_area("Edit Report", value=result["report_draft"], height=400)
            
            if st.button("Approve & Sign Report"):
                st.success("Report approved and logged.")
                st.balloons()
    else:
        st.error("Processing failed.")