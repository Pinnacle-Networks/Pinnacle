import dataclasses as dc
import os
import typing as t

import anthropic
from anthropic import APIConnectionError, APIError, APIStatusError, APITimeoutError
from pinnacle.base.query_dataset import QueryDataset
from pinnacle.components.model import APIBaseModel
from pinnacle.misc.retry import Retry
from pinnacle.misc.utils import format_prompt

retry = Retry(
    exception_types=(APIConnectionError, APIError, APIStatusError, APITimeoutError)
)

KEY_NAME = 'ANTHROPIC_API_KEY'


class Anthropic(APIBaseModel):
    """Anthropic predictor.

    :param client_kwargs: The keyword arguments to pass to the client.
    """

    client_kwargs: t.Dict[str, t.Any] = dc.field(default_factory=dict)

    def postinit(self):
        """Post-initialization method."""
        self.model = self.model or self.identifier
        super().postinit()

    def setup(self, db=None):
        """Initialize the model.

        :param db: The database to use.
        """
        self.client = anthropic.Anthropic(
            api_key=os.environ[KEY_NAME], **self.client_kwargs
        )
        super().setup(db=db)


class AnthropicCompletions(Anthropic):
    """Cohere completions (chat) predictor.

    :param prompt: The prompt to use to seed the response.

    Example:
    -------
    >>> from pinnacle_anthropic.model import AnthropicCompletions
    >>>
    >>> model = AnthropicCompletions(
    >>>     identifier="claude-2.1",
    >>>     predict_kwargs={"max_tokens": 64},
    >>> )
    >>> model.predict_batches(["Hello, world!"])

    """

    prompt: str = ''

    @retry
    def predict(
        self,
        X: t.Union[str, list[dict]],
        context: t.Optional[t.List[str]] = None,
        **kwargs,
    ):
        """Generate text from a single input.

        :param X: The input to generate text from.
        :param context: The context to use for the prompt.
        :param kwargs: The keyword arguments to pass to the prompt function and
                        the llm model.
        """
        if isinstance(X, str):
            if context is not None:
                X = format_prompt(X, self.prompt, context=context)
            messages = [{'role': 'user', 'content': X}]

        elif isinstance(X, list) and all(isinstance(p, dict) for p in X):
            messages = X

        else:
            raise ValueError(
                f'Invalid input: {X}, only support str or messages format data'
            )
        message = self.client.messages.create(
            messages=messages,
            model=self.model,
            **{**self.predict_kwargs, **kwargs},
        )
        return message.content[0].text

    def predict_batches(self, dataset: t.Union[t.List, QueryDataset]) -> t.List:
        """Predict the embeddings of a dataset.

        :param dataset: The dataset to predict the embeddings of.
        """
        return [self.predict(dataset[i]) for i in range(len(dataset))]
