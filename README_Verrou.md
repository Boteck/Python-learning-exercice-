# Verrou à Combinaison 🔐

Un jeu de devinette en ligne de commande où l'utilisateur doit trouver un code secret à 3 chiffres généré aléatoirement, avec indices chiffre par chiffre et système de blocage temporaire.

---

## Règles du jeu

- Le code secret est un entier aléatoire entre **100 et 999**
- Le joueur dispose de **5 tentatives** par partie
- À chaque mauvais essai, le programme analyse les 3 chiffres séparément et indique pour chacun : ✅ OK, ⬆️ Trop grand, ou ⬇️ Trop petit
- En cas d'échec après 5 tentatives → **blocage de 30 secondes** puis nouveau code généré
- Le joueur peut saisir `exit` à tout moment pour quitter
- En fin de partie, le joueur choisit de rejouer ou non

---

## Lancement

```bash
python verrou_à_combinaison_correction.py
```

Aucune dépendance externe — bibliothèques standard Python uniquement (`random`, `time`).

---

## Exemple de partie

```
============================================================
🔐 VERROU À COMBINAISON - Devine le code à 3 chiffres
============================================================

🎯 NOUVEAU CODE GÉNÉRÉ !
saisissez le code : 456

🔍 ANALYSE DU CODE :
   ⬇️ Centaine : Trop petit
   ⬆️ Dizaine  : Trop grand
   ✅ Unité    : OK

saisissez le code : 523

============================================================
🎉🎉🎉 FÉLICITATIONS! 🎉🎉🎉
 🔓 CODE 523 TROUVÉ !
💪 Tentatives utilisées : 2
============================================================
```

---

## Structure du code

```
verrou_à_combinaison_correction.py
│
├── Affichage des règles
├── Boucle principale (partie_en_cours)
│   ├── Génération du code secret (random.randint)
│   ├── Boucle de tentatives
│   │   ├── Validation de la saisie
│   │   ├── Comparaison chiffre par chiffre (centaine, dizaine, unité)
│   │   └── Décompte des tentatives
│   ├── Blocage 30s si échec (time.sleep)
│   └── Proposition de rejouer
└── Fin du programme
```

---

## Améliorations prévues

- [ ] Réécriture en POO (classe `Verrou`, classe `Partie`)
- [ ] Mode super difficile : code régénéré après 3 erreurs consécutives
- [ ] Historique des tentatives affiché en fin de partie
- [ ] Sauvegarde du meilleur score (moins de tentatives)

---

*Projet personnel — Darky (Enock BOTO C.)*
