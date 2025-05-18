# dr_model_arch.py
import torch.nn as nn
import timm

class DRModel(nn.Module):
    def __init__(self, num_classes=5):
        super(DRModel, self).__init__()
        # Use timm to create the exact same model class used during training
        self.base_model = timm.create_model('efficientnet_b4', pretrained=False, num_classes=num_classes)

    def forward(self, x):
        return self.base_model(x)
