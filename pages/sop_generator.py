import streamlit as st
from openai import OpenAI
from pydantic import BaseModel, Field

# 1. Define the exact structure we want the AI to return
class SOPResponse(BaseModel):
    hook: str = Field(description="A compelling 1-paragraph opening hook")
    academic_background: str = Field(description="A 2-paragraph summary of the student's academic path")
    research_interests: str = Field(description="A 2-paragraph section on research interests and university fit")
    conclusion: str = Field(description="A 1-paragraph closing statement with career goals")

def sop_generator_page():
    st.header("📄 SOP Generator")
    
    # Adding a box for the API Key so you don't have to mess with computer settings
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")

    academic_background = st.text_area("Enter your academic background, goals, and interests:", height=150)

    if st.button("Generate SOP"):
        # Check if the user forgot their key or background text
        if not api_key:
            st.error("Please enter your OpenAI API key first.")
            return
        if not academic_background:
            st.warning("Please enter your academic background.")
            return

        with st.spinner("Writing your structured SOP..."):
            try:
                # 2. Connect to OpenAI
                client = OpenAI(api_key=api_key)
                
                prompt = f"Write a statement of purpose based on this background: {academic_background}"

                # 3. Call the AI and force it to use our SOPResponse structure
                # We use gpt-4o-mini because it fully supports structured JSON outputs and is very fast
                response = client.beta.chat.completions.parse(
                    model="gpt-4o-mini", 
                    messages=[
                        {"role": "system", "content": "You are an expert academic advisor."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format=SOPResponse,
                    temperature=0.7
                )

                # 4. Extract the structured data
                result = response.choices[0].message.parsed
                
                st.success("✅ SOP generated successfully!")

                # 5. Display the structured sections beautifully in Streamlit
                st.subheader("Opening Hook")
                st.write(result.hook)

                st.subheader("Academic Background")
                st.write(result.academic_background)

                st.subheader("Research Interests")
                st.write(result.research_interests)

                st.subheader("Conclusion & Goals")
                st.write(result.conclusion)
                
                # 6. Format the sections back together into one document for the download button
                full_text = f"{result.hook}\n\n{result.academic_background}\n\n{result.research_interests}\n\n{result.conclusion}"
                st.download_button("📥 Download Full SOP", full_text, "generated_sop.txt", "text/plain")

            except Exception as e:
                st.error(f"An error occurred: {e}")