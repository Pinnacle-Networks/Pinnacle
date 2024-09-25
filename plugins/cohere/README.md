<!-- Auto-generated content start -->
# pinnacle_cohere

Pinnacle allows users to work with cohere API models.

## Installation

```bash
pip install pinnacle_cohere
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/cohere)
- [API-docs](/docs/api/plugins/pinnacle_cohere)

| Class | Description |
|---|---|
| `pinnacle_cohere.model.Cohere` | Cohere predictor. |
| `pinnacle_cohere.model.CohereEmbed` | Cohere embedding predictor. |
| `pinnacle_cohere.model.CohereGenerate` | Cohere realistic text generator (chat predictor). |


## Examples

### CohereEmbed

```python
from pinnacle_cohere.model import CohereEmbed
model = CohereEmbed(identifier='embed-english-v2.0', batch_size=1)
model..predict('Hello world')
```

### CohereGenerate

```python
from pinnacle_cohere.model import CohereGenerate
model = CohereGenerate(identifier='base-light', prompt='Hello, {context}')
model.predict('', context=['world!'])
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
