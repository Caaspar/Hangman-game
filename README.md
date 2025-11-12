# Hangman-game

Un jeu simple et coloré du Pendu en Python. Vous pouvez jouer seul avec un mot aléatoire depuis un fichier ou défier un ami en mode deux joueurs.

## Fonctionnalités :

* 🎨 Interface colorée dans le terminal grâce à colorama.
* 🕹️ Mode solo avec un mot aléatoire tiré du fichier words.txt (1000 mots disponible générés aléatoirement).
* 👥 Mode deux joueurs : un joueur choisit un mot secret que l’autre doit deviner.
* 📈 Représentation ASCII du pendu qui évolue à chaque erreur.
* 🔒 Entrée du mot secret masquée en mode deux joueurs avec getpass.

## Comment jouer :

1. Cloner ou télécharger le dépôt
2. Lancer le jeu :
```bash
python3 hangman.py
```
ou
```bash
python hangman.py
```
3. Choisir un mode :
    * Mode solo : Le jeu choisit un mot aléatoire.
    * Mode deux joueurs : Le joueur 1 entre un mot secret pour le joueur 2.
    * Quitter : Pour fermer le jeu.
4. Deviner les lettres une par une. Chaque mauvaise réponse rapproche le pendu de la fin.
5. Gagner en devinant toutes les lettres avant que le pendu soit complètement dessiné.

## Étapes du pendu

Le jeu utilise plusieurs dessins ASCII pour montrer le pendu qui se complète après chaque erreur.

       +---+
       |   |
       O   |
      /|\  |
      / \  |
    =========

Notes
* Seules les lettres alphabétiques uniques sont acceptées.
* Répéter une lettre compte comme une erreur.
* En mode deux joueurs, le mot secret est masqué à l’écran pour que le joueur 2 ne le voie pas.
* Le jeu est en anglais mais les mots présents dans words.txt sont en français