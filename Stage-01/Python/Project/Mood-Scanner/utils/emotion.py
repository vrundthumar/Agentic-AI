from deepface import DeepFace
import cv2

def detect_emotion(image):
    try:
        result = DeepFace.analyze(
            image,
            actions=["emotion"],
            enforce_detection=False
        )
        return result[0]["dominant_emotion"]
    except:
        return "No face detected"
