import os
import glob
import pandas as pd
from pinnacledb import pinnacle
from pinnacledb.container.document import Document as D
from pinnacledb.container.listener import Listener
from pinnacledb.container.vector_index import VectorIndex
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.ext.openai.model import OpenAIChatCompletion, OpenAIEmbedding

from ..config import Settings
from .utils import contextualize

def setup_qa_documentation(mongodb_client):
    db = pinnacle(mongodb_client.my_database_name)
    md_levels = 2
    content = []
    for level in range(1, md_levels):
       md_path = os.path.join(Settings.PATH_TO_REPO,*["*"]*level if level else '/', "*.md")
       for file in glob.glob(md_path):
           content.append(open(file).readlines())
        
    content = sum(content)
    content_df = pd.DataFrame({"text": content})
    df = contextualize(content_df, window_size=60, stride=17)

    documents = [D({"text": v}) for v in df["text"].values]

    db.execute(Collection("markdown").insert_many(documents))

    db.add(
        VectorIndex(
            identifier="documentation_index",
            indexing_listener=Listener(
                model=OpenAIEmbedding(model="text-embedding-ada-002"),
                key="text",
                select=Collection(name="markdown").find(),
            ),
        )
    )

    # Setup the chatbot into the database
    model = OpenAIChatCompletion(identifier='superbot', takes_context=True, model="gpt-3.5-turbo")
    db.add(model)
