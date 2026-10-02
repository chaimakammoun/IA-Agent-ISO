from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.vectordb.lancedb import LanceDb
from agno.agent import Agent
from agno.models.ollama import Ollama


def build_agent():
    knowledge = Knowledge(
        vector_db=LanceDb(
            table_name="atlas_qualite",
            uri="./lancedb",
            embedder=OllamaEmbedder(id="nomic-embed-text", dimensions=768),
        ),
        max_results=5,
    )

    knowledge.insert(path="data/")

    agent = Agent(
        model=Ollama(id="llama3.2:3b"),
        knowledge=knowledge,
        add_knowledge_to_context=True,
        instructions=[
            "Réponds uniquement à partir des documents trouvés dans la base de connaissances.",
            "Si l'information n'y figure pas, dis clairement que tu ne trouves pas de réponse.",
            "N'utilise que les informations qui répondent directement à la question posée. Ignore tout passage récupéré qui ne concerne pas le sujet exact de la question, même s'il semble lié.",
            "Ne cite que les références de document et de clause qui apparaissent explicitement dans le contexte récupéré. N'invente jamais un numéro de clause de mémoire.",
            "Termine ta réponse par une ligne 'Sources utilisées :' suivie de la liste des noms de fichiers réellement utilisés pour construire la réponse.",
            "Ne conclus JAMAIS qu'une entreprise ne respecte pas une exigence simplement parce que tu n'as pas trouvé l'information. Si tu ne trouves pas de document d'entreprise qui réponde à une clause, dis explicitement que ta recherche n'a pas trouvé de document pertinent, et précise que cela ne signifie pas que l'exigence n'est pas respectée dans la réalité — seulement qu'aucun document ne le confirme dans ta base.",
            "N'établis jamais de lien ou de relation entre deux clauses différentes sauf si ce lien est explicitement écrit dans le contexte récupéré.",
            "Sois concis : ne développe pas de phrases générales sur l'importance d'une exigence si cette information n'est pas dans le contexte récupéré. Si tu ne sais pas, dis-le en une phrase et arrête-toi là.",
            "La liste 'Sources utilisées' doit contenir UNIQUEMENT les fichiers dont tu as recopié ou reformulé le contenu dans ta réponse. Ne liste jamais un fichier simplement parce qu'il a été récupéré par la recherche.",
        ],
    )

    return agent
