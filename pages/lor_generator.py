import streamlit as st

def lor_generator_page():
    st.header("📄 LOR Generator")

    professor_name = st.text_input("Enter Professor's Name:")
    relationship = st.text_input("Your relationship with the recommender:")
    achievements = st.text_area("Enter key achievements and strengths:")

    if st.button("Generate LOR"):
        generated_lor = f"""
        Letter of Recommendation

        To Whom It May Concern,

        I am writing to recommend the student who has shown exemplary performance in academics and extracurriculars. As {relationship} to the student, I can confidently say they have demonstrated {achievements}.

        I strongly recommend them for your program and believe they will excel in any challenge they take on.

        Sincerely,
        {professor_name}
        """

        st.success("✅ LOR generated successfully!")
        st.text_area("Generated LOR", generated_lor, height=300)
        st.download_button("📥 Download LOR", generated_lor, "generated_lor.txt", "text/plain")
