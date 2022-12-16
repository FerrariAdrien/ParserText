import pathlib
import os 
import sys

#titre_doss = input('Choisir nom du dossier \n') 


def xml(str,type,fichier) :
    File = open(fichier ,  'un')
    if (type.find("preamble")):
        File.write("<article>")
        File.write("<"+type+">"+str+"</"+type+">")
    elif (type.find("biblio")) :
        File.write("<"+type+">"+str+"</"+type+">")
        File.write("</article>")
    else :
        File.write("<"+type+">"+str+"</"+type+">")

      

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
			#Titre 
			i=0
			nbLigne = 0
			trouver = False
			while not trouver : 

				if i>=1 :
					if texte[i].find(',')!=-1 or texte[i].find('\ ')!=-1 or nbLigne>=2 or texte[i].find('Andrei')!=-1 or texte[i].find('Kevin')!=-1 or texte[i].find('Vincent')!=-1 :
						trouver = True
						print("Auteur(s) : ")
					
					else :
						if texte[i].find('Submit')!=-1 or texte[i].find('Journal')!=-1 or texte[i]=='\n' :
							i+=1
						else :
							print(texte[i])
							nbLigne+=1
							i+=1
				else : 
					if texte[i].find('\ ')!=-1 or nbLigne>=2 :
						trouver = True
						print("Auteur(s) : ")
					
					else :
						if texte[i].find('Submit')!=-1 or texte[i].find('Journal')!=-1 or texte[i]=='\n' or texte[i].find('From')!=-1:
							i+=1
						else :
							print(texte[i])
							nbLigne+=1
							i+=1
		#Nom auteur
		v=i
		while not trouverAuteur :
			if  texte[v+1].find("published")==-1:
				print(texte[v],end=" ")
			if (texte[v]=='\n' and texte[v+1].find("@")==-1  and texte[v+1].find("\,")==-1 and texte[v+1].find("\ ")==-1 and texte[v+1].count(" ")!=2 and texte[v+1].find("University")==-1 and texte[v+1].find("School")==-1) or texte[v+1].find("Abstract")!=-1 or texte[v+1].find("Introduction")!=-1 :
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
