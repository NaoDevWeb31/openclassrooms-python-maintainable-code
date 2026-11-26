"""
Chapitre 3 : Créez des fonctions flexibles avec le design pattern Décorateur.

Ce fichier illustre l'utilisation du design pattern Décorateur
dont la complexité modérée facilite la création de nombreuses fonctions
qui accomplissent des choses similaires.
"""


# Le pattern Décorateur
def decorate_function(function):
    """Cette fonction va générer le décorateur."""

    def wrapper():
        """Voici le "vrai" décorateur.

        C'est ici que l'on change la fonction de base
        en rajoutant des choses avant et après.
        """
        print("Do something at the start")

        result = function()

        print("Do something at the end")

        return result

    return wrapper


def travelling_through_the_stars():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")


# ici, nous allons récupérer le retour de "decorate_function",
# qui n'est autre que la fonction "wrapper" !
# Notez que nous pouvons très bien renommer une fonction en
# l'assignant dans une nouvelle variable (ici "wrapper" devient "decorated").
decorated = decorate_function(travelling_through_the_stars)
decorated()  # nous exécutons la fonction "wrapper"


# La syntaxe Décorateur
#
# L’interpréteur Python va exécuter la fonction décorateur
# lors du lancement du code et passer la fonction décorée
# en paramètre de son appel
def decorate_function_2(function):
    """Cette fonction va générer le décorateur."""

    def wrapper():
        """Le "vrai" décorateur."""
        print("Do something at the start")
        result = function()
        print("Do something at the end")
        return result

    return wrapper


@decorate_function_2  # c'est ici que ça se passe !
def travelling_through_the_stars_2():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")


# la fonction est directement décorée, et s'utilise comme telle, comme si rien
# comme si rien n'avait changé ! ;)
travelling_through_the_stars_2()
