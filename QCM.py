"""
╔══════════════════════════════════════════════════════════╗
║                     QUIZ MASTER v2.0                     ║
║          Programme principal — version complète          ║
╚══════════════════════════════════════════════════════════╝

Fonctionnalités :
  - Gestion des joueurs avec profils persistants
  - Questions et réponses sauvegardées en JSON
  - Statistiques par joueur et globales persistantes
  - Chronomètre par question
  - Système de niveaux et de badges
  - Historique des parties
  - Contributions validées (questions et avis)
  - Classement général
"""

import random
import sys
import json
import os
import time
from datetime import datetime

# ══════════════════════════════════════════════════════════
#  CHEMINS DES FICHIERS DE DONNÉES
# ══════════════════════════════════════════════════════════

BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
DATA_DIR      = os.path.join(BASE_DIR, "data")
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
JOUEURS_FILE   = os.path.join(DATA_DIR, "joueurs.json")
AVIS_FILE      = os.path.join(DATA_DIR, "avis.json")
HISTORIQUE_FILE= os.path.join(DATA_DIR, "historique.json")

NOMS_RUBRIQUES = ["Sport", "Histoire", "Santé", "Technologie", "Actualité"]

# ══════════════════════════════════════════════════════════
#  DONNÉES INITIALES PAR DÉFAUT
# ══════════════════════════════════════════════════════════

QUESTIONS_PAR_DEFAUT = {
    "0": {
        "nom": "Sport",
        "questions": [
            "Quel pays a remporté la Coupe du Monde 2022 ? ; 1-France ; 2-Argentine ; 3-Brésil",
            "Combien de joueurs compte une équipe de football ? ; 1-9 ; 2-11 ; 3-13",
            "Dans quel sport utilise-t-on un volant ? ; 1-Tennis ; 2-Badminton ; 3-Squash",
            "Combien de sets faut-il gagner pour remporter un match de tennis en Grand Chelem (hommes) ? ; 1-2 ; 2-3 ; 3-4"
        ],
        "reponses": ["2", "2", "2", "2"]
    },
    "1": {
        "nom": "Histoire",
        "questions": [
            "En quelle année a eu lieu la Révolution française ? ; 1-1789 ; 2-1815 ; 3-1848",
            "Qui était le premier président des États-Unis ? ; 1-Lincoln ; 2-Jefferson ; 3-Washington",
            "Quelle civilisation a construit les pyramides de Gizeh ? ; 1-Romaine ; 2-Grecque ; 3-Égyptienne",
            "En quelle année le mur de Berlin est-il tombé ? ; 1-1985 ; 2-1989 ; 3-1991"
        ],
        "reponses": ["1", "3", "3", "2"]
    },
    "2": {
        "nom": "Santé",
        "questions": [
            "Quel organe filtre le sang ? ; 1-Le foie ; 2-Les reins ; 3-Le poumon",
            "Combien d'os compte le corps humain adulte ? ; 1-106 ; 2-206 ; 3-306",
            "Quelle vitamine est produite par la peau sous l'effet du soleil ? ; 1-Vitamine A ; 2-Vitamine C ; 3-Vitamine D",
            "Quel est le groupe sanguin universel donneur ? ; 1-AB+ ; 2-O- ; 3-A+"
        ],
        "reponses": ["2", "2", "3", "2"]
    },
    "3": {
        "nom": "Technologie",
        "questions": [
            "Qui a fondé Apple ? ; 1-Bill Gates ; 2-Steve Jobs ; 3-Elon Musk",
            "Que signifie CPU ? ; 1-Central Processing Unit ; 2-Computer Power Unit ; 3-Core Program Utility",
            "Quel langage est principalement utilisé pour le développement web front-end ? ; 1-Python ; 2-JavaScript ; 3-Java",
            "En quelle année le premier iPhone a-t-il été lancé ? ; 1-2005 ; 2-2007 ; 3-2009"
        ],
        "reponses": ["2", "1", "2", "2"]
    },
    "4": {
        "nom": "Actualité",
        "questions": [
            "Quel continent abrite le plus grand nombre de pays ? ; 1-Asie ; 2-Amérique ; 3-Afrique",
            "Quelle organisation mondiale gère la santé internationale ? ; 1-ONU ; 2-OMS ; 3-UNESCO",
            "Quelle est la monnaie officielle du Bénin ? ; 1-Naira ; 2-Franc CFA ; 3-Cedi",
            "Combien de pays composent l'Union Européenne ? ; 1-25 ; 2-27 ; 3-30"
        ],
        "reponses": ["3", "2", "2", "2"]
    }
}

