###Le Jeu des Actions
###Créé par Rémy Weber et Charles-Augustin Videlaine
###Créé le 30 septembre 2021
###Version du 23 mars 2023

#Importation des modules random, pour générer le prix aléatoire des actions, et math, pour permettre d'arrondir à la partie entière du nombre d'actions achetables
from random import*
from math import*
from time import*
import os

def clear():
  os.system('clear || CLS')
  
#Définition de la fonction quitter, qui permet de quitter le jeu
def quitter():
  clear()
  print("Le jeu va quitter, veuillez patienter.")
  return

#Définition de la variable heure, qui permet d'indiquer l'heure et le jour au joueur, et de l'entrer dans le fichier contenant les scores
heure=strftime("Nous sommes le %d %b %Y, il est %H:%M:%S %Z.\n", localtime())


def menuJeuInfini():
  clear()
  print(heure)
  print('Parfait, vous avez choisi le mode de jeu "Infini".')
  choixDifficulteInfini=input("\nSouhaitez-vous jouer à la version facile (1) ou difficile (2) ? " )
  if choixDifficulteInfini=="1":
    print("\nVous avez choisi le mode facile.")
    jeuInfiniFacile()
  elif choixDifficulteInfini=="2":
    print("\nVous avez choisi le mode difficile.")
    jeuInfiniDifficile()
  else:
    menuJeuInfini()
  

