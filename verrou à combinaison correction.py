#Code secret : 123 (mais le programme doit le générer aléatoirement entre 100 et 999)

#Règles :
#1. L'utilisateur a 5 tentatives maximum
# 2. À chaque erreur, affiche un indice :
#    - "Plus grand" ou "Plus petit" pour chaque chiffre
#    - Exemple : Si code=123 et essai=153 → "Chiffre 1 : OK, Chiffre 2 : trop grand, Chiffre 3 : OK"
# 3. Si l'utilisateur échoue 5 fois → "Verrou bloqué pour 30 secondes" (simule avec un compteur)
# 4. Si l'utilisateur réussit → "🎉 Ouvert ! Tentatives : X"

# BONUS : Ajoute un mode "super difficile" où le code change après 3 erreurs !

#RESULTAT

import random
import time 

print("=" * 60)
print("🔐 VERROU À COMBINAISON - Devine le code à 3 chiffres")
print("=" * 60)
print("📌 Règle de déverrouillage :")
print("   - Votre code à 3 chiffre; Votre code est compris entre 100 et 999")
print("   - Tapez 'exit' pour quitter le programme")
print("   - Vous avez 5 tentatives avant blocage")
print (". - En cas de blocage patientez 30 seconde avant de retenter ")
print("=" * 60)

tentative_max=5
partie_en_cours= True

while partie_en_cours :
    
    code_secret= random.randint (100,999)
    print(f"\n🎯 NOUVEAU CODE GÉNÉRÉ !")

    tentative_restante= tentative_max
    code_trouve= False
    #
    while tentative_restante >0 and not       code_trouve :
        saisie= input ('saisissez le code ')
        
        if saisie.lower() == 'exit':
            print ("merci d'avoir jouer👋")
            partie_en_cours= False
            break 
        
        if not saisie.isdigit() or len (saisie) != 3 or int(saisie) <100 or int(saisie)  > 999:
                print ("Le code entrer ne respecte pas les consignes ")
                continue 
         
        essai = int(saisie)

        if essai == code_secret:
            # VICTOIRE !
            code_trouve = True
            print("\n" + "=" * 60)
            print("🎉🎉🎉 FÉLICITATIONS! 🎉🎉🎉")
            print(f" 🔓 CODE {code_secret} TROUVÉ !")
            print(f"💪 Tentatives utilisées : {tentative_max - tentative_restante + 1}")
            print("=" * 60)
            
        else:
            
            print("\n🔍 ANALYSE DU CODE :")
            

            c_centaine = code_secret // 100
            c_dizaine = (code_secret // 10) % 10
            c_unite = code_secret % 10
            
           
            e_centaine = essai // 100
            e_dizaine = (essai // 10) % 10
            e_unite = essai % 10
            
               #Comparaison centaine
            if e_centaine == c_centaine:
                print("   ✅ Centaine : OK")
            elif e_centaine > c_centaine:
                print("   ⬆️ Centaine : Trop grand")
            else:
                print("   ⬇️ Centaine : Trop petit")
            
            # Comparaison dizaine
            if e_dizaine == c_dizaine:
                print("   ✅ Dizaine  : OK")
            elif e_dizaine > c_dizaine:
                print("   ⬆️ Dizaine  : Trop grand")
            else:
                print("   ⬇️ Dizaine  : Trop petit")
            
            # Comparaison unité
            if e_unite == c_unite:
                print("   ✅ Unité    : OK")
            elif e_unite > c_unite:
                print("   ⬆️ Unité    : Trop grand")
            else:
                print("   ⬇️ Unité    : Trop petit")
            
            # Une tentative de moins
            tentative_restante -= 1
            
            # Au cas où aucune tentative n'est bonne 
    if not code_trouve and partie_en_cours:
        print("\n" + "=" * 60)
        print("🔒 VERROUILLAGE DU SYSTÈME !")
        print("=" * 60)
        print(f"Le code secret était : {code_secret}")
        print("\n⏰ DÉCOMPTE DE 30 SECONDES...")
        
        print(f"   ⏳ Déverrouillage dans 30 secondes...", end="\r")
        # Compte à rebours
        for seconde in range(30, 0, -1):
            time.sleep(1)
        
        print("\n" + "=" * 60)
        print("✅ SYSTÈME DÉVERROUILLÉ !")
        print("🔄 GÉNÉRATION D'UN NOUVEAU CODE...")
        print("=" * 60)
    
    
    if partie_en_cours:
        print("\n" + "-" * 60)
        rejouer = input("🎮 Veux-tu rejouer une nouvelle partie ? (répondez non si vous ne rejouerai pas, tapez n'importe quoi d'autre si vous rejouez) : ")
        if rejouer.lower() == 'non':
            print("\n👋 Merci d'avoir joué ! À bientôt.")
            partie_en_cours = False
            print("\n🔐 Programme terminé.")
            
         

print("\n🔐 Programme terminé.")
    