# ══════════════════════════════════════════════════════════
#  GESTION DE LA PERSISTANCE JSON
# ══════════════════════════════════════════════════════════

def initialiser_donnees():
    """Crée le dossier data et les fichiers JSON s'ils n'existent pas."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(QUESTIONS_FILE):
        sauvegarder_json(QUESTIONS_FILE, QUESTIONS_PAR_DEFAUT)

    if not os.path.exists(JOUEURS_FILE):
        sauvegarder_json(JOUEURS_FILE, {})

    if not os.path.exists(AVIS_FILE):
        sauvegarder_json(AVIS_FILE, [])

    if not os.path.exists(HISTORIQUE_FILE):
        sauvegarder_json(HISTORIQUE_FILE, [])


def charger_json(chemin):
    """Charge et retourne le contenu d'un fichier JSON."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return None


def sauvegarder_json(chemin, donnees):
    """Sauvegarde des données dans un fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)


# ══════════════════════════════════════════════════════════
#  GESTION DES JOUEURS
# ══════════════════════════════════════════════════════════

def creer_profil_joueur(nom):
    """Retourne un nouveau profil joueur vide."""
    return {
        "nom": nom,
        "nb_parties": 0,
        "score_max": 0,
        "score_min": None,
        "cumul_scores": 0,
        "date_inscription": datetime.now().strftime("%d/%m/%Y"),
        "derniere_partie": None,
        "badges": []
    }


def connexion_joueur():
    """Gère la connexion ou la création d'un joueur. Retourne le nom du joueur."""
    joueurs = charger_json(JOUEURS_FILE)

    print("\n── CONNEXION ──")
    nom = input("Entrez votre nom de joueur : ").strip()

    if not nom:
        print("❌ Nom invalide.")
        return connexion_joueur()

    if nom not in joueurs:
        confirmation = input(f"Joueur « {nom} » inconnu. Créer ce profil ? (o/n) : ").strip().lower()
        if confirmation == "o":
            joueurs[nom] = creer_profil_joueur(nom)
            sauvegarder_json(JOUEURS_FILE, joueurs)
            print(f"✅ Profil créé. Bienvenue, {nom} !\n")
        else:
            return connexion_joueur()
    else:
        print(f"✅ Bienvenue de retour, {nom} ! ({joueurs[nom]['nb_parties']} partie(s) jouée(s))\n")

    return nom


def mettre_a_jour_joueur(nom, score):
    """Met à jour les statistiques persistantes d'un joueur après une partie."""
    joueurs = charger_json(JOUEURS_FILE)
    j = joueurs[nom]

    j["nb_parties"] += 1
    j["cumul_scores"] += score
    j["derniere_partie"] = datetime.now().strftime("%d/%m/%Y %H:%M")

    if score > j["score_max"]:
        j["score_max"] = score
    if j["score_min"] is None or score < j["score_min"]:
        j["score_min"] = score

    # Attribution de badges
    moyenne = j["cumul_scores"] / j["nb_parties"]
    if score == 100 and "🏆 Score parfait" not in j["badges"]:
        j["badges"].append("🏆 Score parfait")
    if j["nb_parties"] >= 10 and "🎮 Joueur assidu" not in j["badges"]:
        j["badges"].append("🎮 Joueur assidu")
    if moyenne >= 80 and "⭐ Expert" not in j["badges"]:
        j["badges"].append("⭐ Expert")
    if j["nb_parties"] >= 1 and "🌱 Débutant" not in j["badges"]:
        j["badges"].append("🌱 Débutant")

    joueurs[nom] = j
    sauvegarder_json(JOUEURS_FILE, joueurs)


