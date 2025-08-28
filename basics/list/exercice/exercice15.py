import math

while True:
    print("\nOpérations disponibles :")
    print(" + , - , * , / , ** (puissance), sqrt (racine carrée), log (logarithme base n), ln (log naturel), sin, cos, tan")
    op = input("Entrez l'opérateur (ou 'q' pour quitter) : ").strip().lower()
    if op == 'q':
        print("Fin du programme.")
        break

    a = float(input("Premier nombre : "))

    if op in ['sqrt', 'ln', 'log', 'sin', 'cos', 'tan']:
        if op == 'sqrt':
            result = math.sqrt(a)
        elif op == 'ln':
            result = math.log(a)
        elif op == 'sin':
            result = math.sin(math.radians(a))
        elif op == 'cos':
            result = math.cos(math.radians(a))
        elif op == 'tan':
            result = math.tan(math.radians(a))
        elif op == 'log':
            b = float(input("Base du logarithme : "))
            result = math.log(a, b)
    else:
        b = float(input("Deuxième nombre : "))
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        elif op == '**':
            result = a ** b
        else:
            print("Opérateur non reconnu.")
            continue

    print("Résultat :", result)
