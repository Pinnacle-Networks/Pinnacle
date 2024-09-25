<!-- Auto-generated content start -->
# pinnacle_jina

Pinnacle allows users to work with Jina Embeddings models through the Jina Embedding API.

## Installation

```bash
pip install pinnacle_jina
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/jina)
- [API-docs](/docs/api/plugins/pinnacle_jina)

| Class | Description |
|---|---|
| `pinnacle_jina.client.JinaAPIClient` | A client for the Jina Embedding platform. |
| `pinnacle_jina.model.Jina` | Cohere predictor. |
| `pinnacle_jina.model.JinaEmbedding` | Jina embedding predictor. |


## Examples

### JinaEmbedding

```python
from pinnacle_jina.model import JinaEmbedding
model = JinaEmbedding(identifier='jina-embeddings-v2-base-en')
model.predict('Hello world')
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
