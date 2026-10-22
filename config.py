"""Central configuration. Everything comes from environment variables / .env"""
import os
from dotenv import load_dotenv

load_dotenv()

## ── Gemini ────────────────────────────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "models/gemini-3.5-live")
GEMINI_VOICE = os.getenv("GEMINI_VOICE", "leda")

# Optional: Vertex AI instead of an API key
USE_VERTEX_AI = os.getenv("USE_VERTEX_AI", "false").lower() == "true"
VERTEX_PROJECT_ID = os.getenv("VERTEX_PROJECT_ID", "")
VERTEX_LOCATION = os.getenv("VERTEX_LOCATION", "us-central1")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")

# ── Agent persona ─────────────────────────────────────────────────────────────
AGENT_NAME = os.getenv("AGENT_NAME", "Reem")
COMPANY_NAME = os.getenv("COMPANY_NAME", "honour-junction")
AGENT_LANGUAGE = os.getenv("AGENT_LANGUAGE", "en-IN")

# Human hand-off number (sales team)
TRANSFER_NUMBER = os.getenv("TRANSFER_NUMBER", "9889479110")

# ── RAG (knowledge base search) ───────────────────────────────────────────────
USE_RAG = os.getenv("USE_RAG", "false").lower() == "true"
RAG_DEBUG = os.getenv("RAG_DEBUG", "true").lower() == "true"   # print [RAG]/[GEMINI] after each answer

# ── Server ────────────────────────────────────────────────────────────────────
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("PORT") or os.getenv("SERVER_PORT", "8000"))   # Render sets PORT

_origins = os.getenv("ALLOWED_ORIGINS", "*")
ALLOWED_ORIGINS = ["*"] if _origins == "*" else [o.strip() for o in _origins.split(",") if o.strip()]