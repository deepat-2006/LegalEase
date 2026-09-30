import streamlit as st

st.set_page_config(page_title="LegalEase", page_icon="⚖️")

st.title("⚖️ LegalEase - Legal Document Simplifier")
st.write("AI-powered legal document simplifier for common people")

uploaded_file = st.file_uploader("Upload your legal document", type=["txt", "pdf"])
user_text = st.text_area("Or paste your legal text here:")

if st.button("Simplify"):
    if user_text:
        st.subheader("Simplified Version:")
        st.success("This document basically says: Your agreement is valid for 1 year and can be cancelled with 30 days notice. (This is demo - AI integration coming soon)")
    elif uploaded_file:
        st.success("File uploaded! Simplification will be shown here.")
    else:
        st.warning("Please upload or paste some text da!")
