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
    while (j < len(texte)):
        v=j
        while not trouver : 
            print(texte[v])
            if texte[v]=='\n' :
                trouver = True
            v+=1
        if not texte[j].find("Abstract") :

            n=j
            while(texte[n]!='\n') :
                print(texte[n])
                n+=1
            break
        
        j+=1
    print("\n\n\n")


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

def test(argv,taille):
	if ( taille < 2 ):
		print("Argument manquant.")
		return 1
		
	if ( argv[1] != "-t" and argv[1] != "-x" ) :
		print("Argument non reconnu : ",argv[1]," (deux possibilitées : -t ou -x).")
		return 1
	return 0

if __name__ == '__main__':
	e = test(sys.argv,len(sys.argv))
	if ( e == 0 ):
		main();
