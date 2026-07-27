import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "enterprise_rag"
    GROQ_MODEL = "llama-3.3-70b-versatile"

# we create a singleton instance of the Settings class
# Singleton is a creational design pattern that restricts the instantiation of a class to exactly one single object
settings = Settings()

