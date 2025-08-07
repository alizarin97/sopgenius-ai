import streamlit as st

def visa_letter_generator_page():
    st.header("📄 Visa Letter Generator")

    full_name = st.text_input("Full Name:")
    passport_number = st.text_input("Passport Number:")
    program_name = st.text_input("Program & University:")
    purpose = st.text_area("Purpose of Travel:")

    if st.button("Generate Visa Letter"):
        visa_letter = f"""
        Visa Application Letter

        To Whom It May Concern,

        I, {full_name}, holding passport number {passport_number}, am writing to request a student visa to attend {program_name}.

        The purpose of my visit is: {purpose}

        Kindly consider my application favorably.

        Sincerely,
        {full_name}
        """

        st.success("✅ Visa Letter generated successfully!")
        st.text_area("Generated Visa Letter", visa_letter, height=300)
        st.download_button("📥 Download Visa Letter", visa_letter, "generated_visa_letter.txt", "text/plain")
