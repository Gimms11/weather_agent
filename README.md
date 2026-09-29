# Weather Chatbot Agent

An intelligent conversational weather assistant powered by **LangChain**, **LangGraph** (with memory checkpointing), and **Skycast Google Weather**.

---

## Architecture Overview

```
weather_agent/
├── conseguir_clima.py   # Core weather agent logic and interactive CLI loop
├── main.py              # Application entry point
├── model.py             # Chat model configuration via init_chat_model
├── utils.py             # Response normalization and message parsing helpers
├── pyproject.toml       # Modern Python packaging configuration (uv/poetry/pip)
├── requirements.txt     # Standard pip dependency manifest
├── .env.example         # Environment variables template
└── .gitignore           # Git ignore rules for Python, virtualenvs, and secrets
```

---

## Requirements

- Python 3.10+
- An API key for your LLM Gateway / OpenAI compatible endpoint
- An API key for Google Weather via `skycast-google`

---

## Installation & Setup

### 1. Clone & Navigate to the Project

```bash
cd weather_agent
```

### 2. Set up a Virtual Environment

**Using `uv` (Recommended):**
```bash
uv venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
uv pip install -e .
```

**Using standard `venv` + `pip`:**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

| Variable | Description | Default |
|---|---|---|
| `API_KEY` | API Key for LLM service | Required |
| `BASE_URL` | Base URL for LLM provider API | `https://api.llmgateway.io/v1` |
| `MODEL_NAME` | Model identifier | `gemini-3.5-flash-lite` |
| `API_KEY_GOOGLE_CLIMA` | API Key for Skycast Google Weather service | Required |

---

## Usage

Start the interactive CLI chatbot:

```bash
python main.py
```

*Or directly:*

```bash
python conseguir_clima.py
```

Type your weather queries (e.g., *"¿Cómo está el clima en Buenos Aires?"*, *"Pronóstico para los próximos 3 días en Madrid"*) or type `salir` / `exit` to quit.
