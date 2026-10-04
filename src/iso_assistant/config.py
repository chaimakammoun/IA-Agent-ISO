from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIRECTORY = PROJECT_ROOT / "data"
VECTOR_DATABASE_DIRECTORY = PROJECT_ROOT / "lancedb"

CHAT_MODEL_ID = "llama3.2:3b"
EMBEDDING_MODEL_ID = "nomic-embed-text"
EMBEDDING_DIMENSIONS = 768
VECTOR_TABLE_NAME = "atlas_qualite"
MAX_SEARCH_RESULTS = 5
