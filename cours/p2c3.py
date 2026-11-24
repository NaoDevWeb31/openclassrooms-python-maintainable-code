"""
Chapitre 3 : Écrivez du code Python facile à lire.

Ce fichier illustre des règles de base de la PEP 8: l'indentation,
les espaces, les sauts de ligne et la longueur des lignes.
"""


# Bon code, selon la PEP 8
#
# Un espace autour des opérateurs d'affectation et des opérateurs
# logiques, sauf notamment pour les valeurs par défaut des paramètres
# non annotés, sans espace autour du signe égal.
# Pas d'espace immédiatement après une parenthèse ou un crochet
# ouvrant, ni avant une parenthèse ou un crochet fermant.
# Pas d'espace entre le nom d'une fonction et sa parenthèse ouvrante.
# Un espace après les mots-clés if/for.
def protect_animals(animals, sanctuary="little farm", max_places=4):
    """Place les animaux donnés dans un sanctuaire."""
    is_little = "little" in sanctuary

    if max_places < 5 or is_little:
        print("C'est petit, mais c'est mieux que rien !")

    protected = animals[:max_places]
    print(f"Nous avons protégé ces animaux : {protected}")


animals = ["cochon", "poule", "cerf", "lapin", "chien"]
protect_animals(animals)


# Mauvais code, selon la PEP 8.
# fmt: off
def protect_animals(animals,sanctuary = "little farm",max_places = 4):
    is_little="little" in sanctuary

    if max_places<5 or(is_little):
        print( "C'est petit, mais c'est mieux que rien !" )

    protected=animals[ : max_places]
    print( f"Nous avons protégé ces animaux : { protected }" )

animals = [ "cochon","poule","cerf","lapin","chien" ]
protect_animals( animals )
# fmt: on


# Un paramètre par ligne, et la parenthèse au même niveau d’indentation
# que la fonction
def function_with_a_rather_long_name(
    parameter_number_1,
    parameter_number_2,
    parameter_number_3,
):  # Exemple illustratif supposant l'existence de my_function.
    my_function(parameter_number_1)  # type: ignore  # noqa: F821
    return parameter_number_2


# chaînes de caractères trop longues: une parenthèse +
# plusieurs petites chaînes de caractères à l’intérieur +
# un saut de ligne par chaîne de caractères
super_long_password = (
    "erfzfefrzvterbytnrezrtvbytyruetrgtrth"
    "zeergvzreafz'((-'eg'((yhvgbrz'trvytrh"
    "zerbetrtzbrtyezegbyebzrtbrebrtberbtrg"
    "zevrebtniukoy;i;yu,yt,trntehtrgegretr"
)
