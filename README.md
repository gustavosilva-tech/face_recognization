# face_recognization

This project consists of facial recognition using the DeepFace library in Python. The goal is to compare two images of faces and determine if they belong to the same person, using artificial intelligence models already trained for this task.

# How the project works

Image loading: The system receives two input images, usually photographs of faces, which can be stored on the computer or obtained from the internet.

Processing with DeepFace: The verify function of the DeepFace library is used, which automatically:

Detects and crops the face in the images.

Extracts facial features (embeddings) using state-of-the-art deep learning models such as VGG-Face, Facenet, ArcFace, among others.

Compares these features to calculate the similarity between faces.

Result: The programme returns whether the images are of the same person or different people, with a degree of confidence. It can also provide the distance between faces (the smaller the distance, the more similar they are).

# Practical applications
Security and authentication: Can be used to validate a user's identity when accessing a system.

Access control: Automatic identification in physical or digital systems.

Educational projects: Demonstration of computer vision and applied artificial intelligence.

# Advantages of DeepFace
Ease of use: There is no need to train models from scratch, as DeepFace already comes with pre-trained, ready-to-use models.

Versatility: In addition to facial recognition, it allows you to analyse age, gender, emotions and ethnicity in face images.

High accuracy: The models used achieve levels of accuracy comparable to human recognition in facial identification tasks.

Example of how it works
The user places two images in the project folder.

The Python script reads these images and executes:

from deepface import DeepFace
result = DeepFace.verify(‘img1.jpg’, ‘img2.jpg’)

The result indicates whether the images are of the same person.