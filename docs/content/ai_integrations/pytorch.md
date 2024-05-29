---
sidebar_position: 3
---

# PyTorch

`pinnacledb` allows users to work with arbitrary `torch` models, with custom pre-, post-processing and input/ output data-types,
as well as offering training with `pinnacledb`


| Class | Description | GitHub | API-docs |
| --- | --- | --- | --- |
| `pinnacledb.ext.torch.model.TorchModel` | Wraps a PyTorch model | [Code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/ext/torch/model.py) | [Docs](/docs/api/ext/torch/model#torchmodel-1) |
| `pinnacledb.ext.torch.model.TorchTrainer` | May be attached to a `TorchModel` for training | [Code](https://github.com/SuperDuperDB/pinnacledb/blob/main/pinnacledb/ext/torch/training.py) | [Docs](/docs/api/ext/torch/training#torchtrainer)