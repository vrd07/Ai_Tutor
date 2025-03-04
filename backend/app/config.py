import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ai_tutor.db")

# LLM configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/api")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "mixtral")

# Auth0 configuration
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "")
AUTH0_API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE", "")
AUTH0_ALGORITHMS = os.getenv("AUTH0_ALGORITHMS", "RS256").split(",")
AUTH0_ISSUER = os.getenv("AUTH0_ISSUER", f"https://{AUTH0_DOMAIN}/")

# API configuration
API_PREFIX = "/api/v1"
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Tutor settings
DEFAULT_STUDENT_LEVEL = "beginner"
SUPPORTED_SUBJECTS = ["math", "science", "history", "language", "programming"]
MAX_CONVERSATION_HISTORY = 20

# System settings
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "60"))
QUEUE_SIZE = int(os.getenv("QUEUE_SIZE", "100"))