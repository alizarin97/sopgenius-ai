import streamlit as st

def resume_generator_page():
    st.header("📄 Resume Generator")

    name = st.text_input("Full Name:")
    email = st.text_input("Email:")
    skills = st.text_area("List your skills (comma separated):")
    experience = st.text_area("Summarize your work experience:")

    if st.button("Generate Resume"):
        resume = f"""
        Resume

        Name: {name}
        Email: {email}

        Skills:
        {skills}

        Experience:
        {experience}
        """

        st.success("✅ Resume generated successfully!")
        st.text_area("Generated Resume", resume, height=300)
        st.download_button("📥 Download Resume", resume, "generated_resume.txt", "text/plain")
