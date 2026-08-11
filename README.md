# Snake Game

Un jeu Snake classique développé en Python avec Pygame.

---
## Auteur

Ce jeu a été entièrement développé par moi-même
---

## Commandes

- Flèches directionnelles pour se déplacer
- Touche ESPACE pour lancer ou relancer le jeu
- Touche ECHAP pour quitter le jeu
- Fermer la fenêtre nous fait quitter le jeu

---

## Règles

- La tête du Snake ne doit toucher ni les murs ni son propre corps

---

## Fonctionnalités

- Serpent contrôlé avec les flèches directionnelles
- Nourriture aléatoire qui fait grandir le serpent
- Score affiché en temps réel
- Vitesse progressive (tous les 10 points)
- Écran d'accueil
- Écran Game Over avec score final
- Possibilité de rejouer

---

## Technologies

- Python 3
- Pygame 2.5.2

---

## Structure du projet
Snake-Game/
├── src/
│ ├── constants.py
│ ├── game.py
│ ├── snake.py
│ └── food.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Installation

```bash
# Cloner le projet
git clone https://github.com/GhostNiro/Snake-Game.git
cd Snake-Game

# Installer les dépendances
pip install -r requirements.txt

# Lancer le jeu
python main.py