# offline.py

import numpy as np
from pathlib import Path
from PIL import Image
from feature_extractor import FeatureExtractor

# Initialize the feature extractor
fe = FeatureExtractor()

# Path to the images you want to process
image_dir = Path("./static/img")
# Path to save the features
feature_dir = Path("./static/feature")
feature_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

# Iterate through all images in the specified directory
for img_path in image_dir.glob("*.jpg"):  # Adjust the glob pattern as necessary
    img = Image.open(img_path)  # Load the image
    features = fe.extract(img)  # Extract features

    # Save features to a .npy file
    feature_file = feature_dir / f"{img_path.stem}.npy"
    np.save(feature_file, features)

    print(f"Processed {img_path.name} and saved features to {feature_file.name}")
