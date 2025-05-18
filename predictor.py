from torchvision import transforms
from PIL import Image
import torch
from model_loader import model, device

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def predict_image(image: Image.Image) -> dict:
    image = image.convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        prob = torch.sigmoid(output).item()

    return {
        "probability": round(prob, 4),
        "result": "Likely Glaucoma" if prob >= 0.5 else "Likely Healthy"
    }


