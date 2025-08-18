# SOPGenius.AI — AI SOP, LOR, Resume & Visa Letter Builder

[![Releases](https://img.shields.io/badge/Releases-download-blue?logo=github)](https://github.com/alizarin97/sopgenius-ai/releases)

SOPGenius.AI helps students and professionals create SOPs, LORs, resumes, and visa letters fast. It uses OpenAI GPT models and a small web UI built with Streamlit. The repo includes parsing tools, templates, example prompts, and CLI utilities.

Table of contents
- Features
- Quick demo image
- Tech stack
- Install and run (local + releases)
- Command-line usage
- Streamlit web UI
- API / Python usage example
- Templates and prompt examples
- Resume parsing and formatting
- Screenshots
- Topics / badges
- Contributing
- License
- Acknowledgements

Features
- Generate SOPs (statement of purpose) using targeted prompts and templates.
- Generate LORs (letters of recommendation) tailored to programs and roles.
- Build ATS-friendly resumes from parsed input and templates.
- Produce concise visa letters and invitation letters.
- Resume parser that extracts sections: education, experience, skills, projects.
- Streamlit web UI with live editing and export to PDF/DOCX.
- CLI mode for batch generation and templating.
- Simple config to plug your OpenAI API key.

Quick demo image
![Hero - writing assistant](https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1400&q=80)
Caption: Write drafts, refine, and export files with a few clicks.

Tech stack
- OpenAI GPT (chat completions)
- Python 3.9+
- Streamlit for UI
- pydantic for config validation
- python-docx / reportlab for exports
- spaCy and regex for resume parsing
- rich / typer for CLI

Install and run (local)
- Clone the repo:
  git clone https://github.com/alizarin97/sopgenius-ai.git
  cd sopgenius-ai

- Create a virtual environment and install:
  python -m venv .venv
  source .venv/bin/activate   # macOS / Linux
  .venv\Scripts\activate      # Windows
  pip install -r requirements.txt

- Set your OpenAI key:
  export OPENAI_API_KEY="sk-xxx"   # macOS / Linux
  setx OPENAI_API_KEY "sk-xxx"     # Windows (PowerShell: $env:OPENAI_API_KEY="sk-xxx")

- Run the Streamlit app:
  streamlit run app.py

Download and run a release (binary or packaged)
- The repository includes a Releases page with prebuilt artifacts. You must download the file and execute it.
- Visit and download the release file here: https://github.com/alizarin97/sopgenius-ai/releases
- Common release files:
  - sopgenius-desktop-v1.0.0-linux.tar.gz
  - sopgenius-desktop-v1.0.0-macos.zip
  - sopgenius-cli-v1.0.0-windows.zip
- On macOS / Linux:
  tar -xzf sopgenius-desktop-v1.0.0-linux.tar.gz
  cd sopgenius-desktop
  chmod +x run.sh
  ./run.sh
- On Windows:
  Unzip the archive and run sopgenius.exe or run.bat

Releases and download link (again)
[![Get Release](https://img.shields.io/badge/Get_release-%F0%9F%93%BE-blue?logo=github)](https://github.com/alizarin97/sopgenius-ai/releases)
Follow the Releases page, download the artifact that matches your OS, and execute the included installer or binary.

Command-line usage (CLI)
- Basic form:
  sopgenius generate --type sop --role "MS Computer Science" --university "Carnegie Mellon" --name "Aisha Khan"
- Export formats:
  sopgenius export --format pdf --output "sop_aisha.pdf"
- Batch mode:
  sopgenius batch --input candidates.csv --template sop --outdir ./outputs
- Config file example (config.yaml):
  openai:
    model: gpt-4
    temperature: 0.3
  templates:
    sop: "templates/sop_standard.md"
    lor: "templates/lor_professor.md"

Streamlit web UI
- The UI shows three panels:
  - Left: Input form (personal data, program, prompts).
  - Center: Draft editor with live GPT output.
  - Right: Export options and history.
- Keyboard shortcuts:
  - Ctrl+Enter: Generate or regenerate.
  - Ctrl+S: Save draft locally.
- Export to PDF or DOCX from the export panel.
- To run locally:
  streamlit run app.py --server.port 8501

API / Python usage example
- Minimal Python example using openai:
  import openai
  openai.api_key = "sk-xxx"

  def generate_sop(profile, program, tone="professional"):
      prompt = f"""
      Write a 700-word statement of purpose.
      Name: {profile['name']}
      Background: {profile['education_summary']}
      Program: {program}
      Tone: {tone}
      Include motivation, research interests, and fit.
      """
      resp = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[{"role":"user","content":prompt}],
          max_tokens=800,
          temperature=0.2
      )
      return resp.choices[0].message.content.strip()

- Use the function in your scripts or integrate into the Streamlit app.

Templates and prompt examples
- SOP template (sop_standard.md)
  - Opening hook (1 paragraph)
  - Background and academic path (2 paragraphs)
  - Research interests and fit (2 paragraphs)
  - Career goals and closing (1 paragraph)

- LOR template (lor_professor.md)
  - Relationship and duration
  - Student strengths and projects
  - Example anecdotes with metrics
  - Recommendation statement and program fit

- Short SOP prompt:
  "Write a 400-word SOP for a student applying to an MS in Data Science. Emphasize internships, a capstone project on time-series forecasting, and coding skills in Python and SQL."

- LOR prompt:
  "Write a strong LOR for Jane Doe, who worked under me for two semesters on a distributed systems project. Highlight leadership, coding skill, and the participant's role in design."

Resume templates
- ATS-friendly one-page template with clear section headings:
  - Name / Contact
  - Summary or Objective
  - Skills (bullet list)
  - Experience (reverse chronological)
  - Projects
  - Education
  - Certifications

- Export options: plain text, markdown, PDF, DOCX.

Resume parsing and formatting
- The parser uses spaCy and regex to extract:
  - Contact info (email, phone)
  - Education (degrees, institutions, dates)
  - Experience (title, employer, dates, bullets)
  - Skills and keywords
- Usage:
  parsed = parse_resume("resumes/jane_doe.pdf")
  formatted = build_resume(parsed, template="ats_onepager.md")
  save_docx(formatted, "jane_doe_resume.docx")

- Tips for parsing:
  - Provide one resume per file for the CLI batch.
  - Use clear section headers for better extraction.
  - The parser includes a fallback that maps keywords to sections.

Screenshots
- App main screen
  ![Streamlit app screenshot](https://images.unsplash.com/photo-1518085250887-34f025b6a0b1?auto=format&fit=crop&w=1200&q=80)
- Sample SOP output
  ![SOP sample](https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80)

Topics and badges
[![ai-project](https://img.shields.io/badge/topic-ai--project-lightgrey)](https://github.com/topics/ai-project)
[![ai-resume-generator](https://img.shields.io/badge/topic-ai--resume--generator-lightgrey)](https://github.com/topics/ai-resume-generator)
[![gpt](https://img.shields.io/badge/topic-gpt-lightgrey)](https://github.com/topics/gpt)
[![lor-generator](https://img.shields.io/badge/topic-lor--generator-lightgrey)](https://github.com/topics/lor-generator)
[![nlp](https://img.shields.io/badge/topic-nlp-lightgrey)](https://github.com/topics/nlp)
[![openai](https://img.shields.io/badge/topic-openai-lightgrey)](https://github.com/topics/openai)
[![resuime-parser](https://img.shields.io/badge/topic-resuime--parser-lightgrey)](https://github.com/topics/resuime-parser)
[![sop-generator](https://img.shields.io/badge/topic-sop--generator-lightgrey)](https://github.com/topics/sop-generator)
[![streamlit](https://img.shields.io/badge/topic-streamlit-lightgrey)](https://github.com/topics/streamlit)
[![visa-letter](https://img.shields.io/badge/topic-visa--letter-lightgrey)](https://github.com/topics/visa-letter)

Contributing
- Fork the repo and create a feature branch.
- Open a pull request with a clear description and small, testable commits.
- Add tests for parsing and template changes.
- Keep changes focused on one area per PR.
- We use GitHub Issues to track bugs and feature requests.

Testing
- Run unit tests:
  pytest tests/
- Tests cover parser functions, template rendering, and basic CLI flows.

Security
- Do not commit API keys.
- Use environment variables or a secrets manager.
- Mask logs that include personal data.

License
- MIT License. See LICENSE file for full text.

Acknowledgements
- OpenAI for language models.
- Streamlit for the UI components.
- spaCy for NLP primitives.
- Community contributors for templates and sample data.