def jeuInfiniFacile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  choixTemps=input('Combien de temps souhaitez-vous jouer (en jours) ? ')
  print('\n')
  choixTempsInt=0
  if choixTemps!='':
    choixTempsInt=int(choixTemps)
    tps=choixTempsInt
  if choixTempsInt>0:
    for i in range(choixTempsInt):
      clear()
      print(heure)
      print("\nJOUR :", i+1)
      valeurEntreprise=randint(15,1050)
      print("Votre compte en banque : ", contanbank,"€ \nLe nombre de jours restants : ", tps-1, " \nLe nombre d'actions que vous possédez : ",nombreActions, " \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      valeurEntreprise2=valeurEntreprise
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2), passer au jour suivant (3) ou revenir au menu principal (4) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        sleep(1)
  
      
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? ")
        choixVendreInt=0
        if choixVendre!='':
          choixVendreInt=int(choixVendre)
        if nombreActions>=choixVendreInt and choixVendreInt>0:
          nombreActions=nombreActions-choixVendreInt
          contanbankModifieBis=contanbank+(choixVendreInt*valeurEntreprise)
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendreInt and choixVendreInt==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")
        sleep(1)
        
      elif choixJeu=="3":
        print("\nLe jour va être passé.")
        sleep(1)
      elif choixJeu=="4":
        tSur=input("\nÊtes-vous sûr de vouloir quitter ? Oui (1) ou Non (Tout le reste) ? ")
        if tSur=="1":
          menu()
        print("D'accord, vous passez au jour suivant.")
        sleep(1)
      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")
        sleep(1)
      tps-=1

      if tps>>0:
        print("\n\n")
    

    if nombreActions>>0:
      print("\nVous avez atteint le dernier jour et il vous reste ",nombreActions," actions... Souhaitez-vous vendre vos actions au dernier prix (",valeurEntreprise,"€) ?",sep='')
      choixVente=int(input("\nSouhaitez-vous vendre (1) ou ne pas vendre (2) ? "))
      if choixVente==1:
        print("\nC'est d'accord !")
        contanbankModifieTer=contanbank+(nombreActions*valeurEntreprise)
        contanbank=contanbankModifieTer
        print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
      elif choixVente==2:
        print("\nC'est d'accord. Tant pis !")
        print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
        quitter()
      else:
        print("\nC'est d'accord. Tant pis !")
        print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
        quitter()
    elif nombreActions==0:
      print("\nFélicitations ! Vous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
  elif choixTempsInt<=0 or choixTemps=='':
    jeuInfiniFacile()


def jeuInfiniDifficile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  choixTemps=input('Combien de temps souhaitez-vous jouer (en jours) ? ')
  print('\n')
  choixTempsInt=0
  if choixTemps!='':
    choixTempsInt=int(choixTemps)
    tps=choixTempsInt
  valeurEntreprise=randint(15,1050)
  if choixTempsInt>0:
    for i in range(choixTempsInt):
      os.system('clear')
      if valeurEntreprise>=15 and valeurEntreprise<=200:
        valeurEntreprise=randint(15,400)
      elif valeurEntreprise>=200 and valeurEntreprise<=400:
        valeurEntreprise=randint(100,500)
      elif valeurEntreprise>=400 and valeurEntreprise<=600:
        valeurEntreprise=randint(300,700)
      elif valeurEntreprise>=600 and valeurEntreprise<=800:
        valeurEntreprise=randint(500,900)
      elif valeurEntreprise>=800 and valeurEntreprise<=1050:
        valeurEntreprise=randint(700,1050)
      print(heure)
      print("\nJOUR :", i+1)
      print("Votre compte en banque : ", contanbank,"€ \nLe nombre de jours restants : ", tps-1, " \nLe nombre d'actions que vous possédez : ",nombreActions, " \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      valeurEntreprise2=valeurEntreprise
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2) ou passer au jour suivant (3) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        sleep(1)

      
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=int(input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? "))
        if nombreActions>=choixVendre and choixVendre>0:
          nombreActions=nombreActions-choixVendre
          contanbankModifieBis=contanbank+(choixVendre*valeurEntreprise)
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendre and choixVendre==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")
        sleep(1)

      elif choixJeu=="3":
        print("\nLe jour va être passé.")
        sleep(1)
        
      elif choixJeu=="4":
        tSur=input("\nÊtes-vous sûr de vouloir quitter ? Oui (1) ou Non (Tout le reste) ? ")
        if tSur=="1":
          menu()
        print("D'accord, vous passez au jour suivant.")
        sleep(1)
      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")
        sleep(1)
      
      tps-=1
      if tps>>0:
        print("\n\n")
    

    if nombreActions>>0:
      print("\nVous avez atteint le dernier jour et il vous reste ",nombreActions," actions... Souhaitez-vous vendre vos actions au dernier prix (",valeurEntreprise,"€) ?",sep='')
      choixVente=int(input("\nSouhaitez-vous vendre (1) ou ne pas vendre (2) ? "))
      if choixVente==1:
        print("\nC'est d'accord !")
        contanbankModifieTer=contanbank+(nombreActions*valeurEntreprise)
        contanbank=contanbankModifieTer
        print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
      elif choixVente==2:
        print("\nC'est d'accord. Tant pis !")
        print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
        quitter()
      else:
       quitter()
    elif nombreActions==0:
      print("\nFélicitations ! Vous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
  elif choixTempsInt<=0 or choixTemps=='':
    jeuInfiniDifficile()

    
def menuJeuMini():
  clear()
  print(heure)
  print('Parfait, vous avez choisi le mode de jeu "Minimum".')
  choixDifficulteMini=input("\nSouhaitez-vous jouer à la version facile (1) ou difficile (2) ? " )
  if choixDifficulteMini=="1":
    print("\nVous avez choisi le mode facile.")
    jeuMinimumFacile()
  elif choixDifficulteMini=="2":
    print("\nVous avez choisi le mode difficile.")
    jeuMinimumDifficile()
  else:
    menuJeuMini()


def jeuMinimumFacile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  argentMini=input("Quelle somme d'argent voulez-vous atteindre ? ")
  jour=0
  argentMiniInt=0
  if argentMini!='':
    argentMiniInt=int(argentMini)
  if argentMiniInt<=1000:
    print('\nVeuillez rentrer un montant supérieur à 1000€.')
    sleep(1)
    jeuMinimumFacile()
  else:
    while contanbank<=argentMiniInt:
      os.system('clear')
      valeurEntreprise=randint(15,1050)
      jour+=1 
      print(heure)
      print("\nJOUR :", jour)
      print("Votre compte en banque : ", contanbank,"€ \nIl vous faut ", argentMiniInt-contanbank,"€ avant de finir le jeu \nVous possédez ",nombreActions,  " actions. \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2) ou passer au jour suivant (3) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie

        
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=int(input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? "))
        if nombreActions>=choixVendre and choixVendre>0:
          nombreActions=nombreActions-choixVendre
          contanbankModifie=contanbank+(choixVendre*valeurEntreprise)
          contanbank=contanbankModifie
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendre and choixVendre==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")
      

      elif choixJeu=="3":
        print("\nLe jour va être passé.\n\n")
      
      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")

    contanbank=contanbankModifie
    if contanbank>>argentMiniInt:
      print("\nVous avez atteint votre objectif de ",argentMiniInt,"€, vous avez même ",contanbank,"€ ! Soit ", contanbank-argentMiniInt,"€ en plus ! Le tout en ", jour," jours. Merci d'avoir joué !", sep="")
    else:
      print("\nVous avez atteint votre objectif de ",argentMiniInt,"€, le tout en ", jour," jours. Merci d'avoir joué !", sep="")
      print(argentMiniInt)
      print(contanbank)


def jeuMinimumDifficile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  argentMini=int(input("Quelle somme d'argent voulez-vous atteindre ? "))
  jour=0
  argentMiniInt=0
  if argentMini!='':
    argentMiniInt=int(argentMini)
  if argentMiniInt<=1000:
    print('\nVeuillez rentrer un montant supérieur à 1000€.')
    sleep(1)
    jeuMinimumDifficile()
  else:
    valeurEntreprise=randint(15,1050)
    while contanbank<=argentMiniInt:
      clear()
      if valeurEntreprise>=15 and valeurEntreprise<=200:
        valeurEntreprise=randint(15,400)
      elif valeurEntreprise>=200 and valeurEntreprise<=400:
        valeurEntreprise=randint(100,500)
      elif valeurEntreprise>=400 and valeurEntreprise<=600:
        valeurEntreprise=randint(300,700)
      elif valeurEntreprise>=600 and valeurEntreprise<=800:
        valeurEntreprise=randint(500,900)
      elif valeurEntreprise>=800 and valeurEntreprise<=1050:
        valeurEntreprise=randint(700,1050)
      jour+=1 
      print(heure)
      print("\nJOUR :", jour)
      print("Votre compte en banque : ", contanbank,"€ \nIl vous faut ", argentMiniInt-contanbank,"€ avant de finir le jeu \nVous possédez ",nombreActions,  " actions. \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2) ou passer au jour suivant (3) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie

        
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=int(input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? "))
        if nombreActions>=choixVendre and choixVendre>0:
          nombreActions=nombreActions-choixVendre
          contanbankModifie=contanbank+(choixVendre*valeurEntreprise)
          contanbank=contanbankModifie
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendre and choixVendre==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")
      

      elif choixJeu=="3":
        print("\nLe jour va être passé.\n\n")
      
      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")

    contanbank=contanbankModifie
    if contanbank>>argentMiniInt:
      print("\nVous avez atteint votre objectif de ",argentMiniInt,"€, vous avez même ",contanbank,"€ ! Soit ", contanbank-argentMiniInt,"€ en plus ! Le tout en ", jour," jours. Merci d'avoir joué !", sep="")
    else:
      print("\nVous avez atteint votre objectif de ",argentMiniInt,"€, le tout en ", jour," jours. Merci d'avoir joué !", sep="")


def menuJeuSansLim():
  clear()
  print(heure)
  print('Parfait, vous avez choisi le mode de jeu "Sans limite".')
  choixDifficulteSansLim=input("\nSouhaitez-vous jouer à la version facile (1) ou difficile (2) ? " )
  if choixDifficulteSansLim=="1":
    print("\nVous avez choisi le mode facile.")
    jeuSansLimFacile()
  elif choixDifficulteSansLim=="2":
    print("\nVous avez choisi le mode difficile.")
    jeuSansLimDifficile()
  else:
    menuJeuSansLim()

def jeuSansLimFacile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  choixJeu=0
  jour=1
  while choixJeu!=4:
      os.system('clear')
      print("\n",heure)  
      print("\nJOUR :", jour)
      valeurEntreprise=randint(15,1050)
      print("Votre compte en banque : ", contanbank,"€ \nLe nombre d'actions que vous possédez : ",nombreActions, " \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      valeurEntreprise2=valeurEntreprise
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2), passer au jour suivant (3) ou quitter le jeu (4) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie


      
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=int(input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? "))
        if nombreActions>=choixVendre and choixVendre>0:
          nombreActions=nombreActions-choixVendre
          contanbankModifieBis=contanbank+(choixVendre*valeurEntreprise)
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendre and choixVendre==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")

      elif choixJeu=="3":
        print("\nLe jour va être passé.")
      elif choixJeu=="4":
        if nombreActions==0:
          print("\nFélicitations ! Vous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
          quitter()
        elif nombreActions>>0:
          print("\nVous avez choisi de quitter le jeu et il vous reste ",nombreActions," actions... Souhaitez-vous vendre vos actions au dernier prix (",valeurEntreprise,"€) ?",sep='')
          choixVente=int(input("\nSouhaitez-vous vendre (1) ou ne pas vendre (2) ? "))
          if choixVente==1:
            print("\nC'est d'accord !")
            contanbankModifieTer=contanbank+(nombreActions*valeurEntreprise)
            contanbank=contanbankModifieTer
            print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
            quitter()
          elif choixVente==2:
            print("\nC'est d'accord. Tant pis !")
            print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
            quitter()
          else:
            quitter()
    
      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")
      
      jour+=1
    

def jeuSansLimDifficile():
  clear()
  print(heure)
  contanbank=1000
  nombreActions=0
  choixJeu=0
  jour=1
  valeurEntreprise=randint(15,1050)
  while choixJeu!=4:
      clear()
      if valeurEntreprise>=15 and valeurEntreprise<=200:
        valeurEntreprise=randint(15,400)
      elif valeurEntreprise>=200 and valeurEntreprise<=400:
        valeurEntreprise=randint(100,500)
      elif valeurEntreprise>=400 and valeurEntreprise<=600:
        valeurEntreprise=randint(300,700)
      elif valeurEntreprise>=600 and valeurEntreprise<=800:
        valeurEntreprise=randint(500,900)
      elif valeurEntreprise>=800 and valeurEntreprise<=1050:
        valeurEntreprise=randint(700,1050)
      print(heure)
      print("\nJOUR :", jour)
      print("Votre compte en banque : ", contanbank,"€ \nLe nombre d'actions que vous possédez : ",nombreActions, " \nLes actions de l'entreprise sont aujourd'hui élevées à ", valeurEntreprise,"€", sep="")
      valeurEntreprise2=valeurEntreprise
      choixJeu=input("\nSouhaitez-vous acheter des actions (1), vendre des actions (2), passer au jour suivant (3) ou quitter le jeu (4) ? ")
      if choixJeu=="1":
        actionsAchetables=floor(contanbank/valeurEntreprise)
        print("\nVous pouvez acheter jusqu'à ", actionsAchetables, " action(s).",sep='')
        choixAchat=int(input("\nCombien d'actions voulez-vous donc acheter (tapez -1 pour toutes les acheter) ? "))
        if choixAchat>actionsAchetables:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat<=-2:
          print("\nMalheureusement, cette action est impossible...")
        elif choixAchat==-1:
          nombreActions=nombreActions+actionsAchetables
          contanbankModifie=contanbank-(actionsAchetables*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie
        elif choixAchat>>0:
          nombreActions=nombreActions+choixAchat
          contanbankModifie=contanbank-(choixAchat*valeurEntreprise)
          print("Vous possédez désormais ", nombreActions, " actions.\nIl vous reste maintenant ",contanbankModifie,"€.",sep='')
          contanbank=contanbankModifie


      
      elif choixJeu=="2" and nombreActions>0:
        print("\nVous possédez ",nombreActions," actions, leur valeur du jour est de ", valeurEntreprise,'€, vous pouvez gagner un maximum de ', nombreActions*valeurEntreprise,'€.',sep='')
        choixVendre=int(input("\nCombien d'actions souhaitez-vous vendre (tapez -1 pour tout vendre) ? "))
        if nombreActions>=choixVendre and choixVendre>0:
          nombreActions=nombreActions-choixVendre
          contanbankModifieBis=contanbank+(choixVendre*valeurEntreprise)
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        elif nombreActions>=choixVendre and choixVendre==-1:
          contanbankModifieBis=contanbank+(nombreActions*valeurEntreprise)
          nombreActions=0
          contanbank=contanbankModifieBis
          print("Il vous reste ", nombreActions, " actions.\nVous possédez désormais ",contanbank,"€.",sep='')
        else:
          print("\nMalheureusement, cette action est impossible...")

      elif choixJeu=="3":
        print("\nLe jour va être passé.")
      elif choixJeu=="4":
        if nombreActions==0:
          print("\nFélicitations ! Vous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
          quitter()
        elif nombreActions>>0:
          print("\nVous avez choisi de quitter le jeu et il vous reste ",nombreActions," actions... Souhaitez-vous vendre vos actions au dernier prix (",valeurEntreprise,"€) ?",sep='')
          choixVente=int(input("\nSouhaitez-vous vendre (1) ou ne pas vendre (2) ? "))
          if choixVente==1:
            print("\nC'est d'accord !")
            contanbankModifieTer=contanbank+(nombreActions*valeurEntreprise)
            contanbank=contanbankModifieTer
            print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
            quitter()
          elif choixVente==2:
            print("\nC'est d'accord. Tant pis !")
            print("\nVous avez fini le jeu avec ",contanbank,"€ en poche !",sep='')
            quitter()
          else:
            quitter()

      else:
        print("\nLe nombre saisi n'est pas correct, le jour va être passé...")
      
      jour+=1


def regles():
  clear()
  print("Bienvenue dans les règles du Jeu des Actions.")
  print("\nPour lire les règles du mode de jeu Infini, tapez 1; pour les règles du mode de jeu Fini, tapez 2. Pour les règles du jeu sans limite, tapez 3. Enfin, pour les crédits, veuillez taper 4.")
  choixRegles=input("\nQue souhaitez-vous savoir ? ")
  clear()
  if choixRegles=='1':
    choixDiffJeuReg=input("Souhaitez-vous les règles du mode de jeu Facile (1) ou du mode de jeu Difficile (2) ? ")
    if choixDiffJeuReg=='1':
      clear()
      print("D'accord, voici les règles du mode de jeu Facile pour le mode de jeu Infini.")
      print("\n1. Votre but est de vous faire un maximum d'argent, en un minimum de temps défini au lancement du jeu, et qui ne peut être changée qu'en redémarrant le jeu.\n2. Le mode de jeu est appelé 'Facile', car la génération de la valeur des actions est très aléatoire. Celles-ci peuvent varier rapidement d'un moment à un autre, et vous permettent ainsi d'atteindre plus rapidement votre objectif. Cependant, ceci ne représente pas correctement la réalité. Pour plus de réalisme, veuillez utiliser la version 'Difficile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€. Le montant minimum définissable est de 1001€. Il n'y a pas de maximum.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetour=input("\nSouhaitez-vous retourner au menu (1) ou quitter(2) ? ")
      if choixRetour=="1":
        menuSansBienvenue()
      else:
        quitter()

    elif choixDiffJeuReg=='2':
      clear()
      print("D'accord, voici les règles du mode de jeu Difficile pour le mode de jeu Infini.")
      print("\n1. Votre but est de vous faire un maximum d'argent, en un minimum de temps défini au lancement du jeu, et qui ne peut être changée qu'en redémarrant le jeu.\n2. Le mode de jeu est appelé 'Difficile', car la génération de la valeur des actions est beaucoup plus contrôlée. Celles-ci varient peu, ce qui ajoute du réalisme, mais également de la difficulté. Veuillez noter que toutes les générations restent cependant aléatoires. Pour plus d'amusement, veuillez utiliser la version 'Facile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité.\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€. Le montant minimum définissable est de 1001€. Il n'y a pas de maximum.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetourMenu2=input("\nSouhaitez-vous retourner au menu (1) ou quitter (2) ? ")
      if choixRetourMenu2=="1":
        menuSansBienvenue()
      elif choixRetourMenu2=="2":
        quitter()
      else:
        regles()

    else:
      regles()

  elif choixRegles=='2':
    choixDiffJeuReg2=input("Souhaitez-vous les règles du mode de jeu Facile (1) ou Difficile (2) ? ")
    if choixDiffJeuReg2=='1':
      clear()
      print("D'accord, voici les règles du mode de jeu Facile pour le mode de jeu en argent minimum.")  
      print("\n1. Votre but est de vous faire un maximum d'argent, selon une somme que vous avez définie au lancement du jeu, et qui ne peut être changée qu'en redémarrant le jeu.\n2. Le mode de jeu est appelé 'Facile', car la génération de la valeur des actions est très aléatoire. Celles-ci peuvent varier rapidement d'un moment à un autre, et vous permettent ainsi d'atteindre plus rapidement votre objectif. Cependant, ceci ne représente pas correctement la réalité. Pour plus de réalisme, veuillez utiliser la version 'Difficile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€. Le montant minimum définissable est de 1001€. Il n'y a pas de maximum.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetourMenu=input("\nSouhaitez-vous retourner au menu (1) ou quitter (2) ? ")
      if choixRetourMenu=="1":
        menuSansBienvenue()
      elif choixRetourMenu=="2":
        quitter()
      else:
        regles()

    elif choixDiffJeuReg2=='2':
      clear()
      print("D'accord, voici les règles du mode de jeu Difficile pour le jeu en argent minimum.")
      print("\n1. Votre but est de vous faire un maximum d'argent, selon une somme que vous avez définie au lancement du jeu, et qui ne peut être changée qu'en redémarrant le jeu.\n2. Le mode de jeu est appelé 'Difficile', car la génération de la valeur des actions est beaucoup plus contrôlée. Celles-ci varient peu, ce qui ajoute du réalisme, mais également de la difficulté. Veuillez noter que toutes les générations restent cependant aléatoires. Pour plus d'amusement, veuillez utiliser la version 'Facile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité.\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€. Le montant minimum définissable est de 1001€. Il n'y a pas de maximum.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetourMenu2=input("\nSouhaitez-vous retourner au menu (1) ou quitter (2) ? ")
      if choixRetourMenu2=='1':
        menuSansBienvenue()
      elif choixRetourMenu2=='2':
        quitter()
      else:
        regles()
    else:
      regles()
  elif choixRegles=='3':
    choixDiffJeuReg=input("Souhaitez-vous les règles du mode de jeu Facile (1) ou du mode de jeu Difficile (2) ? ")
    if choixDiffJeuReg=='1':
      clear()
      print("D'accord, voici les règles du mode de jeu Facile pour le jeu sans limite.")
      print("\n1. Votre but est de vous faire un maximum d'argent, sans aucune limite de temps ou d'argent !\n2. Le mode de jeu est appelé 'Facile', car la génération de la valeur des actions est très aléatoire. Celles-ci peuvent varier rapidement d'un moment à un autre, et vous permettent ainsi d'atteindre plus rapidement votre objectif. Cependant, ceci ne représente pas correctement la réalité. Pour plus de réalisme, veuillez utiliser la version 'Difficile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité.\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetour=input("\nSouhaitez-vous retourner au menu (1) ou quitter(2) ? ")
      if choixRetour=='1':
        menuSansBienvenue()
      elif choixRetour=='2':
        quitter()
      else:
        regles()

    elif choixDiffJeuReg=='2':
      clear()
      print("D'accord, voici les règles du mode de jeu Difficile pour le jeu sans limite.")
      print("\n1. Votre but est de vous faire un maximum d'argent, sans aucune limite de temps ou d'argent !\n2. Le mode de jeu est appelé 'Difficile', car la génération de la valeur des actions est beaucoup plus contrôlée. Celles-ci varient peu, ce qui ajoute du réalisme, mais également de la difficulté. Veuillez noter que toutes les générations restent cependant aléatoires. Pour plus d'amusement, veuillez utiliser la version 'Facile'.\n3. Il est IMPOSSIBLE de revendre plus d'actions que ce que l'on possède, d'en acheter plus que ce que l'on peut, ou d'en vendre un nombre négatif pour gagner de l'argent. Tout essai de ce type vous fera directement passer au jour suivant, et perdre une probable belle opportunité.\n4. La valeur originelle de votre compte en banque est de 1000€ Les actions peuvent varier entre 15 et 1050€.\n5. Veuillez n'entrer que les caractères préconisés lors des demandes de l'interface. Toute autre caractère que celui présenté fera planter le jeu.\n6. Amusez-vous ! Le but de ce jeu est que vous vous amusiez, que vous passiez le temps... Profitez !\n\nD'autres mises à jour arriveront, n'oubliez pas de maintenir votre jeu à jour (Vérifiez votre version régulièrement et, le cas échéant, remplacez le fichier, le jeu ne garde rien en mémoire.)")

      choixRetourMenu2=input("\nSouhaitez-vous retourner au menu (1) ou quitter (2) ? ")
      if choixRetourMenu2==1:
        menuSansBienvenue()
      elif choixRetourMenu2=='2':
        quitter()
      else:
        regles()

    else:
      regles()

  elif choixRegles=='4':
    print("CRÉDITS :\nLe Jeu Des Actions,\nun jeu créé et développé par Rémy Weber et Charles-Augustin Videlaine.\nPÉRIODE 2021-2023.\nCréé sur le site 'https://replit.com'.\nNon-libre de droits.\nVERSION LITE BÊTA 1.0.0.") 
 
    choixRetourMenu3=input("\nSouhaitez-vous retourner au menu (1) ou quitter (2) ? ")
    if choixRetourMenu3=='1':
      menuSansBienvenue()
    elif choixRetourMenu3=='2':
      quitter()
    else:
      regles()

  else:
    regles()
  
def menuSansBienvenue():
    clear()
    choixmenu=input('Souhaitez-vous commencer une partie en jours finis (1), une partie en argent minimum (2) ou une partie sans limite (3), ou lire les règles (4) ? ')
    if choixmenu=="1":
        menuJeuInfini()
    elif choixmenu=="2":
        menuJeuMinimum()
    elif choixmenu=="3":
      menuJeuSansFin()
    elif choixmenu=="4":
      regles()
    else:
      menuSansBienvenue()

#Définition de la fonction menu, qui affiche le menu de démarrage et les différents choix de jeu possibles (à compléter)
def menu():
  clear()
  for i in range(1):
    clear()
    print('                                   Bienvenue dans...\n')
    sleep(0.5)
    print("Le Jeu des Actions !")
  choixmenu=input('\n\nSouhaitez-vous commencer une partie en jours finis (1), une partie en argent minimum (2), une partie sans limite (3) ou lire les règles (4) ? ')
  
  if choixmenu=="1":
    menuJeuInfini()
  elif choixmenu=="2":
    menuJeuMini()
  elif choixmenu=="3":
    menuJeuSansLim()
  elif choixmenu=="4":
    regles()
  else:
    menu()

menu()
