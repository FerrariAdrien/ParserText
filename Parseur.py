import pathlib
import os 
import sys

#titre_doss = input('Choisir nom du dossier \n') 
def xml(titre,preamble,auteur,abstract,biblio,fichier) :
    #File = open(fichier,  'w+')
    print("<article>")
    print("<preamble>"+preamble+"</preamble>")
    print("<titre>"+titre+"</titre>")
    print("<auteur>"+auteur+"</auteur>")
    print("<abstract>"+abstract+"</abstract>")
    print("<biblio>"+biblio+"</biblio>")
    print("</article>")

 
def recherche(fichier):
	texte = fichier.readlines()

    #titre_doss.replace(" ","_")
	#print(titre_doss)

	titre = ""
	auteur = ""
	abstract = ""
	j = 0
	trouver = False
	trouverAuteur = False
	esp = 0
	while (j < len(texte)):
		v=j
		while not trouver :
			#Titre 
			i=0
			nbLigne = 0
			trouver = False
			while not trouver : 

				if i>=1 :
					if texte[i].find(',')!=-1 or texte[i].find('\ ')!=-1 or nbLigne>=2 or texte[i].find('Andrei')!=-1 or texte[i].find('Kevin')!=-1 or texte[i].find('Vincent')!=-1 :
						trouver = True
					
					else :
						if texte[i].find('Submit')!=-1 or texte[i].find('Journal')!=-1 or texte[i]=='\n' :
							i+=1
						else :
							titre += texte[v]
							nbLigne+=1
							i+=1
				else : 
					if texte[i].find('\ ')!=-1 or nbLigne>=2 :
						trouver = True
					
					else :
						if texte[i].find('Submit')!=-1 or texte[i].find('Journal')!=-1 or texte[i]=='\n' or texte[i].find('From')!=-1:
							i+=1
						else :
							titre += texte[v]
							nbLigne+=1
							i+=1
		#Nom auteur
		v=i
		while not trouverAuteur :
			if  texte[v+1].find("published")==-1:
				if not texte[v]=='\n' : auteur += texte[v]
			if (texte[v]=='\n' and texte[v+1].find("@")==-1  and texte[v+1].find("\,")==-1 and texte[v+1].find("\ ")==-1 and texte[v+1].count(" ")!=1 and texte[v+1].find("University")==-1 and texte[v+1].find("Laboratory")==-1 and texte[v+1].find("School")==-1) or texte[v+1].find("Abstract")!=-1 or texte[v+1].find("Introduction")!=-1 :
				trouverAuteur = True
			v+=1
		#Abstract
		if not (texte[j].find("Abstract") and texte[j].find("ABSTRACT")):

			n=j
			nbLigne = 0
			while( texte[n]!='\n' or nbLigne<=1) :
				abstract += texte[n]
				n+=1
				nbLigne += 1
				
		if not texte[j].find("References") and texte[j].find("REFERENCES"):
			while (j<len(texte)) :
				if not texte[v]=='\n' : biblio+=texte[j]
				j+=1
			#break
		
		j+=1
	xml(titre,"fichier.txt",auteur,abstract,biblio,path)
	print("-----------Titre-----------\n",titre,"-----------Auteur-----------\n",auteur,"-----------Abstract-----------\n",abstract)


def main ():
	init=0
	for path in pathlib.Path(".").iterdir():
		if path.is_file():
			root, extension = os.path.splitext(path)
			if (extension == '.txt'):
					#print (path)
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
