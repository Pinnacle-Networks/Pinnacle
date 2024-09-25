<!-- Auto-generated content start -->
# pinnacle_openai

Pinnacle allows users to work with openai API models.

## Installation

```bash
pip install pinnacle_openai
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/openai)
- [API-docs](/docs/api/plugins/pinnacle_openai)

| Class | Description |
|---|---|
| `pinnacle_openai.model.OpenAIEmbedding` | OpenAI embedding predictor. |
| `pinnacle_openai.model.OpenAIChatCompletion` | OpenAI chat completion predictor. |
| `pinnacle_openai.model.OpenAIImageCreation` | OpenAI image creation predictor. |
| `pinnacle_openai.model.OpenAIImageEdit` | OpenAI image edit predictor. |
| `pinnacle_openai.model.OpenAIAudioTranscription` | OpenAI audio transcription predictor. |
| `pinnacle_openai.model.OpenAIAudioTranslation` | OpenAI audio translation predictor. |


## Examples

### OpenAIEmbedding

```python
from pinnacle_openai.model import OpenAIEmbedding
model = OpenAIEmbedding(identifier='text-embedding-ada-002')
model.predict('Hello, world!')
```

### OpenAIChatCompletion

```python
from pinnacle_openai.model import OpenAIChatCompletion
model = OpenAIChatCompletion(model='gpt-3.5-turbo', prompt='Hello, {context}')
model.predict('Hello, world!')
```

### OpenAIImageCreation

```python
from pinnacle_openai.model import OpenAIImageCreation

model = OpenAIImageCreation(
    model="dall-e",
    prompt="a close up, studio photographic portrait of a {context}",
    response_format="url",
)
model.predict("cat")
```

### OpenAIImageEdit

```python
import io

from pinnacle_openai.model import OpenAIImageEdit

model = OpenAIImageEdit(
    model="dall-e",
    prompt="A celebration party at the launch of {context}",
    response_format="url",
)
with open("test/material/data/rickroll.png", "rb") as f:
    buffer = io.BytesIO(f.read())
model.predict(buffer, context=["pinnacle"])
```

### OpenAIAudioTranscription

```python
import io
from pinnacle_openai.model import OpenAIAudioTranscription
with open('test/material/data/test.wav', 'rb') as f:
    buffer = io.BytesIO(f.read())
buffer.name = 'test.wav'
prompt = (
    'i have some advice for you. write all text in lower-case.'
    'only make an exception for the following words: {context}'
)
model = OpenAIAudioTranscription(identifier='whisper-1', prompt=prompt)
model.predict(buffer, context=['United States'])
```

### OpenAIAudioTranslation

```python
import io
from pinnacle_openai.model import OpenAIAudioTranslation
with open('test/material/data/german.wav', 'rb') as f:
    buffer = io.BytesIO(f.read())
buffer.name = 'test.wav'
prompt = (
    'i have some advice for you. write all text in lower-case.'
    'only make an exception for the following words: {context}'
)
e = OpenAIAudioTranslation(identifier='whisper-1', prompt=prompt)
resp = e.predict(buffer, context=['Emmerich'])
buffer.close()
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->
