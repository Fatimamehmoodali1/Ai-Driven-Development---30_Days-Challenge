# GEMINI.md  
# Role: Senior Python AI Engineer

## Objective
Build a **Study Notes Summarizer + Quiz Generator Agent** using:
- **Streamlit**
- **PyPDF**
- **Gemini CLI**
- **openai-agents SDK**
- **Context7 MCP server**

The agent must summarize uploaded PDFs and generate quizzes strictly from the PDF text.

---

## 1. Project Overview

### A. PDF Summarizer
- User uploads PDF.
- Extract text using **PyPDF**.
- Agent produces a clean, structured academic summary.

### B. Quiz Generator
- After summary, user selects **Create Quiz**.
- Agent analyzes the **full PDF text**, not the summary.
- Generates **MCQs or mixed quiz questions**.

### Framework & Tools
```
UI: Streamlit  
Model: gemini-2.0-flash (via OpenAI Agents SDK)  
Tools: PyPDF  
MCP Server: Context7  
Custom Tool: PDF text extraction  
```

---

## 2. Critical Technical Constraints

### 1. Zero-Bloat Protocol (STRICT)
- No extra logic.
- No unnecessary comments.
- Only required implementation:
  - PDF extraction
  - Agent integration
  - Minimal UI

### 2. API Configuration
- Base URL:  
  `https://generativelanguage.googleapis.com/v1beta/openai/`
- API key from environment:  
  `GEMINI_API_KEY`
- Required model:  
  `OpenaiChatCompletionModel("gemini-2.0-flash")`

### 3. SDK Accuracy
- Must follow **official patterns** from `openai-agents` SDK.
- If any confusion or error → run:  
  `get-library-docs openai-agents` (Context7)

### 4. Error Recovery Protocol
If any of the following occur:
- AttributeError  
- TypeError  
- ImportError  
- Wrong function definitions  

Action:
1. **STOP**
2. Run: `get-library-docs openai-agents`
3. Re-write code EXACTLY as docs show.

### 5. Dependency Management
- Use **uv** for installing packages.
- If package already installed → **DO NOT reinstall**.

---

## 3. Architecture & File Structure
> Root directory only — do **NOT** create a `study_agent/` folder.

```
├── .env                 # Environment variables
├── tools.py             # PDF extraction tool
├── agent.py             # Agent setup & tool registration
├── app.py               # Streamlit UI
├── pdf_text_cache.txt   # Auto-created cache file
└── pyproject.toml       # UV config
```

---

## 4. Implementation Steps (Exact Order — No Skipping)

### Step 1: Documentation & Pattern Analysis
Before writing any code:
- Run: `get-library-docs openai-agents`
- Study:
  - Tool declaration syntax
  - `Agent` structure
  - `OpenaiChatCompletionModel`
  - Binding tools
  - Non-streaming agent calls
  - Function argument formats

If ANY uncertainty:  
**Run docs again.**

---

### Step 2: Tool Implementation (`tools.py`)

Required functions:
- `extract_pdf_text(file_path: str) -> str`
- `cache_pdf_text(text: str)`
- `read_cached_pdf_text() -> str`

Logic:
- Use PyPDF to read text.
- Save extracted text to `pdf_text_cache.txt`.
- If cache missing → return empty string.

Constraints:
- Must follow EXACT `openai-agents` tool format.
- No extra features.
- Minimal logic only.

---

### Step 3: Agent Configuration (`agent.py`)

Steps:
1. Initialize Gemini client with base URL.
2. Create:
   ```python
   OpenaiChatCompletionModel("gemini-2.0-flash")
   ```
3. Import tools from `tools.py`.
4. Bind tools according to SDK doc patterns.
5. System prompt:
   ```
   You are a Study Assistant. Summarize academic PDFs and generate 
   quizzes based strictly on the PDF content. When generating quizzes, 
   DO NOT use the summary—use the full PDF text.
   ```

Restrictions:
- No memory
- No custom caching beyond `pdf_text_cache.txt`
- No streaming mode

---

### Step 4: Application Logic (`app.py`)

Framework: **Streamlit**

UI sections:
- PDF Upload Area
- Summarize Button
- Create Quiz Button
- Output Display

Flow:
1. On upload:
   - Save temp file
   - Call `extract_pdf_text()`
   - Cache text
2. On “Summarize PDF”:
   - Call agent:  
     `"Summarize the extracted PDF text."`
3. On “Create Quiz”:
   - Call agent:  
     `"Based strictly on the full PDF text, generate 5–10 quiz questions."`

Restrictions:
- Minimal UI
- No advanced styling

---

## 5. Environment & Dependencies

### .env
```
GEMINI_API_KEY=your_key_here
```

### Required Packages
- `openai-agents`
- `streamlit`
- `pypdf`
- `python-dotenv`

### Smart Install Rule
- If package already exists → DO NOT reinstall.

---

## 6. MCP Server Notes
- Context7 must remain connected.
- If needing documentation:
  - Run `get-library-docs openai-agents`
- Always follow SDK patterns when unsure.

---

## 7. Developer Notes
- Must use uv for all dependency operations.
- Must keep project clean with **Zero-Bloat Protocol**.
- All agent calls must be **non-streaming**.
- Agent MUST use full PDF text for quizzes.

