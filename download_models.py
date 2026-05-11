import gdown
import os

FILES = {
    "svd_artefacts.pkl": "1HCQHa3sdpixJgXBQ4WoDEB-DDIkMH8RA",
    "cosine_sim.pkl": "15dh1qmFnqE23Gj-zJfcXbjbCASpHsojG",
    "movies.pkl": "1VR5vBKUGsFtQ6G7wainTWe6t_kMW5ywN",
    "ratings.pkl": "1Znhjb9bVEeB6za7FXm4dg1OfaNCiEKXu",
    "cb_data.pkl": "1JBFHI8TY6jyFIMhFkFH8gQOFO4bmlZ8a"
}

for filename, file_id in FILES.items():

    if not os.path.exists(filename):

        url = f"https://drive.google.com/uc?id={file_id}"

        print(f"Downloading {filename}...")

        gdown.download(url, filename, quiet=False)

print("All files downloaded.")