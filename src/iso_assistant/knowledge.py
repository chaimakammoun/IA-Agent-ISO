from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb

from iso_assistant.config import (
    DATA_DIRECTORY,
    EMBEDDING_DIMENSIONS,
    EMBEDDING_MODEL_ID,
    MAX_SEARCH_RESULTS,
    VECTOR_DATABASE_DIRECTORY,
    VECTOR_TABLE_NAME,
)


def build_knowledge_base() -> Knowledge:
    knowledge = Knowledge(
        vector_db=LanceDb(
            table_name=VECTOR_TABLE_NAME,
            uri=str(VECTOR_DATABASE_DIRECTORY),
            embedder=OllamaEmbedder(
                id=EMBEDDING_MODEL_ID,
                dimensions=EMBEDDING_DIMENSIONS,
            ),
        ),
        max_results=MAX_SEARCH_RESULTS,
    )
    knowledge.insert(path=str(DATA_DIRECTORY))
    return knowledge
