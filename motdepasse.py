

## => grandes parties du programme
# => sous parties du programme


##importations

from random import * #import de random
from tkinter import * #import de tkinter (l'interface graphique)






##fonction mot de passe
def mdpsecure(n):
    '''Génère un mot de passe très sécurisé de longueur n (16 caractère minimum recommandé)'''
    global mdp #variable globale où sera stocké le mot de passe
    for i in range(0,n):
        nb=randint(1,4)#on choisi entre 1 2 3 ou 4 (voir signification ligne 23 , 25 , 27 , 29)
        if nb==1: #caractères minuscules
            mdp=mdp+chr(randint(97,122))
        elif nb==2: #caractères majuscules
            mdp=mdp+chr(randint(65,90))
        elif nb==3: #caractères chiffres
            mdp=mdp+str(randint(0,9))
        elif nb==4: #caractères spéciaux
            mdp=mdp+chr(choice([33,36,37]))


    interfacegraphique2() #appel de l'interface graphique qui affichera le résultat final






def interfacegraphique():
    '''interface graphique principale'''
    ##création de la fenêtre

    root=Tk() #création de la fenêtre principale

    stringinput=IntVar(root) #variable où sera stocké le nombre de caractère du mot de passe qu'on rentrera dans la zone de texte dans la fenêtre

    def verif(): ##NE PAS DEPLACER!!
        '''Fonction vérification qui permet de savoir si la valeur entré dans la zone de texte est valide'''

        if type(stringinput.get())==int and stringinput.get()<=55: #si la valeur est un type int et si il est inférieur à 55 (55 est la longueur maximale du mot de passe)
            root.destroy() # on détruit la fenêtre pour pouvoir afficher la suivante dans la fonction mdpsecure
            mdpsecure(stringinput.get()) #appel de mdpsecure avec la valeur donné par l'utilisateur pour la longueur du mdp

        else: #si la valeur entrée est invalide, ça ferme la fenêtre et ça la remet (autrement dit : rénitialisation de l'interface graphique pour une programmation défensive"
            root.destroy()
            interfacegraphique()



    ##boite
    boite=Frame(root,bg="#6A756F") #layout comportant les composants pour bien les organiser dans la fenêtre

    ##personnalisation de la fenêtre
    root.title("Générateur de mots de passe")
    root.geometry("500x300")
    root.minsize(500,300)
    root.maxsize(500,300)
    root.iconbitmap("logo.ico")
    root.config(background="#6A756F")


    ##composant de la fenêtre

    #label principal
    titre=Label(root,text="Générateur de mots de passe sécurisés",font=("Courrier",15),bg="#6A756F",fg="#EAC50D") #Création du label principal
    titre.pack(side=TOP) #affichage du label

    #label information
    label1=Label(boite,text="Entrez le nombre de caractères désirés \n [16 caractères minimum recommandé pour une sécurité maximale] \n [Pas plus de 55 caractères]"
    ,font=("Courrier",10),bg="#6A756F",fg="#EAC50D")#Label d'information positionné en dessous du label principal
    label1.pack() #affichage du label d'information

    #boite de saisie
    boitedesaise= Entry(boite,bg="White",textvariable=stringinput) #boite de saise où sera saisie la longueur qui sera stocké dans la variable stringinput
    boitedesaise.pack() #affichage de boite de saisie en dessous du label d'information


    #bouton "générer"
    bouton=Button(boite,text="Générer",bg="#EAC50D",command=verif) #Bouton générer qui appelle la fonction vérif
    bouton.pack() #affichage du bouton en dessous de la boite de saisie

    #on fait afficher la boite contenant le bouton et les deux labels
    boite.pack(expand=YES)

    ##afficher
    root.mainloop()







def interfacegraphique2():
    '''interface graphique de fin'''

    ##initialisation de la fenêtre
    root2=Tk()
    boite2=Frame(root2,bg="#6A756F") #Création de la boite qui organise les composants de la fenêtre finale

    ##config de la deuxième fenêtre
    root2.title("Générateur de mots de passe")
    root2.geometry("500x300")
    root2.minsize(500,300)
    root2.maxsize(500,300)
    root2.iconbitmap("logo.ico")
    root2.config(background="#6A756F")

    ##composants de la fenêtre finale

    #label principal
    label3=Label(boite2,text="Voici ton mot de passe sécurisé:",font=("Courrier",15),bg="#6A756F",fg="#EAC50D")
    label3.pack() #affichage du label principal

    #label mot de passe
    resultat=Label(boite2,text=mdp,font=("Courrier",10),bg="#6A756F",fg="#EAC50D")
    resultat.pack() #affichage du mot de passe en dessous du label principal

    #label information
    label4=Label(boite2,text="[Le mot de passe est automatiquement copié]",font=("Courrier",10),bg="#6A756F",fg="#EAC50D")
    label4.pack() #affichage du label information en dessous du mot de passe

    root2.clipboard_append(mdp) #copie automatiquement le mot de passe


    #affichage de la boite
    boite2.pack(expand=YES) #affichage de la boite contenant le label principal et le mot de passe

    ##affichage de la fenêtre finale
    root2.mainloop() ##fin du programme



mdp="" ##initialisation de la variable mot de passe placée ici pour pouvoir l'utiliser dans l'entièreté du code

interfacegraphique() ##début du programme
















