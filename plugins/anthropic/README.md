<!-- Auto-generated content start -->
# pinnacle_anthropic

Pinnacle allows users to work with anthropic API models. The key integration is the integration of high-quality API-hosted LLM services.

## Installation

```bash
pip install pinnacle_anthropic
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/anthropic)
- [API-docs](/docs/api/plugins/pinnacle_anthropic)

| Class | Description |
|---|---|
| `pinnacle_anthropic.model.Anthropic` | Anthropic predictor. |
| `pinnacle_anthropic.model.AnthropicCompletions` | Cohere completions (chat) predictor. |


## Examples

### AnthropicCompletions

```python
from pinnacle_anthropic.model import AnthropicCompletions

model = AnthropicCompletions(
    identifier="claude-2.1",
    predict_kwargs={"max_tokens": 64},
)
model.predict_batches(["Hello, world!"])
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
