# import streamlit as st
# from PIL import Image
# import io
# import numpy as np

# from controllers.model import extract_text_from_images
# from controllers.pdf2image_convertor import pdf_to_images
# from controllers.llm_model import get_structured_json

# st.set_page_config(page_title="Invoice Extractor", layout="centered")
# st.title("🧑‍💻 Invoice Data Extractor")

# # File uploader
# uploaded_file = st.file_uploader("Upload a PDF or Image file (JPG, PNG, TIFF)", type=["pdf", "jpg", "jpeg", "png", "tif", "tiff"])

# if uploaded_file is not None:
#     filename = uploaded_file.name.lower()
#     try:
#         # Step 1: Convert PDF/image to PIL images
#         if filename.endswith('.pdf'):
#             file_stream = io.BytesIO(uploaded_file.read())
#             images = pdf_to_images(file_stream)
#         else:
#             image = Image.open(uploaded_file).convert("RGB")
#             images = [image]

#         st.success("✅ File successfully processed into image(s)")


#         # Step 2: Extract text
#         extracted_text = ""
#         with st.spinner("🔍 Performing OCR..."):
#             images_np = [np.array(img) for img in images]
#             extracted_text = extract_text_from_images(images_np)

#         st.success("✅ Text successfully extracted from image(s)")

#         # Step 4: Get structured JSON from LLM
#         with st.spinner("🧠 Structuring data with LLaMA/LLM..."):
#             structured_data = get_structured_json(extracted_text)

#         st.subheader("Structured JSON Output")
#         st.json(structured_data)

#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")