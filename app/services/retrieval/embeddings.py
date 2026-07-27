import time
# from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
import logfire
from app.config import settings

BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768 # all-mpnet-base-v2

# When ever our gemini api will give us rate limiting issues we will fall back to this all-mpnet-base-v2 model

_active_model = None
_model_type:str | None = None

def _probe_gemini():
    """Try one embed call to verify Gemini is reachable. Returns model or None."""


def _load_fallback():
    return 

def _init():
    return

def get_embedding_dim() -> int:
    """
    Return the vector dimension of the active model. Call after _init().
    """

    return

# This is going to embed the embeddings.
def _embed_batch(batch: list[str]) -> list[list[float]]:
    return

def embed_query(query: str) -> list[float]:
    return

def embed_texts(texts: list[str]) -> list[list[float]]:
    _init()