# dr_model.py
import torch
from torchvision import transforms
from PIL import Image
from app.dr_model_arch import DRModel
  # Adjust based on your path

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DRModel()
model.load_state_dict(torch.load("models/efficientnet_b4_dr.pth", map_location=device))
model.to(device)
model.eval()


# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Define classes
classes = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

def predict_dr(image: Image.Image) -> str:
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return classes[predicted.item()]