def enregistrer_historique(nom, rubrique, nb_questions, score, temps_total):
    """Ajoute une entrée dans l'historique global des parties."""
    historique = charger_json(HISTORIQUE_FILE)
    historique.append({
        "joueur": nom,
        "rubrique": rubrique,
        "nb_questions": nb_questions,
        "score": score,
        "temps_total": round(temps_total, 1),
        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
    })
    sauvegarder_json(HISTORIQUE_FILE, historique)


# ══════════════════════════════════════════════════════════
#  FONCTIONS PRINCIPALES
# ══════════════════════════════════════════════════════════

def jeu(nom_joueur):
    """Lance une partie de quiz avec chronomètre."""
    donnees = charger_json(QUESTIONS_FILE)

    RUBRIQUE_MENU = "\n"
    for k, v in donnees.items():
        RUBRIQUE_MENU += f"  {int(k)+1} - {v['nom']}\n"

    print(RUBRIQUE_MENU)

    try:
        rub = int(input("Choisissez votre rubrique : ")) - 1
        if rub < 0 or rub >= len(donnees):
            raise ValueError
    except ValueError:
        print("❌ Rubrique invalide.\n")
        return

    rubrique_data = donnees[str(rub)]
    questions  = rubrique_data["questions"]
    reponses   = rubrique_data["reponses"]
    nom_rub    = rubrique_data["nom"]
    max_q      = len(questions)

    if max_q == 0:
        print("❌ Aucune question disponible pour cette rubrique.\n")
        return

    try:
        nb_question = int(input(f"Nombre de questions (1 à {max_q}) : "))
        if nb_question < 1 or nb_question > max_q:
            raise ValueError
    except ValueError:
        print(f"❌ Entrez un nombre entre 1 et {max_q}.\n")
        return

    try:
        limite = int(input("Temps limite par question en secondes (0 = sans limite) : "))
        if limite < 0:
            raise ValueError
    except ValueError:
        print("❌ Valeur invalide, pas de limite appliquée.")
        limite = 0

    nb_correct   = 0
    numeros_poses = []
    temps_total  = 0
    i = 0

    print(f"\n{'─'*45}")
    print(f"  Quiz — {nom_rub} | {nb_question} question(s)")
    if limite > 0:
        print(f"  ⏱  {limite} secondes par question")
    print(f"{'─'*45}\n")

    while i < nb_question:
        numero = random.randint(0, max_q - 1)
        if numero in numeros_poses:
            continue
        numeros_poses.append(numero)
        i += 1

        print(f"Question {i}/{nb_question} :")
        print(f"  {questions[numero]}")

        debut = time.time()
        if limite > 0:
            print(f"  ⏱  Vous avez {limite}s pour répondre.")

        reponse_joueur = input("  Votre réponse : ").strip()
        duree = time.time() - debut
        temps_total += duree

        if limite > 0 and duree > limite:
            print(f"  ⏰ Temps dépassé ! ({round(duree, 1)}s) La réponse était : {reponses[numero]}\n")
            continue

        bonne = reponses[numero]
        if reponse_joueur == bonne:
            nb_correct += 1
            print(f"  ✅ EXACT ! ({round(duree, 1)}s)\n")
        else:
            print(f"  ❌ FAUX. La bonne réponse était : {bonne} ({round(duree, 1)}s)\n")

    score = round(100 * nb_correct / nb_question, 2)

    print(f"{'─'*45}")
    print(f"  🏆 SCORE FINAL : {score}/100  ({nb_correct}/{nb_question} bonnes réponses)")
    print(f"  ⏱  Temps total : {round(temps_total, 1)}s")

    if score < 50:
        verdict = "Peut mieux faire."
    elif score < 80:
        verdict = "Bien !"
    elif score < 100:
        verdict = "Excellent !"
    else:
        verdict = "WAOUH, VOUS ÊTES UN AS !"
    print(f"  VERDICT : {verdict}")
    print(f"{'─'*45}\n")

    mettre_a_jour_joueur(nom_joueur, score)
    enregistrer_historique(nom_joueur, nom_rub, nb_question, score, temps_total)


