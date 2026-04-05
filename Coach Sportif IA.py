from numbers import Number

print("="*30,"\nBonjour et bienvenue mon sportif.","\nJe suis là pour te créer un programme d'entraînement personnalisés .","\nPrêt pour nouveau defis? Aller entre tes informartion personnel\n","="*30)



#Sexe
sexe="-"
while sexe.upper() not in ["M","F"]:
    sexe=input("Quel est votre sexe? M pour masculin et F pour Feminin    ")
#Age et verifications
try:
    age = float(input("Age : "))
except ValueError:
    age = -1
    
while (not isinstance(age,Number)) or int(age)<=0:
    try: 
        age =float(input("Age erroné. Veillez rééssayer.Age    :"))
    except ValueError : 
        age=-1




#Poids et verifications
try:
    poids=float(input("Poids    :"))
except ValueError:
    poids=-1
    
while not isinstance(poids,Number) or float(poids)<=0 :
    try:
        poids = float(input("Poids erroné.Veillez rééssayer. Poids    :"))
    except ValueError:
        poids=-1



#taille et verification
try:
    taille=float(input("Taille     :"))
except ValueError:
    taille=-1
    
while not isinstance(taille,Number) or float(taille)<=0 or float(taille)>200:
    try:
        taille = float(input ("Taille erroné. Veillez rééssayer. Taille    :"))
    except ValueError:
        taille=-1
 
 
 
    
#Niveau d'activité et verification
print ("En utilisant uniquement les chiffre, choisissez votre niveau d'activité ","\n1 ---sédentaire","\n2 ---modéré","\n3 ---actif ","\n4 ---très actifs")

try:
    activity=float(input("Niveau d'activité    :"))
except ValueError:
    activity=-1
    
while not isinstance(activity,Number) or int(activity)<=0 or int(activity)>4:
    try:
        activity = float(input("Niveau d'activité erroné. Veillez rééssayer.Niveau d'activité    "))
    except ValueError:
        activity=-1




#objectif et vérification     
print ("En utilisant uniquement les chiffre, choisissez votre objectif ","\n1 ---perte de poids","\n2 ---gagner des muscles","\n3 ---maintenir ")

try:
    objectif=float(input("Objectif    :"))
except ValueError:
    objectif=-1
    
while not isinstance(objectif,Number) or int(objectif)<=0 or int(objectif)>3:
    try:
        objectif = float(input("Objectif erroné. Veillez rééssayer.Niveau d'activité    "))
    except ValueError:
        objectif=-1
        
def analyse (sx,a,p,t,ac,o):
  
    
    IMC=p/t**2
 
# sédentaire = 0
#- modéré = 200
#- actif = 400
#- très actif = 600
    if ac==1:
        activité=0
    elif ac==2:
         activité=200
    elif ac==3:
        activité=400
    else :
        activité=600   

    if sx.upper()=="M":
        calorie =10*p+6.25*(t/100)-5*a + activité
    elif sx.upper()=="F":
        calorie =10*p + 6.25*(t/100)-5*a-161+activité
    
    # Déterminer la catégorie d'IMC
    if IMC < 18.5:
        # SOUS-POIDS
        if o == 1:
            conseil = "⚠️ DANGER : Ne perds pas de poids, consulte un médecin !"
        elif o == 2:
            conseil = "💪 Focus sur la musculation avec protéines"
        else:
            conseil = "🥑 Mange équilibré et fais du sport doux"
        
            
    elif IMC < 25:  # 18.5 - 25
        # POIDS NORMAL
        if o == 1:
            conseil = "🚶‍♂️ Cardio + contrôle alimentaire"
        elif o == 2:
            conseil = "💪 Musculation + protéines"
        else:
            conseil = "🏋️‍♀️ Sport régulier + équilibre"
        
            
    elif IMC < 30:  # 25 - 30
        # SURPOIDS
        if o == 1 :
            conseil = "🔥 Cardio + diète contrôlée"
        elif o == 2 :
            conseil = "🏋️‍♂️ Musculation + cardio modéré"
        else :
            conseil = "🚶‍♀️ Sport régulier + vigilance"
        
            
    else:  # imc >= 30
        # OBÉSITÉ
        if o == 1:
            conseil = "⚠️ Consulte un médecin + cardio adapté"
        elif o == 2:
            conseil = "💪 Musculation légère + cardio"
        else :
            conseil = "🥗 Échange alimentaire + marche"
    
    return conseil,IMC,calorie
    

conseil,IMC,calorie=analyse(sexe,age,poids,taille,activity,objectif)


 # En-tête
print("\n" + "="*40)
print("=== COACH SPORTIF IA ===")
print("="*40)
    
    # Données utilisateur
print("\n📋 DONNÉES UTILISATEUR")
print("-"*30)
print(f"• Âge : {age} ans")
print(f"• Poids : {poids} kg")
print(f"• Taille : {taille} cm")
    
    # Formatage du sexe
if sexe == "M":
    sexe_texte = "Masculin"  
else:
    sexe_texte ="Féminin"
    
print(f"• Sexe : {sexe_texte}")
    
    # niveau d'activité
if activity==1:
    print("• Niveau d'activité: sédentaire")
elif activity==2:
    print("• Niveau d'activité: modéré")
elif activity==3:
    print("• Niveau d'activité: actif")
else:
    print("• Niveau d'activité: très actif")
    
    # Formatage de l'objectif
if objectif ==1:
    print("• Objectif: perte de poids")
elif objectif==2:
    print("• Objectif: gagné des muscles")
else:
    print("• Objectif: maintenir")
    
    # Résultats
    print("\n📊 RÉSULTATS")
    print("-"*30)
    
    

# Déterminer la catégorie avec if
if IMC < 18.5:
    categorie = "Sous-poids"
elif IMC < 25:  # 18.5 - 25
    categorie = "Poids normal"
elif IMC < 30:  # 25 - 30
    categorie = "Surpoids"
else:  # IMC >= 30
    categorie = "Obésité"

# Affichage
print(f"📊 IMC : {IMC:.1f} ({categorie})")

print(f"📊 CALORIE : {calorie:.1f} Kcal ({categorie})")
    
    # Conseil personnalisé
print("\n💡 CONSEILPERSONNALISÉ")
print("-"*30)
print(conseil)
    
    # Pied de page
print("\n" + "="*40)
print("✨ Restez motivé ! ✨")
print("="*40)
 

