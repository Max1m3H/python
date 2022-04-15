#
#Hamming
#
C1=input("Veuillez entrer un nombre binaire sur 7 ou 11 bits :")

if len(C1)==7:
    codage()
    demande=input("Voulez vous décoder ce mot binaire pour vérifier le résultat ? Oui = 1, Non = 2: ")
    if demande==1:
        decodage()
elif len(C1)==11:
    decodage()
else:
    print("Nombre de bit non valide, veuillez recommencer")
    

def codage(C1, Num=['0011','0101','0110','0111','1001','1010','1011'], C=[], erreur=0):
    """Permet d'effectuer un codage de Hamming sur un mot binaire de 7 bits"""

    #Verification longueur

    if len(C1)!=7:  #Si le nombre de bits est différents de 7, arrête le programme
        print("erreur: le nombre entré n'est pas sur 7 bits")  #Renvoie la cause de l'arrêt du programme
        erreur=1  #Compteur permettant de stopper le programme si différent de 0


    #Verification bit
    
    for i in range(7):  #Parcours du nombre binaire 
        if C1[i] != '1' and C1[i]!= '0':  #Si un chiffre différent de 0 et 1 présent, arrête le programme
            print("erreur: le nombre entré n'est pas en binaire")  #Renvoie la cause de l'arrêt du programme
            erreur=1  #Compteur permettant de stopper le programme si différent de 0


    #Si tout erreur = 0
        
    if erreur==0:  #Si aucune erreur n'est survenue, le programme continue
        for i in range(7):  #Parcours du nombre binaire
            if C1[i]=='1':  #Si un bit rencontré equivaut à 1
                C.append(Num[i])  #Ajoute a la liste vide C la valeur binaire correspondant a i, stockée dans la liste Num
                

        #Création des variables permettant le codage de Hamming
                
        x1=0
        x2=0
        x3=0
        x4=0
        

        #Permet de determiner le nombre de bits egaux à 1, pour une position donnée
        
        for i in range(len(C)):  #En fonction de la longueur de la liste C
            x1=x1+int(C[i][0])  #Pour la variable x1
            x2=x2+int(C[i][1])  #Pour la variable x2
            x3=x3+int(C[i][2])  #Pour la variable x3
            x4=x4+int(C[i][3])  #Pour la variable x4
        
        print(f"x1: {x1}, x2: {x2}, x3: {x3}, x4: {x4}") #Test des valeures de x obtenues

        
        #On effectue une oppération 'ou exclusif' pour chaques valeures x obtenues
        
        x1=x1%2  #Pour obtenir le bit x1
        x2=x2%2  #Pour obtenir le bit x2
        x3=x3%2  #Pour obtenir le bit x3
        x4=x4%2  #Pour obtenir le bit x4

        print(f"x1: {x1}, x2: {x2}, x3: {x3}, x4: {x4}") #Test des bits obtenues
        

        #Inversion de la liste afin d'obtenir les placement désiré

        C1=list(C1)  #Transformation de la variable C1 en liste
        C1.reverse()  #Inversion de la liste


        #Insertion des bits x dans le mot binaire aux positions définies préalablement
        
        C1[3:3]=[str(x1)]  #Insertion en position 3 de la liste
        C1[7:7]=[str(x2)]  #Insertion en position 7 de la liste
        C1[9:9]=[str(x3)]  #Insertion en position 9 de la liste
        C1[10:10]=[str(x4)]  #Insertion en position 10 de la liste

        C1="".join(C1)  #Transforme la liste C1 en chaine de charactères 


        return f"Après le codage de Hamming, nous obtenons le mot binaire {C1}"  #affichage du résultat
    

def decodage(C1):
    "Permet de décoder un codage de Hamming"

    C1=list(C1)

    if len(C1)!=11:  #Si le nombre de bits est différents de 11, arrête le programme
        print("erreur: le mot binaire à décoder n'est pas sur 11 bits")  #Renvoie la cause de l'arrêt du programme
        erreur=1  #Compteur permettant de stopper le programme si différent de 0 
    
    for i in range(11):  #Parcours du nombre binaire 
        if C1[i] != '1' and C1[i]!= '0':  #Si un chiffre différent de 0 et 1 présent, arrête le programme
            print("erreur: le nombre entré n'est pas en binaire")  #Renvoie la cause de l'arrêt du programme
            erreur=1  #Compteur permettant de stopper le programme si différent de 0

    if erreur==0:  #Si aucune erreur n'est survenue, le programme continue
        del(C1[3], C1[7], C1[9], C1[10])
        C1.reverse()  #Inversion de la liste
        C1="".join(C1)  #Transforme la liste C1 en chaine de charactères
        return f"Après le décodage de Hamming, nous obtenons le mot binaire {C1}"  #affichage du résultat
        



    
