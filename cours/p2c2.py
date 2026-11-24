"""
Chapitre 2 : Écrivez du code Python qui s’explique tout seul.

Ce fichier illustre des règles de base de la PEP 8: les conventions de
nommage, les commentaires et les chaînes de documentation.
"""

# noms de variables: minuscules + underscores => snake_case
name = "Jeanne"
fuel_level = 100
famous_singers = ["Céline Dion", "Michael Jackson", "Edith Piaf"]

# variables constantes: majuscules + underscores => UPPER_SNAKE_CASE
DAYS_PER_WEEK = 7
PERSONAL_EMAIL = "myemail@email.com"


# noms de classe: majuscule au début de chaque mot
# sans séparateur => PascalCase
class JukeBox:
    pass


class SpaceShip:
    pass


# noms de modules: court + minuscules + underscores à éviter
# sauf pour lisibilité (exemples pris de la bibliothèque standard de Python)
import os
import sys
import shutil  # contraction de "shell" et "utilities"
import pathlib  # contraction de “path” et “lib”


# chaînes de documentation ou docstrings : chaînes de caractères
# placées au tout début d'une fonction, d'une classe ou d'un module
# pour documenter le code et permettre aux outils automatisés
# d'accéder à cette documentation
def multiply(first, second=1):
    """Multiplie deux nombres.

    Args:
        first -- le multiplicande
        second -- le multiplicateur (défaut 1)
    """
    return first * second


print(multiply(13, 77))
# accéder à la docstring de la fonction en utilisant l’attribut __doc__
print(multiply.__doc__)


def search_film(name):
    """Cherche un film selon un nom donné.

    Args:
        name (str): le nom utilisé pour la recherche.

    Returns:
        - un objet `film` si un film a été trouvé, ou None.
    """

    # Exemple illustratif supposant l'existence d'une classe Film.
    films = Film.filter_by_name(name)  # type: ignore  # noqa: F821
    if films:
        return films.pop(0)
    return None
