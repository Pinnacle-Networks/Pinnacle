---
sidebar_position: 3
---

# PyTorch

`pinnacle` allows users to work with arbitrary `torch` models, with custom pre-, post-processing and input/ output data-types,
as well as offering training with `pinnacle`


| Class | Description | GitHub | API-docs |
| --- | --- | --- | --- |
| `pinnacle.ext.torch.model.TorchModel` | Wraps a PyTorch model | [Code](https://github.com/pinnacle/pinnacle/blob/main/pinnacle/ext/torch/model.py) | [Docs](/docs/api/ext/torch/model#torchmodel-1) |
| `pinnacle.ext.torch.model.TorchTrainer` | May be attached to a `TorchModel` for training | [Code](https://github.com/pinnacle/pinnacle/blob/main/pinnacle/ext/torch/training.py) | [Docs](/docs/api/ext/torch/training#torchtrainer)