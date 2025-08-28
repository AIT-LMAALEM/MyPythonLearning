
# 6. Filtrer selon plusieurs conditions
numbers = list(range(1, 11))
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print("Pairs et divisibles par 3 :", filtered)

# 7. Catégoriser selon la divisibilité
categories = [
    "Div2&3" if x % 2 == 0 and x % 3 == 0
    else "Div2" if x % 2 == 0
    else "Div3" if x % 3 == 0
    else "None"
    for x in numbers
]
print("Catégories :", categories)

# 8. Extraire noms avec note >= 85
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
top_students = [s['name'] for s in students if s['grade'] >= 85]
print("Top étudiants :", top_students)

# 9. Extraits d’un texte : mots débutant par voyelle
text = "The quick brown fox jumps over the lazy dog"
vowel_words = [w for w in text.split() if w[0].lower() in 'aeiou']
print("Mots commençant par voyelle :", vowel_words)

# 10. Générer triples pythagoriciens
triples = [
    (x, y, z)
    for x in range(1, 30)
    for y in range(x, 30)
    for z in range(y, 30)
    if x**2 + y**2 == z**2
]
print("Triples pythagoriciens :", triples[:5], "…")
