import cv2
import numpy as np
from insightface.app import FaceAnalysis

app = FaceAnalysis(name="buffalo_l")

app.prepare(ctx_id=0)

stored = np.load("my_face.npy")


def cosine_sim(a, b):
	return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def check():
	login_img = cv2.imread("login.png")

	faces = app.get(login_img)

	if faces:
		login_emb = faces[0].embedding

		score = cosine_sim(stored, login_emb)

		return score

	else:
		return 0
