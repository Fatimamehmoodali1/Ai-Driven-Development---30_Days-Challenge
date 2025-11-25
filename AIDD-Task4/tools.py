from openai_agents.tool import tool
from pypdf import PdfReader

@tool
def extract_pdf_text(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path: The path to the PDF file.

    Returns:
        The extracted text.
    """
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

@tool
def cache_pdf_text(text: str):
    """
    Caches the extracted PDF text to a file.

    Args:
        text: The text to cache.
    """
    with open("pdf_text_cache.txt", "w", encoding="utf-8") as f:
        f.write(text)

@tool
def read_cached_pdf_text() -> str:
    """
    Reads the cached PDF text from a file.

    Returns:
        The cached text, or an empty string if the cache file is not found.
    """
    try:
        with open("pdf_text_cache.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
