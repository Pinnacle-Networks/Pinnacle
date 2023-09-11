'''
INSERT SUMMARY ON THIS MODULE HERE
'''

from backend.config import settings

from pinnacledb.container.listener import Listener
from pinnacledb.container.vector_index import VectorIndex
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.ext.openai.model import OpenAIChatCompletion, OpenAIEmbedding


def install_openai_chatbot(db):
    db.add(
        OpenAIChatCompletion(
            takes_context=True,
            prompt=settings.prompt,
            model=settings.qa_model,
        )
    )


def install_openai_vector_index(db, repo):
    db.add(
        VectorIndex(
            identifier=repo,
            indexing_listener=Listener(
                model=OpenAIEmbedding(model=settings.vector_embedding_model),
                key=settings.vector_embedding_key,
                select=Collection(name=repo).find(),
                predict_kwargs={'chunk_size': 100},
            ),
        )
    )


def install_ai_components(db):
    install_openai_chatbot(db)
    for repo in settings.default_repos:
        install_openai_vector_index(db, repo)
