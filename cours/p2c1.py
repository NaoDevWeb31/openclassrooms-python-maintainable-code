"""
Chapitre 1 : Découvrez les conventions Python

Les 2 fonctions sont équivalentes pour l’ordinateur
"""


# noms de fonction et de variables qui n'aident pas beaucoup
def adjustment(value):
    return (value % 4 == 0) and (value % 100 != 0 or value % 400 == 0)


# version beaucoup plus adaptée et agréable pour des développeurs
# => voir en un coup d’œil ce que fait la fonction avec son nom clair
# et pas besoin de faire des nœuds au cerveau pour comprendre la logique
def is_leap_year(year):
    # Les années bissextiles sont toutes des multiples de 4
    if year % 4 != 0:
        return False

    # Les années séculaires ne sont pas bissextiles, hormis 1600, 2000, 2400,
    # etc.
    if year % 100 == 0:
        return year % 400 == 0

    # Tous les autres résultats sont vrais.
    return True
