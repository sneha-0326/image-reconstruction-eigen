import numpy as np
from PIL import Image

def load_image(path):
    img = Image.open(path).convert('L')
    img = img.resize((256, 256))
    A = np.array(img, dtype=float)

    # Optional normalization
    A = A / 255.0

    return A