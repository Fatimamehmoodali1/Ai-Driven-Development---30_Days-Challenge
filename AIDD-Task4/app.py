import streamlit as st
from agent import agent
from tools import extract_pdf_text, cache_pdf_text, read_cached_pdf_text

st.title("Study Notes Summarizer + Quiz Generator")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Summarize PDF"):
        text = extract_pdf_text("temp.pdf")
        cache_pdf_text(text)
        summary = agent.run(f"Summarize the following text:\n\n{text}")
        st.write(summary)

    if st.button("Create Quiz"):
        text = read_cached_pdf_text()
        if text:
            quiz = agent.run(f"Based strictly on the full PDF text, generate 5–10 quiz questions from the following text:\n\n{text}")
            st.write(quiz)
        else:
            st.write("Please summarize the PDF first to create a quiz.")
