# Écrivez votre code ici !
import csv

#en_tete = ["nom" , "heures_travaillees"]

def extract(nom_du_fichier):
    with open(nom_du_fichier,"r") as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=",")
        for ligne in reader:
            print(ligne)
        
extract("input.csv")


# Ne touchez pas le code ci-dessous
if __name__ == "__min__":
    min()