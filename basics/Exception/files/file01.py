def exception_demo():
    data_dict = {"numbers": [10, 5, 0]}
    num_list = [1, 2, 3]

    try:
        # 1. ZeroDivisionError (division par zéro)
        print("Division by zero example:")
        a = data_dict["numbers"][0] / data_dict["numbers"][2]

        # 2. KeyError (clé manquante dans dictionnaire)
        print("\nKeyError example:")
        missing = data_dict["missing_key"]

        # 3. IndexError (index hors limites dans liste)
        print("\nIndexError example:")
        out = num_list[5]

        # 4. ValueError (conversion incorrecte)
        print("\nValueError example:")
        val = int("not_an_int")

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    else:
        print("Aucune exception — toutes les opérations ont réussi.")
    finally:
        print("\nFin de l'exécution de exception_demo() — (finally exécuté quoiqu'il arrive)")

# Appel de la fonction pour démonstration
exception_demo()
