# Demande une phrase à l'utilisateur
# Exemple : "Python est génial ! Mais il faut pratiquer. 123"

# Le programme doit détecter et analyser :

# 1. COMPTER :
#    - Nombre total de caractères
#    - Nombre de mots
#    - Nombre de phrases (points, !, ?)
#    - Nombre de chiffres

# 2. QUALIFIER :
#    - Si la phrase contient des mots interdits (liste=["mot1", "mot2"])
#      → Alerte "Langage inapproprié"
#    - Si plus de 3 points d'exclamation → "Ton agressif détecté !"
#    - Si plus de 50% de mots sont courts (<4 lettres) → "Style télégraphique"
#    - Si plus de 30% de mots sont longs (>8 lettres) → "Style soutenu"

# 3. ANALYSE AVANCÉE (conditions complexes) :
#    - Détecte si la phrase est :
#      * Une question (commence par "Comment", "Pourquoi", "Est-ce", finit par ?)
#      * Une exclamation (contient !)
#      * Une affirmation (ni ? ni !)
#    - Détecte le sujet probable :
#      * Si contient "je" → Première personne
#      * Si contient "tu" → Deuxième personne
#      * Si contient "il/elle" → Troisième personne
#    - Calcule un score de "positivité" :
#      * Mots positifs (amour, bien, super, génial) : +1 chacun
#      * Mots négatifs (haine, mal, nul, horrible) : -1 chacun
#      * Score final et interprétation

# EXEMPLE DE SORTIE :
# """
# === ANALYSE DE LA PHRASE ===
# Texte : "Je déteste quand il pleut ! Mais j'aime le chocolat."
#
# 📊 STATISTIQUES :
# Caractères : 45
# Mots : 9
# Phrases : 2
#
#TON : Agressif (car !) mais mitigé (score positif: 1, négatif: 1)
# STYLE : Mixte (courts: 4, longs: 2)
# SUJET : Première personne (présence de "je")
#
# 💡 CONCLUSION : Une personne contrariée par la météo qui se console avec du chocolat.

sign = [" ", ".", ",", ";", ":", "!", "?", "'", "\"", "(", ")", "[", "]", "{", "}", "-", "_", "«", "»", "‘", "’", "“", "”", "/", "\\", "|", "*", "&", "@", "#", "%", "^", "+", "=", "~", "`", "<", ">", "°"]
# initialisation des compteurs 
i=0
letter=0
number=0
words_nbr=0 
character=0

#demande du texte
print ("="*40)
print ("Bonjour et Bienvenue 😊 ""\nVeiller saisir le texte à analyser    ")
print ("="*40)
sentence= input("Texte:\n")

#DECOMPTE
for n in sentence:
    #nombre de caractères
    character+=1
    
    #nombre de lettres 
    if n.isdigit()==False and n  not in sign:
        letter +=1
        
     #nombre de chiffres  
    if n.isdigit() :
        number +=1
       
     #nombre de mots
    if n==" ":
        words_nbr+=1

#nous importons Reges pour un décompte des signes.,?,! dans la phrase 
import re
phrases = re.split('[.!?]', sentence) # ceci correspond au découpage du texte de l'utilisateur en plusieurs portions de phrase. ici deux portions sont séparés par . ou ? ou ! . 

# ici nous décomptons les éléments de la listes sans les caractères '
nb_phrases = len([p for p in phrases if p.strip()])

print ("="*40)              
print ("RÈSUMTATS DE L'ANALYSE 🧐🧐"+"\n==>nombre de caractère=",character,"\n==>nombre de lettres=",letter,"\n==>nombre de chiffre=", number,"\n==>nombre de phrase = ",nb_phrases,"\n==>nombre de mots =",len(re.findall(r'\b\w+\b', sentence))) 

def qualifier(phrase):
    mots_interdits = ["idiot", "con", "salope", "enculé", "pute","tuer", "meurtre", "crasher", "exploser","raciste", "homophobe", "sexiste","merde", "putain", "bordel", "foutre","gagné", "clique", "viagra", "escroc","fuck", "shit", "bitch", "asshole", "dumb","abruti", "imbécile", "crétin", "connard","pédé", "lesbienne", "nègre", "bougnoul", "mort", "suicide", "terroriste", "attentat","arnaque", "pirate", "hack", "phishing","spam", "casino", "poker", "porno","drogue", "coke", "herbe", "joint","prostitution", "escort", "pimp", "squatte","flic", "police", "fouille", "perquisition"]
    
    positifs = ["amour", "bien", "super", "génial","excellent", "formidable", "merveilleux", "fantastique", "incroyable", "extraordinaire", "parfait", "magnifique", "splendide","sublime", "ravissant","charmant","adorable", "aimable", "gentil", "sympa","heureux", "joyeux", "content", "satisfait", "enthousiaste","passionné", "enthousiasmé", "motivé", "inspiré", "créatif","brillant", "intelligent", "astucieux", "ingénieux", "talentueux","courageux", "brave", "héroïque", "généreux", "altruiste","sincère", "honnête", "loyal", "fidèle", "respectueux","calme", "serein", "tranquille", "détendu", "relax","confiant", "optimiste", "positif", "ambitieux", "déterminé"]
    alerte = []

    # Mots interdits
    if any(mot in re.findall(r'\b\w+\b', phrase) for mot in mots_interdits):
        alerte.append("==>Langage inapproprié❌")

    # Points d'exclamation
    if phrase.count("!") > 3:
        alerte.append("==>Ton agressif détecté !🔪🔪🔪")

    # Analyse mots
    mots = re.findall(r'\b\w+\b', phrase)
    nb_mots = len(mots)
    if nb_mots > 0:
        # Mots courts
        courts = sum(1 for m in mots if len(m) < 4)
        if courts/nb_mots > 0.5:
            alerte.append("==>Style télégraphique✍️✍️")

        # Mots longs
        longs = sum(1 for m in mots if len(m) > 8)
        if longs/nb_mots > 0.3:
            alerte.append("==>Style soutenu✍️✍️")

        score = sum(1 if m in positifs else -1 if m in mots_interdits else 0 for m in mots)
        if score > 0: 
            alerte.append(f"==>Ton positif😊 (score: {score})")
        elif score < 0: 
            alerte.append(f"==>Ton négatif❌ (score: {score})")
    return alerte if alerte else ["==>Style neutre😑"]

x=qualifier(sentence)
"""Dark nel"""
for p in x:
    print(p) 
print ("="*40)    
    #END#