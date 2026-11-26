NUMBER_OF_GUEST = 15
WATER_PER_GUEST = 400
WATER_LEVEL = WATER_PER_GUEST * NUMBER_OF_GUEST
SPOONS_PER_GUEST = 2
MUSIC_VOLUME = 2
TIME_TO_WAIT = 2


def serve_group_of_two():
    """Sert un groupe de deux clients affamés.

    S'assure d'une expérience inoubliable !
    """
    greet_guests()
    table_number = prepare_table(NUMBER_OF_GUEST)
    for guest in range(NUMBER_OF_GUEST):
        lay_spoons_on_table(SPOONS_PER_GUEST)

    lead_customers_to_table(table_number)
    fill_water_carafe(WATER_LEVEL)
    adjust_music_volume(MUSIC_VOLUME)
    present_menus(NUMBER_OF_GUEST)

    wait_minutes(TIME_TO_WAIT)

    drinks_order = take_order(table_number)
    process_order(drinks_order)
    # ...
    present_bill()
    thank_guests()


def greet_guests():
    print("Bienvenue !")


def prepare_table(guests):
    print(f"Nous servons une table pour {guests}")
    return 10


def lay_spoons_on_table(spoons):
    print(f"Nous servons {spoons} cuillères.")


def lead_customers_to_table(table_number):
    print(f"Venez à la table {table_number} !")


def fill_water_carafe(water_level):
    print(f"Nous vous servons {water_level} ml d'eau.")


def adjust_music_volume(level):
    print(f"Nous mettons le volume à {level}.")


def present_menus(number):
    print(f"Nous présentons {number} menus.")


def wait_minutes(minutes):
    print(f"--- attente de {minutes} minutes ---")


def take_order(number):
    print(f"Nous prenons la commande de la table {number}.")
    return "Bouteille de vin"


def process_order(drinks_order):
    print("Nous allons chercher les boissons !")


def present_bill():
    print("Nous présentons l'addition.")


def thank_guests():
    print("Nous remercions les invités !")


if __name__ == "__main__":
    serve_group_of_two()
