# Quiz Master v2.0 🎮

Un jeu de quiz en ligne de commande avec profils joueurs persistants, chronomètre, système de badges et classement général.

---

## Fonctionnalités

### Gestion des joueurs
- Connexion ou création de profil à chaque lancement
- Statistiques individuelles persistantes : parties jouées, scores max/min/moyen, date d'inscription, dernière partie
- Système de badges débloqués automatiquement :
  - 🌱 Débutant — première partie jouée
  - 🏆 Score parfait — score de 100/100
  - 🎮 Joueur assidu — 10 parties ou plus
  - ⭐ Expert — moyenne générale ≥ 80

### Quiz
- 5 rubriques : Sport, Histoire, Santé, Technologie, Actualité
- Nombre de questions configurable par partie
- Questions tirées aléatoirement dans la rubrique choisie
- Chronomètre par question et temps total affiché en fin de partie
- Score calculé sur 100 avec verdict final

### Persistance JSON
Toutes les données sont sauvegardées automatiquement dans un dossier `data/` :
- `questions.json` — banque de questions par rubrique
- `joueurs.json` — profils et statistiques des joueurs
- `historique.json` — journal de toutes les parties jouées
- `avis.json` — avis laissés par les joueurs

### Contributions communautaires
- Ajout de nouvelles questions dans n'importe quelle rubrique
- Dépôt d'avis textuels sur le jeu
- Validation et confirmation avant enregistrement

### Classement et historique
- Classement général trié par score moyen avec médailles 🥇🥈🥉
- Historique des 10 dernières parties du joueur connecté

---

## Lancement

```bash
python QCM.py
```

Aucune dépendance externe — bibliothèques standard Python uniquement (`json`, `os`, `random`, `time`, `datetime`).

Le dossier `data/` et les fichiers JSON sont créés automatiquement au premier lancement.

---

## Structure des fichiers

```
projet/
├── QCM.py
└── data/
    ├── questions.json
    ├── joueurs.json
    ├── historique.json
    └── avis.json
```

---

## Structure du code

```
QCM.py
│
├── Constantes & chemins (BASE_DIR, DATA_DIR, fichiers JSON)
├── QUESTIONS_PAR_DEFAUT — banque initiale de 20 questions
│
├── Persistance JSON
│   ├── initialiser_donnees()
│   ├── charger_json()
│   └── sauvegarder_json()
│
├── Gestion des joueurs
│   ├── creer_profil_joueur()
│   ├── connexion_joueur()
│   ├── mettre_a_jour_joueur()
│   └── enregistrer_historique()
│
├── Fonctions principales
│   ├── jeu()              — déroulement d'une partie
│   ├── info()             — profil joueur + stats globales
│   ├── classement()       — classement général
│   ├── historique_afficher() — 10 dernières parties
│   ├── avis_afficher()    — lecture des avis
│   ├── ajout()            — contribution question ou avis
│   └── quitter()
│
└── main() — boucle du menu principal
```

---

## Améliorations prévues

- [ ] Réécriture en POO (classes `Joueur`, `Quiz`, `Banque`)
- [ ] Mode multijoueur en local
- [ ] Difficulté par question (facile / moyen / difficile)
- [ ] Export des statistiques en fichier texte ou CSV
- [ ] Interface graphique (Tkinter)

---

*Projet personnel — Darky (Enock BOTO C.)*
