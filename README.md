# ENDLESS ARENA

## Projet d'ISN année 2017-2018 - Lycée Janson de Sailly
### - Henri de Pesquidoux - Olivier Moreau -

Réalisé avec python3 - pygame
#### Manifeste
> Le projet est un jeu mêlant des mécanismes d'arène en 2d (Towerfall, Samurai Gunn ...) et d' endless runner (Run ninja run ...).
> Deux personnages s'affrontent à l'aide d'épées , tout en sautant de plateformes en plateformes dans le but d'éviter le _Insérer ici obstacle poursuivant les persos_. Le premier à 3 points gagne.

#### Gestion des points

> Un joueur gagne un point en tuant l'autre, et en perd un en tombant (le score d'un joueur peut être négatif) ou en étant rattrapé par le _Insérer ici obstacle poursuivant les persos_

### Proportions des éléments de jeu

> La fenêtre principale à une résolution de 16x9 (configurable ?). Cette fenêtre est divisée en 'cases' (invisibles pour le joueur) : 16x9 encore.
La taille de chaque objet est quantifiée en cases : le sprite doit s'approcher le plus possible de remplir l'espace donné tout en restant agréable à l'oeil.

> Liste provisoire des tailles des objets:

> * Une plateforme est composée d'un nombre X de blocs d'une case chacun.

> * Un personnage remplis deux cases l'une au dessus de l'autre.

> * Une épée remplis une case et peut frapper n'importe quelle case en contact avec son maitre (le personnage auquel elle est attachée), y compris en diagonale.
