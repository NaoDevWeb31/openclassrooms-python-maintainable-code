"""
Chapitre 5 : Utilisez des linters pour que votre code reste propre.

Ce fichier illustre l'utilisation des linters et des autoformateurs pour
maintenir un code Python propre, lisible et cohérent.

Flake8 permet de détecter les problèmes de style et certaines erreurs
de code, tandis que Black permet de corriger automatiquement les
problèmes de formatage.
"""

# Avant correction : erreurs de style détectées par Flake8
# fmt: off
def say_hello( name = "John" ):
    print( f"Bonjour { name } !")
say_hello( "Martin" )
# fmt: on


# Après correction automatique avec Black
def say_hello(name="John"):
    print(f"Bonjour { name } !")


say_hello("Martin")
