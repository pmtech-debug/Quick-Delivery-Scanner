import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Quick Delivery Scanner")
st.title("📦 Courier Invoice Reader")
st.write("Upload a photo of the 'Quick Delivery Express' invoice below.")

# 2. File Uploader (Works with your phone's camera or gallery)
uploaded_file = st.file_uploader("Capture or Select Invoice", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open and show the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Document', use_container_width=True)
    
    with st.status("Reading text... please wait", expanded=True) as status:
        # 3. Initialize the Reader (English)
        # This might take a minute the first time as it downloads the 'brain'
        reader = easyocr.Reader(['en']) 
        
        # 4. Extract Text
        raw_results = reader.readtext(np.array(image), detail=0)
        status.update(label="Scanning Complete!", state="complete", expanded=False)

    # 5. Display text in a copy-friendly way
    st.subheader("Extracted Details")
    st.info("Tap and hold any box below to copy the text.")
    
    for line in raw_results:
        # We use st.code because it provides a 'Copy' button on many browsers
        st.code(line, language=None)