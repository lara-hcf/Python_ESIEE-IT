from cgitb import text
import csv
import re
from bs4 import BeautifulSoup
import requests

def exo1(text):
    #text= text.lower()
    text= re.sub(r'[^\w\s]','',text)
    dictionaire = text.split()
    ocurrance= {}
    #Reunitialisation dict
    for i in dictionaire: 
        ocurrance[i]= 0
    #Comptage des mots
    for i in dictionaire: 
        for j in ocurrance: 
            if (i==j): 
                ocurrance[i]+=1

    return ocurrance

def exo2(liste_ocurrance,liste_mot_parasite): 
    #liste_mot_parasite = ['la', 'le', 'les','dans','un','une','ces',"ce"]
    new_dict= {}
    alors=""
    
    for key,value in liste_ocurrance.items():
        for i in liste_mot_parasite: 
            if key==i: 
                alors="oui"
                break
        if alors=="oui": 
            alors=""
            continue
        new_dict[key]=value
        
    return new_dict

def exo3(nom_fichier): 
    liste=[]
    with open(nom_fichier, 'r') as file: 
        reader= csv.reader(file, delimiter=';')
        for row in reader: 
            liste+= row
    return liste
        
def exo5(text_html): 
    soup= BeautifulSoup(text_html, 'html.parser')
    new_text= soup.get_text(separator=' ')
    return new_text

def exo6(text, nom_balise, nom_attribut): 
    soupe= BeautifulSoup(text, 'html.parser')
    tags= soupe.findAll(nom_balise)
    liste= []
    for i in tags: 
        attribut= i.get(nom_attribut)
        if attribut: 
            liste.append(attribut)
    return liste

def exo8(lien):
    lien= lien.split("//")
    lien2= lien[1].split("/")
    nom_domaine= lien2[0].split(".",1)
    return nom_domaine[1]

def exo9(nom_domaine, liste_url): 
    liste_not= []
    liste_yes= []
    for i in liste_url: 
        if nom_domaine in i: 
            liste_yes+= i
        else: 
            liste_not+= i
    return [liste_yes]+[liste_not]

def exo10(lien): 
    try: 
        reponse= requests.get(lien)
        if reponse.status_code== 200: 
            return reponse.text
        else: 
            print("Erreur, no 200")
            
    except requests.RequestException as e: 
        print("Erreur, ",e)
    return None

def final_program():
    lien= input("Veuillez entrer le lien: ")
    text_html= exo10(lien)
    nom_domaine= exo8(lien)
    liste_lien_url= exo6(text_html,"a", "href")
    liste_balise_alt= exo6(text_html, "img", "alt")
    text_no_html= exo5(text_html)
    #print(text_no_html)
    liste_mot_cle= exo1(text_no_html)
    liste_mot_parasite= exo3("parasite.csv")
    new_liste_mot_cle= exo2(liste_mot_cle, liste_mot_parasite)
    liste_lien= exo9(nom_domaine, liste_lien_url)
    
    print("Voici les 3 premier mots cles : ")
    compt=0
    for i in new_liste_mot_cle: 
        if compt>=3:
            break
        print(i)
        compt+= 1
        
    print("Puis voici le nombre des liens entrants : ", len(liste_lien[0]))
    print("Nombre de lien sortant: ", len(liste_lien[1]))
    print("Et le nombre de balise alt: ", len(liste_balise_alt))
    
final_program()


