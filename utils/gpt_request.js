import openai
import os

# Set your API key here or in environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure it's set!

def load_prompt(doc_type):
    with open(f"prompts/{doc_type.lower()}_prompt.txt", "r") as file:
        return file.read()

def generate_text(doc_type, name, university, course, gpa, goals, experience):
    prompt_template = load_prompt(doc_type)
    prompt = prompt_template.format(
        name=name,
        university=university,
        course=course,
        gpa=gpa,
        goals=goals,
        experience=experience
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