def info(nom_joueur):
    """Affiche les statistiques du joueur connecté et les stats globales."""
    joueurs   = charger_json(JOUEURS_FILE)
    historique = charger_json(HISTORIQUE_FILE)
    j = joueurs.get(nom_joueur, {})

    print(f"\n── MON PROFIL : {nom_joueur} ──")
    nb = j.get("nb_parties", 0)
    print(f"  Inscrit le          : {j.get('date_inscription', 'N/A')}")
    print(f"  Dernière partie     : {j.get('derniere_partie', 'Aucune')}")
    print(f"  Parties jouées      : {nb}")

    if nb > 0:
        moyenne = round(j["cumul_scores"] / nb, 2)
        print(f"  Score maximal       : {j['score_max']}")
        print(f"  Score minimal       : {j['score_min']}")
        print(f"  Score moyen         : {moyenne}")
    else:
        print("  Aucune partie jouée encore.")

    badges = j.get("badges", [])
    if badges:
        print(f"  Badges              : {' | '.join(badges)}")

    print(f"\n── STATISTIQUES GLOBALES ──")
    donnees = charger_json(QUESTIONS_FILE)
    total_questions = sum(len(v["questions"]) for v in donnees.values())
    print(f"  Nombre de rubriques : {len(donnees)}")
    print(f"  Total de questions  : {total_questions}")
    for k, v in donnees.items():
        print(f"    → {v['nom']:<15} : {len(v['questions'])} question(s)")

    parties_totales = len(historique)
    print(f"\n  Parties jouées (tous joueurs) : {parties_totales}")
    if parties_totales > 0:
        scores = [p["score"] for p in historique]
        print(f"  Meilleur score global : {max(scores)}")
        print(f"  Score moyen global    : {round(sum(scores)/len(scores), 2)}")
    print()


def avis_afficher():
    """Affiche tous les avis laissés par les joueurs."""
    tous_avis = charger_json(AVIS_FILE)
    print(f"\n── AVIS DES JOUEURS ({len(tous_avis)}) ──")
    if not tous_avis:
        print("  Aucun avis pour le moment.\n")
    else:
        for i, a in enumerate(tous_avis, 1):
            print(f"  {i}. [{a['joueur']} — {a['date']}] {a['texte']}")
    print()


