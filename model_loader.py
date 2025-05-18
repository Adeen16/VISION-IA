import torch

from collections import OrderedDict

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    model = GlaucomaModel().to(device)
    state_dict = torch.load("models/glaucoma_model_best.pth", map_location=device)

    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        if k.startswith("resnet."):
            k = k.replace("resnet.", "base_model.")
        if "base_model.fc" in k:
            continue
        new_state_dict[k] = v

    model.load_state_dict(new_state_dict, strict=False)
    model.eval()
    return model

model = load_model()
