# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:01:01 2020

@author: Matthis
"""

import cherrypy
import os.path
import matplotlib.pyplot as plt
import os
import datetime
from collections import Counter
import time
cherrypy.engine.stop()
cherrypy.server.httpserver = None
cherrypy.config.update({'server.socket_port': 8099})
cherrypy.engine.start()
#***********************          CLASSES        ******************************************

class CompteFoyer:
    def __init__(self, pseudo, email, password, telephone, adresse, personnes):#personnes->dict
        self.pseudo=pseudo
        self.email=email
        self.password=password
        self.telephone=telephone
        self.adresse=adresse
        self.personnes=personnes  
    def __getitem__(self,i):
        if i ==0:
            return self.pseudo
        if i==1:
            return self.email
        if i==2:
            return self.password
        if i==3:
            return self.telephone
        if i==4:
            return self.adresse
        if i==5:
            return self.personnes
    def __setitem__(self,i,val,key=None):
        if i==0:
            if type(val)==type(self.pseudo):
                self.pseudo=val
        if i==1:
            if type(val)==type(self.email):
                self.email=val
        if i ==2: 
            if type(val)==type(self.password):
                self.password=val
        if i==3:
            if type(val)==type(self.telephone):
                self.telephone=val
        if i==4:
            if type(val)==type(self.adresse):
                self.adresse= val
        if i==5:
            if key!=None:
                if type(key)== type(list(self.personnes.keys())[0]) and type(val)==type(list(self.personnes.values())[0]):
                    self.personnes[key]=val
    def __str__(self):
        return ""+self.pseudo+";"+self.email+";"+self.password+";"+str(self.telephone)+";"+self.adresse+ ";"+str(self.personnes)


class CompteBenevole:
    def __init__(self,login,mdp,nom,prenom,naissance,num,adresse,domainecomp,dispo,permis,vehicule,rayonaction):
        self.login=login
        self.mdp=mdp
        self.nom=nom
        self.prenom=prenom
        self.naissance=naissance
        self.num=num
        self.adresse=adresse
        self.domaincomp=domainecomp
        self.dispo=dispo
        self.permis=permis
        self.vehicule=vehicule
        self.rayonaction=rayonaction
    def __getitem__(self,i):
        if i==0:
            return self.login
        if i==1:
            return self.mdp
        if i==2:
            return self.nom
        if i==3:
            return self.prenom
        if i==4: 
            return self.naissance
        if i==5:
           return self.num
        if i==6:
            return self.adresse
        if i==7:
            return self.domaincomp
        if i==8:
            return self.dispo
        if i==9:
            return self.permis
        if i==10:
            return self.vehicule
        if i==11:
            return self.rayonaction
    def __setitem__(self,i,val):
        # on a des attributs qui ne changeront pas ici 
        if i==1:
            if type(val)==type(self.mdp):
                self.mdp=val
        if i==5:
            if type(val)==type(self.num):
                self.num=val
        if i==7:
            if type(val)==type(self.domaincomp):
                self.domaincomp=val
        if i==8:
            if type(val)==type(self.dispo):
                self.dispo=val
        if i==10:
            if type(val)==type(self.vehicule):
                self.vehicule=val
        if i==11:
            if type(val)==type(self.rayonaction):
                self.rayonaction=val
    def __str__(self):
        return ""+self.login + ";" +self.mdp + ";" + self.nom +";" +self.prenom + ";"+str(self.num)+";"+self.adresse+";"+self.domaincomp + ";"+self.dispo+";"+self.permis+";"+str(self.vehicule)+";"+str(self.rayonaction)+";"+str(self.naissance)
        
class Admin:
    def __init__(self,login,mdp,nom,prenom,telephone,poste,ville):
        self.login=login
        self.mdp=mdp
        self.nom=nom
        self.prenom=prenom
        self.telephone=telephone
        self.poste=poste
        self.ville=ville
        
    def __getitem__(self,i):
        if i ==0:
            return self.login
        if i==1:
            return self.mdp
        if i==2:
            return self.nom
        if i==3:
            return self.prenom
        if i==4:
            return self.telephone
        if i==5:
            return self.poste
        if i==6:
            return self.ville
        
        
    def __setitem__(self,i,val):
        if i==1:
            
            self.mdp=val
        if i==4:
            self.telephone=val
        if i==5:
            self.poste=val    
    def __str__(self):
        return str(self.login)+";"+str(self.mdp)+";"+str(self.nom)+";"+str(self.prenom)+";"+str(self.telephone)+";"+str(self.poste)+";"+str(self.ville)+"\n"


class Produit:
    def __init__(self,nom,marque,type_produit,desc,state,prix): # rajouter des caracteristiques pour un produit
        self.nom=nom
        self.marque=marque
        self.type_produit=type_produit
        self.desc=desc
        self.state=state #-> disponible ou pas
        self.prix=prix
    def __getitem__(self,i):
        if i==0:
            return self.nom
        if i==1:
            return self.marque
        if i==2:
            return self.type_produit
        if i==3:
            return self.desc
        if i==4:
            return self.state
        if i ==5:
            return self.prix
        return 
    def __setitem__(self,i,val):
        if i==0:
            if type(val)==type(self.nom):
                self.nom=val
        if i==1:
            if type(val)==type(self.marque):
                self.marque=val
        if i==2:
            if type(val)==type(self.type_produit):
                self.type_produit=val
        if i==3:
            if type(val)==type(self.desc):
                self.desc=val
        if i==4:
            if type(val)==type(self.state):
                self.state=val
        if i==5:
            if type(val)==type(self.prix):
                self.prix=val          
    def __eq__(self,other):
        if type(other)==type(self):
            return self.nom==other.nom and self.marque==other.marque and self.desc==other.desc and self.type_produit==other.type_produit
    def __str__(self):
        return ""+self.nom+";"+self.marque+";"+self.type_produit+";"+self.desc+";"+self.state+";"+str(self.prix)
   
class Stocks:
    def __init__(self,Liste_produits=None):
        if Liste_produits ==None:
            self.Liste_produits=list()
        else:
            self.Liste_produits=Liste_produits
    def __getitem__(self,i):
        return self.Liste_produits[i]
    
    def __setitem__(self,val,i):
        if type(val)==type(self.Liste_produits[i]):
            self.Liste_produits[i]=val
    def __add__(self,prod):
        if type(prod)==type(Produit):
            self.Liste_produits.append(prod)
            print("element ajoute au catalogue")
    def __sub__(self,prod):
        if type(prod)==type(Produit):
            self.Liste_produits.remove(prod)
            print("element retire du catalogue")        
    def __str__(self):
        produits = ""
        for i in range(len(self.Liste_produits)):
            produits+=str(self.Liste_produits[i])+"\n"
        return produits
  

class Commande:
    def __init__(self,foyer,produits,prix,etat,date):
        self.foyer=foyer
        self.produits=produits
        self.prix=prix
        self.etat=etat
        self.date=date
        
        
    def __getitem__(self,i):
        if i==0:
            return self.foyer
        if i==1:
            return self.produits
        if i==2:
            return self.prix
        if i==3:
            return self.etat
        if i==4:
            return self.date
    
    def __setitem__(self,val,i):
        if i==1:
            self.produits=val
        if i==3:
            self.etat=val
    def __str__(self):
        rep = str(self.foyer)+";" + str(self.produits)+";" + str(self.prix)+";" + str(self.etat)+";" + str(self.date)
        return rep


#******************************       FONCTIONS        ****************************************************
    


def AjoutProduits(prod): 
    f = open('Produits.txt','a')
    f.write(str(prod.nom)+";"+str(prod.marque)+";"+str(prod.type_produit)+";"+str(prod.desc)+";"+str(prod.state)+";"+str(prod.prix)+"\n")
    f.close()

def SupProduit(prod):
    produits = lectureFichierStock()
    for element in produits.Liste_produits:
        if prod == element :
            produits.Liste_produits.remove(element)
    #on doit avoir le meme chemin d'acces que pour importeProudit
    path = 'test'
    os.remove(path)
    file = open(path,'x')
    for element in produits.Liste_produits:
        file.write(str(prod.nom)+";"+str(prod.marque)+";"+str(prod.type_produit)+";"+str(prod.desc)+";"+str(prod.state)+";"+str(prod.prix)+"\n")
    print("Stocks mis a jour")
    file.close()
        
def lectureFichierStock(): 
    f = open(r'Produits.txt','r')
    l = []
    for line in f:
        temp = line.strip()
        l.append(temp)
        #temp = line.strip().split(";")
        #prod = Produit(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
        #l.append(prod)
    #produits = Stocks(l)
    f.close()
    return l

    
    
def AfficherStock():
    produits = lectureFichierStock()
    output='''*********************        Produits      **********************'''
    output+="<br />"
    k=1
    for produit in produits : 
        output+=str(k)+" : "+str(produit)+"<br />"
        k+=1
    output+="******************************************"
    return output

    
def EcritureFichierCommandes(commande):
    f = open(r'Commandes.txt','a')
    if(os.stat(r'Commandes.txt').st_size == 0):
        f.write(str(commande))
    else :
        f.write("\n")
        f.write(str(commande))
    f.close()

def LectureFichierCommandes():
    f = open('Commandes.txt','r')
    commandes = list()
    for line in f :
        temp = line.strip()
        commandes.append(temp)
    f.close()
    return commandes

def afficherCommandes():
    output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
nav {
  float: left;
  width: 30%;
  background: #ccc;
  padding: 20px;
}
</style><header>
*********************        COMMANDES      **********************</header><article>'''
    output+="<br />"
    fichier = LectureFichierCommandes()
    for commande in fichier:
        commandeSep = commande.split(';')
        output+="Foyer : "+ commandeSep[0]+"<br />"
        output+="Produits : "+commandeSep[1]+"<br />"
        output+="Prix : "+commandeSep[2]+"<br />"
        output+="Etat : " +commandeSep[3]+"<br />"
        output+="Date : "+commandeSep[4]+"<br />"
        output+="<br />"+"<br />"
    output+="******************************************************************</article>"
    return output

def afficherCommandesFoyer(foyer=None):
    output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
nav {
  float: left;
  width: 30%;
  background: #ccc;
  padding: 20px;
}
</style><header>
*********************        COMMANDES      **********************</header><article>'''
    output+="<br />"
    fichier = LectureFichierCommandes()
    for commande in fichier:
        commandeSep = commande.split(';')
        if commandeSep[0]==foyer:
            output+="Foyer : "+ commandeSep[0]+"<br />"
            output+="Produits : "+commandeSep[1]+"<br />"
            output+="Prix : "+commandeSep[2]+"<br />"
            output+="Etat : " +commandeSep[3]+"<br />"
            output+="Date : "+commandeSep[4]+"<br />"
            output+="<br />"+"<br />"
    output+="******************************************************************</article>"
    return output


def CommandeNonLivrees():
  commandes=afficherCommandes()
  res = list()
  for commande in commandes:
    if commande.etat!="livree":
      res.append(commande)
  return res



#methodes pour interagir avec la BDD des foyers (en dessous)    
def LectureFichierFoyer():
    f=open(r'Foyers.txt','r')
    liste = []
    for line in f :
        ligne =line.strip()
        liste.append(ligne)
    f.close()
    return liste

def EcritureFichierFoyer(CompteFoyer):
    f = open(r'Foyers.txt','a')
    if(os.stat(r'Foyers.txt').st_size == 0):
        f.write(str(CompteFoyer))
    else :
        f.write("\n")
        f.write(str(CompteFoyer))
    f.close()

def LectureFichierBenevole():
    f=open(r'Bénévoles.txt','r')
    liste = []
    for line in f :
        ligne =line.strip()
        liste.append(ligne)
    f.close()
    return liste

def EcritureFichierBenevole(CompteBenevole):
    f = open(r'Bénévoles.txt','a')
    if(os.stat(r'Bénévoles.txt').st_size == 0):
        f.write(str(CompteBenevole))
    else :
        f.write("\n")
        f.write(str(CompteBenevole))
    f.close

def afficherFoyer():
    fichier = LectureFichierFoyer()
    output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>
<header>*********************        FOYERS      **********************</header><article>'''
    for foyer in fichier:
        foyerSep = foyer.split(";")
        output+="<br />"
        output+="Pseudo : "+foyerSep[0]+"<br />"
        output+="email : "+foyerSep[1]+"<br />"
        output+="Password : "+foyerSep[2]+"<br />"
        output+="Tel : "+foyerSep[3]+"\n"
        output+="Adresse : "+foyerSep[4]+"<br />"
        output+="Membres (et âges correspondant) du foyer  : "+foyerSep[5]+"<br />"
    output+=("<br />")
    output+="******************************************************************</article>"
    return output


def afficherBenevole():
    fichier=LectureFichierBenevole()
    output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>
<header>*********************        Bénévoles      **********************</header><article>'''
    for benevole in fichier:
        benevSep = benevole.split(";")
        output+="<br />"
        output+="Login : "+benevSep[0]+"<br />"
        output+="Mot de passe : "+benevSep[1]+"<br />"
        output+="Nom : "+benevSep[2]+"<br />"
        output+="Prenom : "+benevSep[3]+"<br />"
        output+="Téléphone: "+benevSep[4]+"<br />"
        output+="Adresse: "+benevSep[5]+"<br />"
        output+="Domaine de compétence: "+benevSep[6]+"<br />"
        output+="Disponibilités: "+benevSep[7]+"<br />"
        output+="Permis: "+benevSep[8]+"<br />"
        output+="Véhiculé (1/Oui, 0/Non): "+benevSep[9]+"<br />"
        output+="Rayon d'action: "+benevSep[10]+"<br /><br /><br />"
    output+=("<br />")
    output+="******************************************************************</article>"
    return output


def existeFoyer(pseudo):
    existeDeja = False
    fichier = LectureFichierFoyer()
    for foyer in fichier:
        foyerSep = foyer.split(";")
        if foyerSep[0]==pseudo:
            existeDeja = True
    return existeDeja
        
def passwordFoyer(pseudo,password):
    passwordCorrect = False
    fichier = LectureFichierFoyer()
    for foyer in fichier:
        foyerSep = foyer.split(";")
        if(foyerSep[0]==pseudo and foyerSep[2]==password):
            passwordCorrect = True
    return passwordCorrect

def passwordBenevole(pseudo,password):
    passwordCorrect=False
    fichier=LectureFichierBenevole()
    for benevole in fichier:
        benevoleSep=benevole.split(";")
        if(benevoleSep[0]==pseudo and benevoleSep[1]==password):
            passwordCorrect=True
        return passwordCorrect
    
    
def AfficheDemandesJour(date):
    demandes = afficherCommandes()
    for demande in demandes :
        if demande.date==date:
            print(demande)
    
def AfficheDemandesNb(n):#affiche un graphique du nombre de commandes des n dernier jours
    ajd = datetime.datetime.now()
    first = ajd.timedelta(n)
    firstDate = time.strptime(first, "%d/%m/%Y")
    demandes = afficherCommandes()
    demandes.sort(key = lambda demande:demande.date)
    rep = list()
    for element in demandes:
        if time.strptime(element.date, "%d/%m/%Y")>firstDate:
            rep.append(element.date)
    dico = {}
    for element in rep:
        if element.date in list(dico.keys()):
            dico[element.date]+=1
        else:
            dico[element.date]=1
    
    
    absi=list(dico.keys)
    ordo= list(dico.values)
    width = 1.0
    plt.bar(absi, ordo, width )
    plt.show()
            
def Courses(pseudoFoyer,art1=0,art2=0,art3=0,art4=0,art5=0,qte1=0,qte2=0,qte3=0,qte4=0,qte5=0):                                   
      panier= dict() # produit et quantité
      produits = lectureFichierStock()
      for produit in produits:           
        if int(qte1)>0:
            panier[int(qte1)]= produits[int(art1)]
            prixSep = produits[int(art1)].split(";")
            prix = int(qte1)*int(prixSep[5])
            panier[int(qte1)] = prixSep[0]+" "+prixSep[1]+" "+prixSep[5]+" €"
        if int(qte2)>0:
            panier[int(qte2)]= produits[int(art2)]
            prixSep = produits[int(art2)].split(";")
            prix += int(qte2)*int(prixSep[5])
            panier[int(qte2)] =  prixSep[0]+" "+prixSep[1]+" "+prixSep[5]+" €"
        if int(qte3)>0:
            panier[int(qte3)]= produits[int(art3)]
            prixSep = produits[int(art3)].split(";")
            prix += int(qte3)*int(prixSep[5])
            panier[int(qte3)] =  prixSep[0]+" "+prixSep[1]+" "+prixSep[5]+" €"
        if int(qte4)>0:
            panier[int(qte4)]= produits[int(art4)]
            prixSep = produits[int(art4)].split(";")
            prix += int(qte4)*int(prixSep[5])
            panier[int(qte4)] =  prixSep[0]+" "+prixSep[1]+" "+prixSep[5]+" €"
        if int(qte5)>0:
            panier[int(qte5)]= produits[int(art5)]
            prixSep = produits[int(art4)].split(";")
            prix += int(qte5)*int(prixSep[5])
            panier[int(qte5)] =  prixSep[0]+" "+prixSep[1]+" "+prixSep[5]+" €"    
        
      nouvelleCommande = Commande(pseudoFoyer,panier,prix,"pas livrée",datetime.datetime.now())
      EcritureFichierCommandes(nouvelleCommande)
    

    
    
def Livrer(commande):
    choix= input("La commande est-elle livrée ? (oui/non)")
    if choix == "oui":
        commande.etat="Livree"
    else:
        commande.etat="Non Livree"



def ProduitsPlusDemandes():
    commandes = LectureFichierCommandes()
    produits = []
    for commande in commandes:
        commandeSep = commande.split(";")
        produits_commande = commandeSep[1].split(",")
        if (len(produits_commande) ==1):
            prod = produits_commande[0].split("{")
            prodBis = prod[1]
            prodBis = prodBis.split("}")
            prodBis = prodBis[0]
            prodBis = prodBis.split(":")
            for i in range(int(prodBis[0])):
                produits.append(prodBis[1])
        else :
            prod = produits_commande[0].split("{")
            prodBis = prod[1]
            prodBis = prodBis.split(":")
            for i in range(int(prodBis[0])):
                produits.append(prodBis[1])
            for i in range(1,len(produits_commande)-1):
                prod = produits_commande[i].split(":")
                for i in range(int(prod[0])):
                    produits.append(prod[1])
            prod = produits_commande[len(produits_commande)-1].split("}")
            prodBis = prod[0]
            prodBis = prodBis.split(":")
            for i in range(int(prodBis[0])):
                produits.append(prodBis[1])
    sorted_list= Counter(produits).most_common()
    topProduits = sorted_list[:5]
    res = ""
    classement = 1
    for e in topProduits :
        position =0
        nomProduit=""
        lettresProduit = list(e[0])[1:len(list(e[0]))-4]
        while position<len(lettresProduit):
            nomProduit+=lettresProduit[position]
            position+=1
        nbCommandes = e[1]
        res+="<br /> "+str(classement)+" : "+nomProduit+"        commandé "+str(nbCommandes)+" fois"
        classement+=1
    return res #retourne la liste des 5 produits les plus demandés





class plateformeprojet:
    def index(self):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>
       <header> Bonjour, bienvenue sur notre interface de gestion! </header> <br /><br />
       <article>
        Si vous êtes un foyer, cliquez <a href="particulier" style="color:red">ici</a><br /><br />
        Pour une collectivité, cliquez <a href="collec" style="color:red">ici</a>
        <br /><br /> Si vous êtes un bénévole, cliquez <a href="benevol" style="color:red"> ici </a>
        </article>
        
        '''
        
        return output
    index.exposed=True
    
    
    def particulier(self):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
<a href="identification" style="color:red">Vous avez déjà un compte</a> <br /><br /> <a href="creationfoyer" style="color:red"> Vous souhaitez vous créer un compte foyer</a></header>'''
        
        return output
    particulier.exposed=True
    
    def identification(self):
            output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
            <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Bonjour, saisissez votre pseudo et mot de passe!</header>
             <article><form action="motdepasse" method="POST">
             Identifiant:
        <input type="text" name="pseudo" />
        Mot de passe:
        <input type="password" name="motdepasse" />
        <input type="submit" />
        </form></article>''' 
            return output
    identification.exposed=True
    
    def motdepasse(self,pseudo=None,motdepasse=None):
        if passwordFoyer(pseudo,motdepasse)==True:
            output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
            <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>
<article>
            Bienvenue sur votre interface! que souhaitez-vous faire?
            <a href= "commander"> Commander</a> <br /> <a href="commandesencours ">Voir vos commandes</a></article>''' 
        else:
            output="Pseudo/Mot de passe incorrect."
        return output
    motdepasse.exposed=True
    
    def commander(self,pseudo=None):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Voici les produits disponibles :   </header><article> '''+AfficherStock()
        output+='''<br /> Lorsque votre choix est fait, saisissez uniquement le numéro du ou des articles que vous souhaitez et leur quantité <br /><br />(5 articles différents maximum, si moins de 5 articles, écrivez 0): <br />'''
        output+='''<br /><form action="commande" method="GET">
            Pseudo de votre famille:
        <input type="text" name="pseudo" /> <br />
        Article 1
        <input type="int" name="art1" />
        Quantité? <input type="int" name="qte1" /><br />
        Article 2
        <input type="int" name="art2" />
        Quantité? <input type="int" name="qte2" /><br />
        Article 3
        <input type="int" name="art3" />
        Quantité? <input type="int" name="qte3" /><br />
        Article 4
        <input type="int" name="art4" />
        Quantité? <input type="int" name="qte4" /><br />
        Article 5
        <input type="int" name="art5" />
        Quantité? <input type="int" name="qte5" /><br /><br />
        <input type="submit" />
        </form></article>'''
        return output
    commander.exposed=True
    

     
    def commande(self,pseudo=None,art1=None,art2=None,art3=None,art4=None,art5=None,qte1=None,qte2=None,qte3=None,qte4=None,qte5=None):
        
        output=''' <body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Commande effectuée, <a href="identification"> revenir au menu de connection</a> ou alors <a href="index"> se déconnecter</a></header>
         '''
        Courses(pseudo,art1,art2,art3,art4,art5,qte1,qte2,qte3,qte4,qte5)
        return output
    commande.exposed=True
       
    def commandesencours(self):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
<form action="listecommandefoyer" method="POST">
            Pseudo de votre famille:
        <input type="text" name="pseudo" /> <input type="submit" /></form> </header>
        '''
        return output
    commandesencours.exposed=True
    
    
    def listecommandefoyer(self,pseudo=None):
        output=afficherCommandesFoyer(pseudo)
        return output
    listecommandefoyer.exposed=True
    
    def creationfoyer(self):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
<form action="nouveaucompte" method="POST">
            Pseudo de votre famille:
        <input type="text" name="pseudo" /> 
        <br />Email:
        <input type="email" name="mail" />
        <br />Mot de passe: <input type="password" name="motdepasse" /></header><article>
        <br />Téléphone:
        <input type="text" name="telephone" />
        <br />Adresse: <input type="text" name="adresse" />
        <br />Nombre de personnes dans le foyer:
        <input type="text" name="nbpers" />
        <input type="submit" />
        </article>
        </form>
        '''
        return output
    creationfoyer.exposed=True
    
    def nouveaucompte(self,pseudo=None,motdepasse=None,mail=None,telephone=None,adresse=None,nbpers=None):
        output=''' <body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Compte créé, <a href="identification">connection</a> <br /> <a href="index">Retour au menu</a></header>
        '''
        dicoPersonne={"Nombre de personnes du foyer: ":nbpers}
        nouveauFoyer = CompteFoyer(pseudo,mail,motdepasse,telephone,adresse,dicoPersonne)
        EcritureFichierFoyer(nouveauFoyer)
        return output
    nouveaucompte.exposed=True
    
    
     #Partie comptes bénévoles
     
    def benevol(self):
         output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
         <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
 <a href="identificationbenev">Accéder à votre compte</a> <br /> <br /> <a href="creationbenevole">Créer un compte</a></header>
         '''
         return output
    benevol.exposed=True
    

    def identificationbenev(self):
            output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
            <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Bonjour, saisissez votre pseudo et votre mot de passe!
            
             <form action="motdepassebenev" method="POST">
             Pseudo: <input type="text" name="pseudobenev" />
             <br />mot de passe:
        <input type="password" name="motdepassebenev" />
        <input type="submit" />
        </form></header>''' 
            return output
    identificationbenev.exposed=True
    
    def motdepassebenev(self,pseudobenev=None,motdepassebenev=None):
        if passwordBenevole(pseudobenev,motdepassebenev)==True:
            output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
            <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Bienvenue sur votre interface! que souhaitez-vous faire?</header>'''
        else:
            output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
            <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>Mot de passe incorrect. <a href="identificationbenev"> Veuillez réessayer </a></header>'''
        return output
    motdepassebenev.exposed=True
   
    def creationbenevole(self):
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><article>
<form action="nouveaucomptebenevole" method="POST">
            Login :
        <input type="text" name="pseudo" /> 
        <br /> Mot de passe :
        <input type="password" name="motdepasse" /> 
        <br />Email:
        <input type="email" name="mail" />
        <br />Nom: <input type="text" name="nom" />
        <br />Prénom: <input type="text" name="prenom" />
        <br />Votre date de naissance: <input type="date" name="naissance" />
        <br />Téléphone:
        <input type="text" name="telephone" />
        <br />Adresse: <input type="text" name="adresse" />
        <br />Domaine de compétences ? (Faites une brève description):
        <input type="text" name="domainecomp" />
        <br />Permis(Oui/Non): <input type="text" name="permis" />
        <br />Véhicule (1 si oui, 0 si non): <input type="text" name="vehicule" />
        <br />Rayon d'action en km: <input type="text" name="rayonaction" />
        <br />Vos disponibilités (format JJ JJ JJ JJ): <input type="text" name="dispo" />
        <input type="submit" />
        </form></article>
        '''
        return output
    creationbenevole.exposed=True
    
    def nouveaucomptebenevole(self,pseudo=None,motdepasse=None,mail=None,nom=None,prenom=None,naissance=None,telephone=None,adresse=None,domainecomp=None,permis=None,vehicule=None,rayonaction=None,dispo=None):
        nouveauBenevole=CompteBenevole(pseudo,motdepasse,nom,prenom,str(naissance),str(telephone),adresse,domainecomp,dispo,permis,str(vehicule),rayonaction)
        EcritureFichierBenevole(nouveauBenevole)
        output='''<body style="background: url(https://www.harrymillercorp.com/wp-content/uploads/2018/11/Industrial-Chemical-Blog-Background-for-Harry-Miller-Corp-Index.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
Votre compte à bien été créé, <a href="identificationbenev"> se connecter</a> <br /> <a href="index">Retourner au menu</a></header>
        '''
        return output
    nouveaucomptebenevole.exposed=True
        
    
    #Partie collectivité; correspond à des administrateurs
    def collec(self):
        output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>

        <header>Bonjour, bienvenue sur l'interface collectivité!</header> <br /><br />
       <article> Si vous souhaitez voir les foyers, cliquez <a href="afficherfoyers">ici</a>
        Pour afficher les bénévoles, cliquez <a href="afficherbenev">ici</a>
        <br /><br /> Pour afficher les commandes,cliquez <a href="affichercommande"> ici </a>
        <br /><br /> Pour livrer,cliquez <a href="livraison"> ici </a>
        <br /><br /> Pour gérer,cliquez <a href="gerer"> ici </a></article>
        
        '''
        return output
    collec.exposed=True
    
    
    def afficherfoyers(self):
        output=afficherFoyer()
        return output
    afficherfoyers.exposed=True
    
    def afficherbenev(self):
        output=afficherBenevole()
        return output
    afficherbenev.exposed=True
        
        
    def affichercommande(self):
        output=afficherCommandes()
        return output
    affichercommande.exposed=True
    
    def livraison(self):
        output=afficherCommandes()+''' <nav><br /> Saisir le numéro de la commande à modifier:
            <form action="commandelivree" method="GET">
            <input type="text" name="numcommande" />
            <input type="submit" />
            </form></nav>
        '''
        return output
    livraison.exposed=True
    
    def commandelivree(self,numcommande=None):
        commande=LectureFichierCommandes()
        lignecommande=commande[int(numcommande)]
        if(lignecommande[3]=="livrée"):
            output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
                <style>
                header {
                    padding: 30px;
          text-align: center;
              font-size: 35px;
          color: white;
              } </style>
        <header> Commande déjà livrée! Souhaitez-vous retourner au <a href="index">menu </a> </header>'''
        else:
            
            output=''' <body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
            <style>
            header {
                    padding: 30px;
                    text-align: center;
                    font-size: 35px;
                    color: white;
                    } </style> <header>Livraison effectuée, <a href="index" style="color:red"> retour au menu</a></header>'''
            
        return output
    commandelivree.exposed=True
    
    def gerer(self):
        output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>
<header>
        Que souhaitez-vous faire?
        <a href="affichestock" style="color:red">Afficher le stock</a>
        <br /><br />  <a href="ajoutproduit" style="color:red"> Ajouter un produit </a>
        <br /><br /> <a href="produitdemande" style="color:red">Consulter la liste des produits les plus demandés</a></header>
        '''
        return output
    gerer.exposed=True
    
    def produitdemande(self):
        output='''<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>'''+ProduitsPlusDemandes()+"</header>"
        return output
    produitdemande.exposed=True
    
    
    def affichestock(self):
        output="""<body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style><header>
        """+AfficherStock()+"</header>"
        return output
    affichestock.exposed=True
 
    def AjouterProduitMenu(self,Nom=None,Marque=None,Type=None,Description=None,Etat=None,prix=None):
        output="Votre produit a bien été enregistré, merci!"
        nouveauProduit = Produit(Nom,Marque,Type,Description,Etat,prix)
        AjoutProduits(nouveauProduit)
        return output
    AjouterProduitMenu.exposed=True
    
        
    def ajoutproduit(self):
        output='''
        <body style="background: url(https://oceanoneholding.com/wp-content/uploads/2017/05/admin-background-squashed.jpg);">
        <style>
        header {
        background-color=blue;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
} 
article {
  text-align:center;
  padding: 30px;
  width: 100%;
  font-size: 25px;
  height: 300px; 
  color: white;
}
</style>

            <article>Caractéristiques du produit:
             <form action="AjouterProduitMenu" method="GET">
             Nom:
        <input type="text" name="Nom" />
        Marque:
        <input type="text" name="Marque" />
        Type:
        <input type="text" name="Type" />
        Description:
        <input type="text" name="Description" />
        Etat:
        <input type="text" name="Etat" />
        prix:
        <input type="text" name="prix" />
        <input type="submit" />
        </form></article>''' 
        return output
    ajoutproduit.exposed=True
    
    

configfile=os.path.join(os.path.dirname(__file__),'server.conf')
cherrypy.quickstart(plateformeprojet(),config=configfile)