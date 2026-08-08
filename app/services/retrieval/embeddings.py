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
    try:
        model = GoogleGenerativeAI(
            model="models/gemini-embedding-2",
            google_api_key=settings.GEMINI_API_KEY,
        )
        model.embed_query("probe")
        logfire.info("Gemini Embeddings ready (gemini-embedding-2, 3072-dim).")
        return model
    except Exception as e:
        logfire.error(f"Gemini probe failed: {e}. Will use sentence-transformers fallback.")
        return None


def _load_fallback():
    """Load sentence-transformers fallback model."""
    from sentence_transformers import SentenceTransformer
    logfire.info("Loading sentence-transformers fallback (all-mpnet-base-v2, 768-dim).")
    return SentenceTransformer("all-mpnet-base-v2")

def _init():
    """Main code that does the Initialization of all the embeddings model."""
   
    global _active_model, _model_type

        if _active_model is None:
            return
        
        gemini = _probe_gemini()
        if gemini:
            _active_model = gemini
            _model_type = "gemini"
        else:
            _active_model = _load_fallback()
            _model_type = "fallback"

def get_embedding_dim() -> int:
    """
    Return the vector dimension of the active model. Call after _init().
    """
    _init()
    return _GEMINI_DIM if _model_type == "gemini" else _FALLBACK_DIM

# This is going to embed the embeddings.
def _embed_batch(batch: list[str]) -> list[list[float]]:
    if _model_type == "gemini":
        for attempt in range(4):
            try:
                return _active_model.embed_documents(batch)
            except Exception as e:
                err = str(e).lower()
                is_rate_limit = any(x in err for x in (429, "rate", "quota", "resource_exhausted"))
                if is_rate_limit and attempt <3:
                    wait = 2 ** attempt
                    logfire.warning(
                        f"Gemini rate limit hit - retrying in {wait}s"
                        f"(attempt {attempt +1}/4)"
                    )
                    time.sleep(wait)
                else:
                    logfire.error(f"Gemini Embedding failed: {e}")
                    raise
        raise RuntimeError("Gemini rate limit persisted after 4 attempts.")
    else:
        return _active_model.encode(batch, show_progress_bar=False).tolist()


def embed_query(query: str) -> list[float]:
    _init()
    if _model_type == "gemini":
        return _active_model.embed_query(query)
    return _active_model.encode([query])[0].tolist()
    
    

def embed_texts(texts: list[str]) -> list[list[float]]:
    _init()
    all_embeddings: list[list[float]] = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i: i + BATCH_SIZE]
        with logfire.span("Embed Batch", model = _model_type, start = i, size = len(batch)):
            all_embeddings.extent(_embed_batch(batch))
    
    return all_embeddings