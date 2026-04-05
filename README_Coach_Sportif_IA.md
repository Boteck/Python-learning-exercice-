# Coach Sportif IA 🏋️

Un programme Python en ligne de commande qui génère un programme d'entraînement personnalisé à partir des données physiques de l'utilisateur.

---

## Fonctionnalités

### Saisie utilisateur
Le programme collecte les informations suivantes avec validation à chaque étape :
- Sexe (M / F)
- Âge
- Poids (kg)
- Taille (cm)
- Niveau d'activité : sédentaire, modéré, actif, très actif
- Objectif : perte de poids, gain musculaire, maintien

### Calculs effectués
- **IMC** (Indice de Masse Corporelle) : `poids / taille²`
- **Besoins caloriques journaliers** selon la formule de Mifflin-St Jeor, ajustés par le niveau d'activité

Bonus calorique selon le niveau d'activité :
- Sédentaire → +0 kcal
- Modéré → +200 kcal
- Actif → +400 kcal
- Très actif → +600 kcal

### Conseil personnalisé
Le conseil est déterminé par la combinaison de la catégorie IMC et de l'objectif :

- **Sous-poids** (IMC < 18.5) : avertissement ou focus musculaire selon l'objectif
- **Poids normal** (18.5 ≤ IMC < 25) : cardio, musculation ou équilibre
- **Surpoids** (25 ≤ IMC < 30) : cardio + diète, musculation modérée ou vigilance
- **Obésité** (IMC ≥ 30) : consultation médicale recommandée selon l'objectif

---

## Lancement

```bash
python Coach_Sportif_IA.py
```

Aucune dépendance externe — uniquement la bibliothèque standard Python.

---

## Exemple de sortie

```
========================================
=== COACH SPORTIF IA ===
========================================

📋 DONNÉES UTILISATEUR
------------------------------
• Âge : 20.0 ans
• Poids : 70.0 kg
• Taille : 175.0 cm
• Sexe : Masculin
• Niveau d'activité: modéré
• Objectif: gagné des muscles

📊 RÉSULTATS
------------------------------
📊 IMC : 22.9 (Poids normal)
📊 CALORIE : 1880.8 Kcal (Poids normal)

💡 CONSEIL PERSONNALISÉ
------------------------------
💪 Musculation + protéines

========================================
✨ Restez motivé ! ✨
========================================
```

---

## Structure du code

```
Coach_Sportif_IA.py
│
├── Saisie et validation des entrées
│   ├── Sexe (boucle while)
│   ├── Âge, Poids, Taille (try/except + boucle while)
│   ├── Niveau d'activité (try/except + boucle while)
│   └── Objectif (try/except + boucle while)
│
└── def analyse(sx, a, p, t, ac, o)
    ├── Calcul de l'IMC
    ├── Calcul des calories (Mifflin-St Jeor)
    └── Retourne conseil, IMC, calorie
```

---

## Améliorations prévues

- [ ] Réécriture en POO (classe `Utilisateur`, classe `Coach`)
- [ ] Génération d'un plan d'entraînement hebdomadaire détaillé
- [ ] Export du rapport en fichier texte ou PDF
- [ ] Ajout d'un suivi de progression dans le temps

---

*Projet personnel — Darky (Enock BOTO C.)*
