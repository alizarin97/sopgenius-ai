import streamlit as st
from pages.sop_generator import sop_generator_page
from pages.lor_generator import lor_generator_page
from pages.resume_generator import resume_generator_page
from pages.visa_letter_generator import visa_letter_generator_page

st.set_page_config(page_title="SOPGenius.AI", layout="centered")
st.title("🚀 SOPGenius.AI")
st.sidebar.title("Navigation")

# Choose page
page = st.sidebar.radio("Go to", ["SOP Generator", "LOR Generator", "Resume Generator", "Visa Letter Generator"])

# Route to pages
if page == "SOP Generator":
    sop_generator_page()
elif page == "LOR Generator":
    lor_generator_page()
elif page == "Resume Generator":
    resume_generator_page()
elif page == "Visa Letter Generator":
    visa_letter_generator_page()
