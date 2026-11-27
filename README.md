# Écrivez du code Python maintenable

Exercices et travaux pratiques du cours « Écrivez du code Python maintenable » proposé par [OpenClassrooms](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable).

## Objectifs du cours

- Appliquer les conventions et le guide de style PEP 8 pour écrire du code Python propre et lisible.
- Améliorer la qualité, la compréhension et la maintenabilité du code.
- Utiliser des outils d'analyse statique (linters) pour identifier les problèmes de qualité.
- Résoudre des problèmes de programmation courants avec les design patterns Python.
- Comprendre et appliquer les principes SOLID pour concevoir un code modulaire et évolutif.

## Contenu du repository

Ce repository contient les fichiers et exercices fournis par OpenClassrooms pour accompagner la formation, ainsi que mes fichiers personnels d'apprentissage et un projet pratique de création d'un jeu de cartes.

```text
├── cours/
├── exercices/
├── jeu-de-carte/
├── .gitignore
└── README.md
```

- `cours/` : notes de cours et exemples de code.
- `exercices/` : exercices fournis par OpenClassrooms et implémentations personnelles.
- `jeu-de-carte/` : projet pratique de création d'un jeu de 52 cartes.

## Projet pratique — Jeu de cartes

Le dossier `jeu-de-carte/` contient un projet de création d'un jeu de 52 cartes standard, permettant de mettre en pratique l'architecture MVC (Modèle-Vue-Contrôleur) et les principes SOLID.

La version initiale du projet est issue du commit [`591cc67`](https://github.com/OpenClassrooms-Student-Center/ecrivez-du-code-python-maintenable-jeu-de-carte/commit/591cc67afd26bdaf9226f4ec58e185fb653f92bb) du dépôt complémentaire OpenClassrooms, correspondant à la création du modèle `Card` (P3C5S1).

Ce projet illustre la construction progressive d'une application Python et l'application des bonnes pratiques de conception et de maintenabilité du code.

### Exécution

Depuis la racine du repository, avec l'environnement virtuel Python activé :

```bash
python jeu-de-carte/main.py
```

### Dépendances

Le fichier `jeu-de-carte/requirements.txt` d'origine est conservé à titre de référence.

Les versions historiques des outils de développement qui y sont déclarées ne sont pas utilisées. Le projet s'appuie sur l'environnement virtuel Python et les outils de développement configurés pour ce repository.

## Technologies et outils

- Python 3
- PEP 8
- Flake8 (linter Python)
- Black (formateur de code Python)
- Design patterns (Décorateur, MVC, etc.)
- Principes SOLID
- Visual Studio Code
- Git et GitHub

## Contexte

Ce repository fait partie de mon parcours de formation continue en développement web et de découverte de l'écosystème Python.

Le projet repose sur les fichiers d'exercices fournis par OpenClassrooms, dont l'historique Git d'origine a été conservé.

Le projet complémentaire de jeu de cartes est intégré directement dans ce repository, à partir d'une version pédagogique du dépôt source, sans créer de dépôt Git imbriqué.

Ce repository retrace ma progression dans le cours à travers des notes, des exercices et des implémentations personnelles, en suivant les différentes étapes pédagogiques.

## Sources

- [Cours OpenClassrooms — Écrivez du code Python maintenable](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable)
- [Repository d'origine — OpenClassrooms Student Center](https://github.com/OpenClassrooms-Student-Center/ecrivez-du-code-python-maintenable)
- [Projet complémentaire — Jeu de cartes](https://github.com/OpenClassrooms-Student-Center/ecrivez-du-code-python-maintenable-jeu-de-carte)
