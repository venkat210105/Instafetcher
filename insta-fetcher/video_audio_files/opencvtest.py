import os
import cv2
from PIL import Image
import torch
from torchvision import transforms
from torchvision.models import resnet50, ResNet50_Weights

# Initialize the video capture
video_path = r"D:\hackathon\video_audio_files\instagram_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(f"Unable to open video file: {video_path}")

# Define frame extraction interval
frame_interval = 100  # Extract every 100th frame

# Load ResNet50 model with ImageNet weights
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

# Load ImageNet labels from the weights metadata
imagenet_labels = weights.meta['categories']

# Transformation to preprocess images for ResNet
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Output directory
output_dir = r"D:\hackathon\insta-fetcher\output_images"
os.makedirs(output_dir, exist_ok=True)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        # Convert the frame to a PIL image
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Preprocess the image
        img_tensor = transform(img).unsqueeze(0)

        # Predict category using the model
        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted = outputs.max(1)

        # Map prediction to class label
        label_name = imagenet_labels[predicted.item()]

        # Construct the output filename with the predicted label
        label = f"frame_{frame_count}_category_{label_name}.jpg"
        output_path = os.path.join(output_dir, label)

        # Save the frame to the specified directory
        cv2.imwrite(output_path, frame)
        print(f"Processed frame {frame_count}, saved as {label}")

        # Clear tensors from memory
        del img_tensor, outputs
        torch.cuda.empty_cache()

    frame_count += 1

# Release the video capture
cap.release()
print("Processing complete!")
