import os
import sys
import uuid
import json
import logfire

from qdrant_client import QdrantClient
from qdrant_client.http import models

from app.config import settings
from app.services.retrieval.embeddings import embed_texts, get_embedding_dim
from app.ingestion.loaders.pdf import parse_pdf
from app.ingestion.loaders.html import parse_html
from app.ingestion.loaders.text import parse_text
from app.ingestion.chunking.splitter import chunk_text

logfire.configure(service_name="enterprise-ingestion-service")

PROCESSED_DATA_DIR = "processed_data"

#Intialize Qdrant Client

qdrant_client = QdrantClient(
    url=settings.QDRANT_CLUSTER_ENDPOINT,
)

def save_processed_locally(data: dict, source_type: str, filename: str) -> str:
    """
    Save parsed chunk metadata as JSON in processed_data/<source_type>/.
    """

    pass

def process_file(file_path: str, filename: str, source_type: str):
    """
    Parse -> chunk -> save locally -> embed -> index in Qdrant.
    """

    pass

def process_directory(directory_path: str, source_type: str):
    """
    Process every file in a directory.
    """

    pass

def run_universal_ingestion(base_dir: str, explicit_source_type: str = None, wipe: bool = False):
    """
    Scan base_dir, map sub-folders to source types, and ingest all documents.
    Pass --wipe to drop and recreated the Qdrant collection before ingestion.
    """

    pass

