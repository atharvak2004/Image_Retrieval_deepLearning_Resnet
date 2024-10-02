from flask import Flask, request, render_template
import os
import numpy as np
from pathlib import Path
from PIL import Image
from feature_extractor import FeatureExtractor
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Set path to save uploaded images and extracted features
UPLOAD_FOLDER = './static/uploaded_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the feature extractor
fe = FeatureExtractor()

# Load pre-extracted feature vectors from saved .npy files
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))

features = np.array(features)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get uploaded image
        file = request.files['query_img']
        filename = file.filename
        
        # Save the image in the upload folder
        query_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(query_img_path)

        # Open the saved image for feature extraction
        img = Image.open(query_img_path)

        # Extract features from the query image
        query_features = fe.extract(img)

        # Calculate cosine similarity between the query and stored features
        similarities = cosine_similarity([query_features], features)

        # Get indices of the most similar images
        ranked_indices = np.argsort(similarities[0])[::-1]

        # Get top 5 similar image paths
        top_img_paths = [img_paths[idx] for idx in ranked_indices[:3]]

        # Use the relative path to the uploaded image for the template
        relative_query_img_path = os.path.relpath(query_img_path, './static')

        # Render the result page with the query image and top similar images
        return render_template('index.html', query_path=relative_query_img_path, result_paths=top_img_paths)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
