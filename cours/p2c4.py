"""
Chapitre 4 : Écrivez du code Python antibug.

Ce fichier illustre les recommandations de la PEP 8 pour écrire du code Python
antibug.
"""


# Soit toutes les instructions return retournent une expression,
# soit aucune ne le fait.
# Privilégier des types de retour cohérents et prévisibles.
# Retourner explicitement None lorsque cela est nécessaire.
def less_confusing_division(top, bottom):
    """Effectue une division exacte entre deux nombres non nuls.

    Retourne None si l'un des nombres est nul ou si la division
    n'est pas exacte.
    """
    if bottom == 0 or top == 0:
        # plutôt qu’un return nu, on retourne explicitement None
        return None

    if top % bottom != 0:
        return None

    return top / bottom


# Écrire des chaînes cohérentes => maintenable, lisible et pythonique
phone_number = "01234567890"
MY_START_PHONE_NUMBER = "01234"

# tranchage de chaîne phone_number[:5] => startswith(constante)
if phone_number.startswith(MY_START_PHONE_NUMBER):
    print("Of course!")
if phone_number.endswith("7890"):
    print("Verily!")
if "345" in phone_number:
    print("Affirmative!")

# Simplifiez les exceptions => écrire un message d’erreur pertinent
letters = ["a", "b", "c", "d", "e"]
length = len(letters)

while True:
    # Le bloc try doit couvrir le moins de code possible
    try:
        message = (
            f"Tapez un index de 0 à {length - 1} pour accéder à l'élément : "
        )
        index = int(input(message))
        print("Vous accédez à l'élément", letters[index])
    # N’utilisez jamais la clause except nue
    except IndexError:
        raise
    except ValueError:
        raise ValueError("Entrée invalide. Veuillez entrer un nombre.")
    except Exception as e:
        print(e)
    break


def get_number():
    """Get a number input and return its value."""
    choice = input("Sélectionnez un nombre : ")

    try:
        number = int(choice)
        return number
    except ValueError:
        print(f"{choice} n'est pas un nombre ! On retourne None.")
        return None


number = get_number()
print("Le nombre est", number)
