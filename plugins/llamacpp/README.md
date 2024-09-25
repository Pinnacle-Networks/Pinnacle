<!-- Auto-generated content start -->
# pinnacle_llamacpp

Pinnacle allows users to work with self-hosted LLM models via [Llama.cpp](https://github.com/ggerganov/llama.cpp).

## Installation

```bash
pip install pinnacle_llamacpp
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/llamacpp)
- [API-docs](/docs/api/plugins/pinnacle_llamacpp)

| Class | Description |
|---|---|
| `pinnacle_llamacpp.model.LlamaCpp` | Llama.cpp connector. |
| `pinnacle_llamacpp.model.LlamaCppEmbedding` | Llama.cpp connector for embeddings. |


## Examples

### LlamaCpp

```python
from pinnacle_llama_cpp.model import LlamaCpp

model = LlamaCpp(
    identifier="llm",
    model_name_or_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
)
model.predict("Hello world")
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
