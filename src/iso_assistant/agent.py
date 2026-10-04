from agno.agent import Agent
from agno.models.ollama import Ollama
from iso_assistant.config import CHAT_MODEL_ID
from iso_assistant.instructions import AGENT_INSTRUCTIONS
from iso_assistant.knowledge import build_knowledge_base


def build_agent() -> Agent:
    return Agent(
        model=Ollama(id=CHAT_MODEL_ID),
        knowledge=build_knowledge_base(),
        add_knowledge_to_context=True,
        instructions=AGENT_INSTRUCTIONS,
    )
