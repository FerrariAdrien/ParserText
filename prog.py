import pathlib
import os 
import sys


#Vérifie si mot a une occurrence dans texte en position i




#titre_doss = input('Choisir nom du dossier \n') 
def txt(titre,preamble,auteur,abstract,biblio,fichier,intro,corps,conclusion,discussion) :
    File = open(preamble+".txt",  'w+')


    File.write(preamble+"\n\n");
    File.write(titre+"\n\n");
    File.write(auteur+"\n\n");
    File.write(abstract+"\n\n");
    File.write(intro+"\n\n");
    File.write(corps+"\n\n");
    File.write(conclusion+"\n\n");
    File.write(discussion+"\n\n");
    File.write(biblio+"\n\n");

    File.close();

    print(preamble+"\n\n")
    print(titre+"\n\n")
    print(auteur+"\n\n")
    print(abstract+"\n\n")
    print(intro+"\n\n")
    print(corps+"\n\n")
    print(conclusion+"\n\n")
    print(discussion+"\n\n")
    print(biblio+"\n\n")

def xml(titre,preamble,auteur,abstract,biblio,fichier,intro,corps,conclusion,discussion) :
    #File = open(fichier,  'w+')

	File = open(preamble+".xml",  'w+')
	File.write("<?xml version='1.0' standalone='yes' ?>");
	File.write("<article>\n");
	File.write("<preamble>"+preamble+"</preamble>\n");
	File.write("<titre>"+titre+"</titre>\n");
	File.write("<auteur>"+auteur+"</auteur>\n");
	File.write("<abstract>"+abstract+"</abstract>\n");
	File.write("<introduction>"+intro+"</introduction>\n");
	File.write("<corps>"+corps+"</corps>\n");
	File.write("<conclusion>"+corps+"</conclusion>\n");
	File.write("<discussion>"+discussion+"</discussion>\n");
	File.write("<biblio>"+biblio+"</biblio>\n");
	File.write("</article>\n");
	File.close();
	"""
	    print("<article>")
    print("<preamble>"+preamble+"</preamble>")
    print("<titre>"+titre+"</titre>")
    print("<auteur>"+auteur+"</auteur>")
    print("<abstract>"+abstract+"</abstract>")
    print("<biblio>"+biblio+"</biblio>")
    print("</article>")

	
	
	"""

      

#titre_doss = input('Choisir nom du dossier \n') 

def recherche(fichier,path,type_fich):
	texte = fichier.readlines()

    #titre_doss.replace(" ","_")
	#print(titre_doss)
	type = ''
	corps=""
	titre = ""
	auteur = ""
	abstract = ""
	biblio = ""
	intro =""
	discussion = ""
	conclusion =""
	head, tail = os.path.split(path)
	trouverIntro = False
	j = 0
	trouver = False
	trouverAuteur = False
	trouverCorps = False
	trouverD = False
	trouverC = False
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
		#intro
		if texte[j].find("Introduction")!=-1 or texte[j].find("introduction")!=-1 or texte[j].find("INTRODUCTION")!=-1 or texte[j].find("I NTRODUCTION")!=-1:
			d=j
			
			d+=1
			
			while(not trouverIntro) :
				if texte[d].startswith("2") and len(texte[d])==2 and len(texte[d+2].split(' '))<7:
				
					trouverIntro = True
				elif texte[d].startswith("II.") :
					trouverIntro = True
				elif texte[d].startswith("2") and len(texte[d])==3 and len(texte[d+2].split(' '))<7 :
					trouverIntro = True
				elif texte[d].find('Method')!=-1 :
					
					trouverIntro = True
				elif texte[d].startswith("2") and len(texte)==1:
					trouverIntro = True
				elif texte[d].find("2. ")!=-1 :
					trouverIntro=True
				elif texte[d].startswith("2 "):
					trouverIntro=True
				elif texte[d].find("II.")!=-1 :
					trouverIntro=True
				else :
					intro+=texte[d]
					#print(texte[d])
					d+=1
			j=d
		#corps
		
		if trouver and trouverIntro and trouverAuteur :
			v=j
			while not trouverCorps:

				if texte[v].find("Conclusion")!=-1 or texte[v].find("CONCLUSIONS")!=-1 or texte[v].find("C ONCLUSIONS")!=-1:
					print("c")
					type = 'c'
					trouverCorps = True
				elif texte[v].find("Discussion")!=-1 and len(texte[v].split(' '))<3:
					print("d")
					type = 'd'
					trouverCorps = True 
				elif texte[v].find("D ISCUSSION")!=-1 :
					trouverCorps = True
					type = 'd'
				elif texte[v].find("Discussion and")!=-1 :
					print("D a")
					type = 'd'
					trouverCorps = True
				elif texte[v].find("References")!=-1 and len(texte[v].split(' '))<5:
					print("R")
					
					trouverCorps = True

				else :
					#print(texte[v])
					corps+=texte[v]
				v+=1
			
			j=v

		if type == 'd' and not trouverD :
			
			c=j
			while not trouverD :
				if texte[c].find("Acknowledgements")!=-1 or texte[c].find("Acknowledgments")!=-1 or texte[c].find("ACKNOWLEDGMENT")!=-1:
					trouverD = True
				elif texte[c].find("Conclusions")!=-1 or texte[c].find("Conclusion")!=-1 : 
					trouverD = True
				else :
					#print(texte[c])
					discussion+=texte[c]
				c+=1
		elif type =='c' and not trouverC:
			c=j
			
			while not trouverC:
				if texte[c].find("Acknowledgements")!=-1 or texte[c].find("Acknowledgments")!=-1:
					trouverC = True
				elif texte[c].find("Conclusion")!=-1 :
					trouverC = True
				elif texte[c].find("Reference")!=-1 :
					trouverC = True
				elif texte[c].find("D ISCUSSION")!=-1 :
					trouverC = True
					type='d'
				else :
					#print(texte[c])
					conclusion+=texte[c]
				c+=1
		if not texte[j].find("References") and texte[j].find("REFERENCES"):
			while (j<len(texte)) :
				if not texte[v]=='\n' : biblio+=texte[j]
				j+=1



		j+=1

	if (type_fich == "-x" ) :
		xml(titre,str(tail),auteur,abstract,biblio,path,intro,corps,conclusion,discussion)
	else :
		txt(titre,str(tail),auteur,abstract,biblio,path,intro,corps,conclusion,discussion)
	#print("-----------Titre-----------\n",titre,"-----------Auteur-----------\n",auteur,"-----------Abstract-----------\n",abstract)


def main (type_fich):
	init=0
	"""	path = "txt/Torres.txt"
	fichier = open(path,'r')
	recherche(fichier,path)
	"""
	for path in pathlib.Path("txt/.").iterdir():
		if path.is_file():
			root, extension = os.path.splitext(path)
			if (extension == '.txt'):
					print (path)
					#print (path)
					reponse = ""
					while ( reponse != "y" and reponse != "n") :
						tail = os.path.split(path)
						print("Voulez vous parser le fichier ",tail[1]," (y/n)")
						reponse = input()
						if ( reponse == "y" ) :
							fichier = open(path,'r')
							recherche(fichier,path,type_fich)
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
		main(sys.argv[1]);




"""
				elif texte[d].split(' ')[0].isupper() and len(texte[d].split(' '))<4 :
					
					print("je passe par la")
					trouverIntro = True
				"""
