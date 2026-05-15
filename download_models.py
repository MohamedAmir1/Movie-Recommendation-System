import gdown
import os
import zipfile

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

FILES = {
    "svd_artefacts.pkl": "14aSJosAOjRApRG5IOfbPx3l9yIOIdYYr",
    "cosine_sim.pkl": "1oQoJBU5sF6-7DcyUhsHGBx0vSL3Aprfj",
    "movies.pkl": "1VR5vBKUGsFtQ6G7wainTWe6t_kMW5ywN",
    "ratings.pkl": "1Znhjb9bVEeB6za7FXm4dg1OfaNCiEKXu",
    "cb_data.pkl": "1JBFHI8TY6jyFIMhFkFH8gQOFO4bmlZ8a"
}

for filename, file_id in FILES.items():

    path = os.path.join(MODEL_DIR, filename)

    if not os.path.exists(path):

        url = f"https://drive.google.com/uc?id={file_id}"

        print(f"Downloading {filename}...")

        gdown.download(url, path, quiet=False)

print("All models downloaded into /models")
