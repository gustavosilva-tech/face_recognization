from deepface import DeepFace

# Caminhos das imagens a comparar
img1_path = "img1.jpg"
img2_path = "img2.jpg"

# Verificar se são a mesma pessoa
result = DeepFace.verify(img1_path, img2_path)

if result["verified"]:
    print("As imagens são da MESMA pessoa.")
else:
    print("As imagens são de pessoas DIFERENTES.")
