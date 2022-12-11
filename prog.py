import pathlib
import os 
import sys

#titre_doss = input('Choisir nom du dossier \n') 

def recherche(fichier):
	texte = fichier.readlines()

    #titre_doss.replace(" ","_")
	#print(titre_doss)

	j = 0
	trouver = False
	trouverAuteur = False
	esp = 0
	while (j < len(texte)):
		v=j
		while not trouver :
			print(texte[v],end=" ")
			esp += texte[v].count(" ")
			if ( texte[v]=='\n' or esp > 15 ) :
				trouver = True
			v+=1
        #Nom auteur
		while not trouverAuteur :
			print(texte[v],end=" ")
			if texte[v]=='\n' :
				trouverAuteur = True
			v+=1
		if not texte[j].find("Abstract") :

			n=j
			while(texte[n]!='\n') :
				print(texte[n],end=" ")
				n+=1
			break
		
		j+=1
	print("\n\n")


def main ():
	init=0
	for path in pathlib.Path(".").iterdir():
		if path.is_file():
			root, extension = os.path.splitext(path)
			if (extension == '.txt'):
					print (path)
					fichier = open(path,'r')
					recherche(fichier)
			init+=1



if __name__ == '__main__':
	main();
