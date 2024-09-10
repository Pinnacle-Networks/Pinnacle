from pinnacle.vector_search.atlas import MongoAtlasVectorSearcher
from pinnacle.vector_search.in_memory import InMemoryVectorSearcher
from pinnacle.vector_search.lance import LanceVectorSearcher
from pinnacle.vector_search.qdrant import QdrantVectorSearcher

vector_searcher_implementations = {
    "lance": LanceVectorSearcher,
    "in_memory": InMemoryVectorSearcher,
    "mongodb+srv": MongoAtlasVectorSearcher,
    "qdrant": QdrantVectorSearcher,
}
