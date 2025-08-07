import streamlit as st

def sop_generator_page():
    st.header("📄 SOP Generator")

    academic_background = st.text_area("Enter your academic background, goals, and interests:")

    if st.button("Generate SOP"):
        generated_sop = f"""
        Statement of Purpose

        I am writing to express my interest in pursuing higher education aligned with my academic background and professional goals. With a strong foundation in {academic_background}, I am eager to contribute to and benefit from a dynamic learning environment.

        My long-term ambition is to gain expertise in this field and bring impactful change to society through innovation and research. This program will enable me to achieve those goals and prepare for a successful career.
        """

        st.success("✅ SOP generated successfully!")
        st.text_area("Generated SOP", generated_sop, height=300)
        st.download_button("📥 Download SOP", generated_sop, "generated_sop.txt", "text/plain")
