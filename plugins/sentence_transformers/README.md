<!-- Auto-generated content start -->
# pinnacle_sentence_transformers

pinnacle allows users to work with self-hosted embedding models via [Sentence-Transformers](https://sbert.net).

## Installation

```bash
pip install pinnacle_sentence_transformers
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/sentence_transformers)
- [API-docs](/docs/api/plugins/pinnacle_sentence_transformers)

| Class | Description |
|---|---|
| `pinnacle_sentence_transformers.model.SentenceTransformer` | A model for sentence embeddings using `sentence-transformers`. |


## Examples

### SentenceTransformer

```python
from pinnacle import vector
from pinnacle_sentence_transformers import SentenceTransformer
import sentence_transformers
model = SentenceTransformer(
    identifier="embedding",
    object=sentence_transformers.SentenceTransformer("BAAI/bge-small-en"),
    datatype=vector(shape=(1024,)),
    postprocess=lambda x: x.tolist(),
    predict_kwargs={"show_progress_bar": True},
)
model.predict("What is pinnacle")
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
