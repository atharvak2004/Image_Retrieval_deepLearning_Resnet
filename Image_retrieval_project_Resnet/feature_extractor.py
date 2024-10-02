from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import numpy as np

class FeatureExtractor:
    def __init__(self):
        # Load the ResNet50 model with pretrained weights
        base_model = ResNet50(weights='imagenet')
        # Extract features from the 'avg_pool' layer (before the dense layers)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

    def extract(self, img):
        """
        Extract deep features from an input image.
        Args:
            img: from PIL.Image.open(path) or tensorflow.keras.preprocessing.image.load_img(path)

        Returns:
            feature (np.ndarray): deep feature with the shape=(2048,)
        """
        img = img.resize((224, 224))  # ResNet50 requires 224x224 input images
        img = img.convert('RGB')  # Ensure the image is in RGB
        x = image.img_to_array(img)  # Convert to np.array (height x width x channels)
        x = np.expand_dims(x, axis=0)  # Expand dimensions for batch size (1, h, w, c)
        x = preprocess_input(x)  # Preprocess using ResNet50 specific preprocessing
        feature = self.model.predict(x)[0]  # Extract the feature
        return feature / np.linalg.norm(feature)  # Normalize the feature vector
