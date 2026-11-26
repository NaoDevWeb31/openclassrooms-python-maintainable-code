"""
Chapitre 4: Structurez une application avec le pattern d'architecture MVC.

Ce fichier illustre comment structurer une application entière
avec le pattern d'architecture Model-View-Controller ou Modèle-Vue-Contrôleur

"""

from datetime import datetime

# ---------------------------------
# Le Modèle (M)
#
# Les informations relatives à l’état y sont conservées dans les classes.
# Ce sont les éléments qui sont vus et manipulés.

PRICE_PER_SONG = 1.20


class Song:
    """Modèle représentant un son."""

    def __init__(self, name, artist, genre, artwork):
        """Initialise les détails relatifs au son."""
        self.artist = artist
        self.name = name
        self.genre = genre
        self.artwork = artwork


class Library:
    """Modèle qui stocke les sons."""

    def __init__(self):
        """Initialise une liste de sons."""
        self.songs = []


class ServiceInfo:
    """Modèle qui gère la maintenance de la jukebox."""

    def __init__(self, status, engineer_name):
        """Initialise les détails du service."""
        self.service_date = datetime.now()
        self.status = status
        self.engineer = engineer_name


# ---------------------------------
# La Vue (V)
#
# La façon dont le modèle est présenté à l’utilisateur
# et dont il interagit avec lui.
# C’est l’élément qui est le plus susceptible de changer.
# Le nom générique donné à toutes les composantes du système
# qui assurent l’interface avec l’utilisateur.

class Touchscreen:
    """Vue qui gère l'interface de la jukebox."""

    def select_song(self):
        """Sélectionne un son."""
        pass

    def prompt_for_next_song(self, songs):
        """Demande un nouveau son."""
        for song in songs:
            # affiche les sons
            pass
        return "Dark Chest of Wonders"


class Speakers:
    """Vue qui gère le son."""

    def __init__(self):
        """Initialise le volume."""
        self.volume = 5

    def get_louder(self):
        """Augmente le volume."""
        self.volume += 1

    def get_quieter(self):
        """Baisse le volume."""
        self.volume -= 1

    def play_song(self, song):
        """Joue la musique."""
        pass


class CoinSlot:
    """Vue qui gère la reception de l'argent."""

    def __init__(self, amount):
        """Initialise le montant."""
        self.amount = amount

    def request_money(self, amount):
        """Attend un montant de l'utilisateur."""
        # attend l'argent
        # donne le change
        self.amount += amount
        return True


# ---------------------------------
# Le Contrôleur (C)
#
# Le flux de l’application y est géré. Tout le séquençage des interactions
# entre l’utilisateur et le système s’y trouve.
# Une sorte de colle entre le modèle et la vue.
# L’utilisateur interagit avec la vue,
# qui interagit à son tour avec le contrôleur.
# Le contrôleur apporte ensuite les modifications appropriées
# aux objets du modèle, en crée de nouveaux,
# ou supprime ceux dont on n’a plus besoin.

class Controller:
    """Contrôleur principal."""

    def __init__(self):
        """Initialise les modèles et les vues."""
        self.bank = CoinBox()  # type: ignore  # noqa: F821
        self.library = Library()
        self.service_history = []

        self.ui = Touchscreen()
        self.audio_output = Speakers()

    def play_next_song(self):
        """Joue le prochain son."""
        songs_to_suggest = []
        for song in self.library:
            # filter logic
            songs_to_suggest.append(song)

        chosen_song = self.ui.prompt_for_next_song(songs_to_suggest)
        request_money(PRICE_PER_SONG)  # type: ignore  # noqa: F821
        self.audio_output.play_song(chosen_song)

    # Beaucoup plus de méthodes ici...
