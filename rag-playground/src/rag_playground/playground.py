import os

from dotenv import load_dotenv
import voyageai
import numpy as np

load_dotenv()

client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

frases = [
    "el gato duerme en el sofá",
    "el felino descansa en el mueble",
    "el clima en Madrid está soleado",
]

result = client.embed(frases, model="voyage-4", input_type="document")

for frase, vector in zip(frases, result.embeddings):
    print(f"\nFrase: {frase}")
    print(f"Dimensiones del vector: {len(vector)}")
    print(f"Primeros 5 valores: {vector[:5]}")

def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    v1 = np.array(1)
    v2 = np.array(2)

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

embeddings = result.embeddings

print("\n--- Similarity between sentences ---")
print(f"Cat vs Feline: {cosine_similarity(embeddings[0], embeddings[1]):.4f}")
print(f"Cat vs Weather: {cosine_similarity(embeddings[0], embeddings[2]):.4f}")
print(f"Feline vs Weather: {cosine_similarity(embeddings[1], embeddings[2]):.4f}")

