
# 1. Transformer une liste de mots en majuscules
words = ["python", "list", "comprehension", "advanced"]
uppercased = [word.upper() for word in words]
print("Majuscules :", uppercased)

# 2. Remplacer les nombres pairs par "even", les autres par "odd"
numbers = list(range(1, 11))
even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
print("Pair ou impair :", even_odd)

# 3. Aplatir une matrice 2D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Aplatit :", flattened)

# 4. Transposer la matrice
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposée :", transposed)

# 5. Coordonnées du produit cartésien
coords = [(x, y) for x in range(3) for y in range(3)]
print("Coordonnées (produit cartésien) :", coords)
