---
sidebar_label: Compute features
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<!-- TABS -->
# Compute features


<Tabs>
    <TabItem value="Text" label="Text" default>
        ```python
        
        key = 'txt'
        
        import sentence_transformers
        from pinnacledb import vector, Listener
        from pinnacledb.ext.sentence_transformers import SentenceTransformer
        
        pinnaclemodel = SentenceTransformer(
            identifier="embedding",
            object=sentence_transformers.SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"),
            datatype=vector(shape=(384,)),
            postprocess=lambda x: x.tolist(),
        )
        
        jobs, listener = db.apply(
            Listener(
                model=pinnaclemodel,
                select=select,
                key=key,
                identifier="features"
            )
        )        
        ```
    </TabItem>
    <TabItem value="Image" label="Image" default>
        ```python
        
        key = 'image'
        
        import torchvision.models as models
        from torchvision import transforms
        from pinnacledb.ext.torch import TorchModel
        from pinnacledb import Listener
        from PIL import Image
        
        class TorchVisionEmbedding:
            def __init__(self):
                # Load the pre-trained ResNet-18 model
                self.resnet = models.resnet18(pretrained=True)
                
                # Set the model to evaluation mode
                self.resnet.eval()
                
            def preprocess(self, image_array):
                # Preprocess the image
                image = Image.fromarray(image_array.astype(np.uint8))
                preprocess = preprocess = transforms.Compose([
                    transforms.Resize(256),
                    transforms.CenterCrop(224),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
                tensor_image = preprocess(image)
                return tensor_image
                
        model = TorchVisionEmbedding()
        pinnaclemodel = TorchModel(identifier='my-vision-model-torch', object=model.resnet, preprocess=model.preprocess, postprocess=lambda x: x.numpy().tolist())
        
        jobs, listener = db.apply(
            Listener(
                model=pinnaclemodel,
                select=select,
                key=key,
                identifier="features"
            )
        )        
        ```
    </TabItem>
    <TabItem value="Text-And-Image" label="Text-And-Image" default>
        ```python
        import torch
        import clip
        from torchvision import transforms
        from pinnacledb import ObjectModel
        from pinnacledb import Listener
        
        import torch
        import clip
        from PIL import Image
        
        key={'txt': 'txt', 'image': 'image'}
        
        class CLIPModel:
            def __init__(self):
                # Load the CLIP model
                self.device = "cuda" if torch.cuda.is_available() else "cpu"
                self.model, self.preprocess = clip.load("RN50", device=self.device)
        
            def __call__(self, text, image):
                with torch.no_grad():
                    text = clip.tokenize([text]).to(self.device)
                    image = self.preprocess(Image.fromarray(image.astype(np.uint8))).unsqueeze(0).to(self.device)
                    image_features = self.model.encode_image(image)[0].numpy().tolist()
                    text_features = self.model.encode_text(text)[0].numpy().tolist()
                return [image_features, text_features]
                
        model = CLIPModel()
        
        pinnaclemodel = ObjectModel(identifier="clip", object=model, signature="**kwargs", flatten=True, model_update_kwargs={"document_embedded": False})
        
        jobs, listener = db.apply(
            Listener(
                model=pinnaclemodel,
                select=select,
                key=key
                identifier="features"
            )
        )
        
        ```
    </TabItem>
    <TabItem value="Random" label="Random" default>
        ```python
        
        key = 'random'
        
        import numpy as np
        from pinnacledb import pinnacle, ObjectModel, Listener
        
        def random(*args, **kwargs):
            return np.random.random(1024).tolist()
        
        pinnaclemodel = ObjectModel(identifier="random", object=random)
        
        jobs, listener = db.apply(
            Listener(
                model=pinnaclemodel,
                select=select,
                key=key,
                identifier="features"
            )
        )        
        ```
    </TabItem>
    <TabItem value="Custom" label="Custom" default>
        ```python
        import numpy as np
        from pinnacledb import pinnacle, ObjectModel, Listener
        
        key = 'custom'
        
        # Define any feature calculation function
        def calc_fake_feature(input_data):
            fake_feature = list(range(10))
            return fake_feature
        
        pinnaclemodel = ObjectModel(identifier="fake_feature", object=calc_fake_feature)
        
        jobs, listener = db.apply(
            Listener(
                model=pinnaclemodel,
                select=select,
                # key of input_data
                key=key,
                identifier="features"
            )
        )        
        ```
    </TabItem>
</Tabs>
