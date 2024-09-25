<!-- Auto-generated content start -->
# pinnacle_sklearn

pinnacle allows users to work with arbitrary sklearn estimators, with additional support for pre-, post-processing and input/ output data-types.

## Installation

```bash
pip install pinnacle_sklearn
```

## API


- [Code](https://github.com/pinnacle-io/pinnacle/tree/main/plugins/sklearn)
- [API-docs](/docs/api/plugins/pinnacle_sklearn)

| Class | Description |
|---|---|
| `pinnacle_sklearn.model.SklearnTrainer` | A trainer for `sklearn` models. |
| `pinnacle_sklearn.model.Estimator` | Estimator model. |


## Examples

### Estimator

```python
from pinnacle_sklearn import Estimator
from sklearn.svm import SVC
model = Estimator(
    identifier='test',
    object=SVC(),
)
```


<!-- Auto-generated content end -->

<!-- Add your additional content below -->

## Training Example

Read more about this [here](https://docs.pinnacle.io/docs/templates/transfer_learning)
