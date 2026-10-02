# 🤖 Assistant Qualité ISO 9001 — RAG avec Ollama, Agno et Streamlit

Assistant IA permettant de poser des questions sur la **norme ISO 9001:2015** et sur les documents qualité d'une entreprise fictive de fabrication (**Atlas Composants**).

L'assistant utilise une approche **RAG (Retrieval-Augmented Generation)** pour rechercher les informations pertinentes dans les documents et générer une réponse avec **citation des sources**.

Le projet fonctionne **entièrement en local** grâce à Ollama.

---

## 🎯 Objectif

L'objectif est de faciliter la recherche d'informations liées à la qualité et à l'ISO 9001:2015.

Au lieu de rechercher manuellement une exigence dans plusieurs documents, l'utilisateur peut poser une question directement à l'assistant.

**Exemple :**

> Quelles sont les exigences concernant les audits internes ?

L'agent recherche les passages pertinents dans les documents disponibles et fournit une réponse accompagnée de ses sources.

---

## 🏗️ Architecture

```text
Question utilisateur
        │
        ▼
Recherche RAG vectorielle
        │
        ▼
LanceDB + Embeddings
(nomic-embed-text)
        │
        ▼
Agent Agno + Ollama
(llama3.2:3b)
        │
        ▼
Réponse avec sources
        │
        ▼
Interface Streamlit


⚙️ Installation

1. Cloner le repository:

git clone https://github.com/chaimakammoun/IA-Agent-ISO.git

cd IA-Agent-ISO

2. Installer les dépendances:

Installer les bibliothèques Python nécessaires au projet.

3. Installer Ollama:

Installer Ollama puis télécharger les modèles utilisés :

ollama pull llama3.2:3b

ollama pull nomic-embed-text


▶️ Lancer l'application

streamlit run app.py

L'application sera ensuite accessible depuis le navigateur via l'interface Streamlit.