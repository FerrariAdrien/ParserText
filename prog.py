import pathlib
import os 
import sys


#Vérifie si mot a une occurrence dans texte en position i




#titre_doss = input('Choisir nom du dossier \n') 


def xml(titre,preamble,auteur,abstract,biblio,fichier) :
    File = open(titre+".xml",  'w+')
    
    File.write("<?xml version='1.0' standalone='yes' ?>");
    File.write("<article>");
    File.write("<preamble>"+preamble+"</preamble>");
    File.write("<titre>"+titre+"</titre>");
    File.write("<auteur>"+auteur+"</auteur>");
    File.write("<abstract>"+abstract+"</abstract>");
    File.write("<biblio>"+biblio+"</biblio>");
    File.write("</article>");
    
    File.close();
    
    print("<article>")
    print("<preamble>"+preamble+"</preamble>")
    print("<titre>"+titre+"</titre>")
    print("<auteur>"+auteur+"</auteur>")
    print("<abstract>"+abstract+"</abstract>")
    print("<biblio>"+biblio+"</biblio>")
    print("</article>")

      

#titre_doss = input('Choisir nom du dossier \n') 

def recherche(fichier,path):
	texte = fichier.readlines()

    #titre_doss.replace(" ","_")
	#print(titre_doss)

	titre = ""
	auteur = ""
	abstract = ""
	biblio = ""
	head, tail = os.path.split(path)
	tail='.'.join(tail.split('.')[:-1])
	
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
							if not texte[v]=='\n' : titre += texte[v]
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
	xml(titre,str(tail),auteur,abstract,biblio,path)
	#print("-----------Titre-----------\n",titre,"-----------Auteur-----------\n",auteur,"-----------Abstract-----------\n",abstract)


def main ():
	init=0
	for path in pathlib.Path("txt/.").iterdir():
		if path.is_file():
			root, extension = os.path.splitext(path)
			if (extension == '.txt'):
					print (path)
					fichier = open(path,'r')
					recherche(fichier,path)
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
