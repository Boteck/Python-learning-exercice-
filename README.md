# Analyseur de Phrase Intelligente 🧐

Un programme Python en ligne de commande qui analyse un texte saisi par l'utilisateur et retourne des statistiques détaillées ainsi qu'une qualification stylistique et tonale.

---

## Fonctionnalités

### Statistiques de base
- Nombre total de **caractères**
- Nombre de **lettres** (hors chiffres et signes de ponctuation)
- Nombre de **chiffres**
- Nombre de **phrases** (délimitées par `.`, `!`, `?`)
- Nombre de **mots**

### Qualification du texte
Le programme analyse automatiquement le style et le ton du texte :

- Présence de mots interdits → ❌ Langage inapproprié
- Plus de 3 points d'exclamation → 🔪 Ton agressif détecté
- Plus de 50% de mots courts (< 4 lettres) → ✍️ Style télégraphique
- Plus de 30% de mots longs (> 8 lettres) → ✍️ Style soutenu
- Score de positivité > 0 → 😊 Ton positif
- Score de positivité < 0 → ❌ Ton négatif
- Aucune condition déclenchée → 😑 Style neutre

### Score de positivité
- Chaque **mot positif** détecté ajoute **+1** au score
- Chaque **mot interdit** détecté retire **-1** au score

---

## Lancement

```bash
python Analyseur_de_phrase_intelligente.py
```

Aucune dépendance externe — le programme utilise uniquement le module standard `re`.

---

## Exemple de sortie

```
========================================
Bonjour et Bienvenue 😊
Veiller saisir le texte à analyser
========================================
Texte:
Je déteste quand il pleut ! Mais j'aime le chocolat.
========================================
RÈSUMTATS DE L'ANALYSE 🧐🧐
==>nombre de caractère= 51
==>nombre de lettres= 40
==>nombre de chiffre= 0
==>nombre de phrase= 2
==>nombre de mots= 10
==>Style neutre😑
========================================
```

---

## Structure du code

```
Analyseur_de_phrase_intelligente.py
│
├── Initialisation des compteurs
├── Saisie utilisateur
├── Boucle de décompte (caractères, lettres, chiffres, mots)
├── Découpage en phrases avec re.split()
├── Affichage des statistiques
└── def qualifier(phrase)
    ├── Détection des mots interdits
    ├── Détection du ton agressif
    ├── Analyse des mots courts / longs
    └── Calcul du score de positivité
```

---

## Améliorations prévues

- [ ] Réécriture en POO (classe `Analyseur`)
- [ ] Détection du type de phrase (question, exclamation, affirmation)
- [ ] Détection de la personne grammaticale (je / tu / il-elle)
- [ ] Conclusion automatique générée en langage naturel
- [ ] Interface graphique (Tkinter ou web)

---

*Projet personnel — Darky (Enock BOTO C.)*