def ajout(nom_joueur):
    """Permet d'ajouter une question ou un avis avec validation complète."""
    choix = ""
    while choix not in ["1", "2"]:
        choix = input("Votre contribution : 1-Avis  |  2-Question → ").strip()

    if choix == "2":
        donnees = charger_json(QUESTIONS_FILE)
        print()
        for k, v in donnees.items():
            print(f"  {int(k)+1} - {v['nom']}")

        try:
            rub = int(input("\nRubrique (1-5) : ")) - 1
            if rub < 0 or rub >= len(donnees):
                raise ValueError
        except ValueError:
            print("❌ Rubrique invalide.\n")
            return

        q = input("Question + options (ex : 'Es-tu humain ? ; 1-Oui ; 2-Non') : ").strip()
        if not q or ";" not in q:
            print("❌ Format invalide. La question doit contenir des options séparées par ';'.\n")
            return

        a = input("Bonne réponse (ex : '1') : ").strip()
        if not a:
            print("❌ Réponse vide.\n")
            return

        confirmation = input(f"\nConfirmer : « {q} » → réponse {a} ? (o/n) : ").strip().lower()
        if confirmation == "o":
            donnees[str(rub)]["questions"].append(q)
            donnees[str(rub)]["reponses"].append(a)
            sauvegarder_json(QUESTIONS_FILE, donnees)
            print("✅ Question ajoutée et sauvegardée !\n")
        else:
            print("❌ Ajout annulé.\n")

    else:
        texte = input("Que pensez-vous de ce jeu ? : ").strip()
        if not texte:
            print("❌ Avis vide.\n")
            return
        tous_avis = charger_json(AVIS_FILE)
        tous_avis.append({
            "joueur": nom_joueur,
            "texte": texte,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        sauvegarder_json(AVIS_FILE, tous_avis)
        print("✅ Avis enregistré et sauvegardé !\n")

    print("──────────────────────────────────────\n   MERCI POUR VOTRE CONTRIBUTION !\n──────────────────────────────────────\n")


def classement():
    """Affiche le classement général de tous les joueurs."""
    joueurs = charger_json(JOUEURS_FILE)
    if not joueurs:
        print("\nAucun joueur enregistré.\n")
        return

    classement_liste = []
    for nom, j in joueurs.items():
        if j["nb_parties"] > 0:
            moyenne = round(j["cumul_scores"] / j["nb_parties"], 2)
            classement_liste.append((nom, moyenne, j["score_max"], j["nb_parties"]))

    classement_liste.sort(key=lambda x: x[1], reverse=True)

    print(f"\n── 🏆 CLASSEMENT GÉNÉRAL ──")
    print(f"  {'Rang':<5} {'Joueur':<20} {'Moyenne':<10} {'Meilleur':<10} {'Parties'}")
    print(f"  {'─'*55}")
    for rang, (nom, moy, maxi, nb) in enumerate(classement_liste, 1):
        medaille = "🥇" if rang == 1 else ("🥈" if rang == 2 else ("🥉" if rang == 3 else f"  {rang}."))
        print(f"  {medaille:<5} {nom:<20} {moy:<10} {maxi:<10} {nb}")
    print()


def historique_afficher(nom_joueur):
    """Affiche l'historique des 10 dernières parties du joueur connecté."""
    historique = charger_json(HISTORIQUE_FILE)
    mes_parties = [p for p in historique if p["joueur"] == nom_joueur]

    print(f"\n── HISTORIQUE DE {nom_joueur} ({len(mes_parties)} partie(s)) ──")
    if not mes_parties:
        print("  Aucune partie jouée encore.\n")
        return

    for p in mes_parties[-10:][::-1]:
        print(f"  [{p['date']}] {p['rubrique']:<15} | {p['nb_questions']} questions | Score : {p['score']}/100 | Temps : {p['temps_total']}s")
    print()


def quitter():
    """Quitte proprement le programme."""
    print("\n👋 Merci d'avoir joué. À bientôt !\n")
    sys.exit()


# ══════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════

MENU = """
╔══════════════════════════════════════╗
║          🎮  QUIZ MASTER v2.0        ║
╠══════════════════════════════════════╣
║  1 – Jouer                           ║
║  2 – Mon profil & statistiques       ║
║  3 – Classement général              ║
║  4 – Historique de mes parties       ║
║  5 – Avis des joueurs                ║
║  6 – Contribuer (question / avis)    ║
║  7 – Changer de joueur               ║
║  8 – Quitter                         ║
╚══════════════════════════════════════╝"""


def main():
    initialiser_donnees()
    print("\n" + "═"*45)
    print("        BIENVENUE SUR QUIZ MASTER v2.0")
    print("═"*45)

    nom_joueur = connexion_joueur()

    while True:
        print(MENU)
        print(f"  Joueur connecté : {nom_joueur}")
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            jeu(nom_joueur)
        elif choix == "2":
            info(nom_joueur)
        elif choix == "3":
            classement()
        elif choix == "4":
            historique_afficher(nom_joueur)
        elif choix == "5":
            avis_afficher()
        elif choix == "6":
            ajout(nom_joueur)
        elif choix == "7":
            nom_joueur = connexion_joueur()
        elif choix == "8":
            quitter()
        else:
            print("❌ Option invalide. Choisissez entre 1 et 8.\n")


if __name__ == "__main__":
    main()
