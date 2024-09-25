<!-- Auto-generated content start -->
# pinnacle_transformers

Transformers is a popular AI framework, and we have incorporated native support for Transformers to provide essential Large Language Model (LLM) capabilities.

Pinnacle allows users to work with arbitrary transformers pipelines, with custom input/ output data-types.


## Installation

```bash
pip install pinnacle_transformers
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/transformers)
- [API-docs](/docs/api/plugins/pinnacle_transformers)

| Class | Description |
|---|---|
| `pinnacle_transformers.model.TextClassificationPipeline` | A wrapper for ``transformers.Pipeline``. |
| `pinnacle_transformers.model.LLM` | LLM model based on `transformers` library. |


## Examples

### TextClassificationPipeline

```python
from pinnacle_transformers.model import TextClassificationPipeline

model = TextClassificationPipeline(
    identifier="my-sentiment-analysis",
    model_name="distilbert-base-uncased",
    model_kwargs={"num_labels": 2},
    device="cpu",
)
model.predict("Hello, world!")
```

### LLM

```python
from pinnacle_transformers import LLM
model = LLM(identifier="llm", model_name_or_path="facebook/opt-125m")
model.predict("Hello, world!")
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
## Training Example
Read more about this [here](https://docs.pinnacle.io/docs/templates/llm_finetuning)
