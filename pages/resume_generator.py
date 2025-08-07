import streamlit as st

def resume_generator_page():
    st.header("📄 Resume Generator")
    st.text_area("Enter your professional and academic details:")
    if st.button("Generate Resume"):
        st.success("Resume generated successfully!")