import pathlib
import os 
import sys


#Vérifie si mot a une occurrence dans texte en position i




#titre_doss = input('Choisir nom du dossier \n') 

	#ajout acknow
def xml(titre,preamble,auteur,abstract,acknowledgments,biblio,conclusion,fichier) :
    File = open(preamble+".xml",  'w+')
    
    File.write("<?xml version='1.0' standalone='yes' ?>\n");
    File.write("<article>\n");
    File.write("<preamble>"+preamble+"</preamble>\n");
    File.write("<titre>"+titre+"</titre>\n");
    File.write("<auteur>"+auteur+"</auteur>\n");
    File.write("<abstract>"+abstract+"</abstract>\n");
	#ajout acknow
    File.write("<acknowledgments>"+acknowledgments+"</acknowledgments>\n");
    File.write("<biblio>"+biblio+"</biblio>\n");
    File.write("<conclusion>"+conclusion+"</conclusion>\n");
    File.write("</article>\n");
    
    File.close();
    
    #print("<article>")
    #print("<preamble>"+preamble+"</preamble>")
    #print("<titre>"+titre+"</titre>")
    #print("<auteur>"+auteur+"</auteur>")
    #print("<abstract>"+abstract+"</abstract>")
    #print("<biblio>"+biblio+"</biblio>")
    #print("</article>")

	#ajout acknow
def txt(titre,preamble,auteur,abstract,acknowledgments,biblio,conclusion,fichier) :
    File = open(preamble+".txt",  'w+')
    

    File.write(preamble+"\n\n");
    File.write(titre+"\n\n");
    File.write(auteur+"\n\n");
    File.write(abstract+"\n\n");
	#ajout acknow
    File.write(acknowledgments+"\n\n);
    File.write(biblio+"\n\n");
    File.write(conclusion+"\n\n");
    
    File.close();
    
    #print(preamble+"\n\n")
    #print(titre+"\n\n")
    #print(auteur+"\n\n")
    #print(abstract+"\n\n")
    #print(biblio+"\n\n")
    #print(conclusion+"\n\n")


      

#titre_doss = input('Choisir nom du dossier \n') 

def recherche(fichier,path,type_fich):
	texte = fichier.readlines()

    #titre_doss.replace(" ","_")
	#print(titre_doss)

	titre = ""
	auteur = ""
	abstract = ""
	biblio = ""
	conclusion = ""
	head, tail = os.path.split(path)
	tail='.'.join(tail.split('.')[:-1])
	
	j = 0
	trouver = False
	trouverAuteur = False
	trouverConclusion = False
	       #ajout acknow
	trouverAcknowledgment = False
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
		
		#Conclusion
		if ( texte[j].find('Conclusion')!=-1 or texte[j].find('Conclusions')!=-1 or texte[j].find('C ONCLUSIONS')!=-1 or texte[j].find('CONCLUSIONS')!=-1) :
			t = j
			while not trouverConclusion and t<len(texte) :
				print(texte[t])
				conclusion += texte[t]
				t += 1
				if ( texte[t].find('Acknowledgments')!=-1 or texte[t].find('References')!=-1 or texte[t].find('ACKNOWLEDGMENT')!=-1 or texte[t].find('D ISCUSSION')!=-1 or texte[t].find('DISCUSSION')!=-1 or texte[t].find('Discution')!=-1 ) :
					trouverConclusion = True
	       
	       #Acknowledgments
	       if not texte[j].find("ACKNOWLEDGMENT") or not texte[j].find("ACKNOWLEDGMENTS") or not texte[j].find("Acknowledgments") or not texte[j].find("5 Acknowledgements") or not texte[j].find("Acknowledgements"):
			ack = j
			while(not trouverAcknowledgment):
				if ack<len(texte) and (not texte[ack+1].find("References") or not texte[ack+1].find("REFERENCES") or not texte[ack+1].find("R EFERENCES")):
					trouverAcknowledgment = True
				acknowledgments+=texte[ack]
				ack+=1
				
				
		#reference
		if not texte[j].find("References") and texte[j].find("REFERENCES"):
			while (j<len(texte)) :
				if not texte[v]=='\n' : biblio+=texte[j]
				j+=1
				
		j+=1
	if (type_fich == "-x" ) :
	       	#ajout acknow pour les 2
		xml(titre,str(tail),auteur,abstract,acknowledgments,biblio,conclusion,path)
	else :
		txt(titre,str(tail),auteur,abstract,acknowledgments,biblio,conclusion,path)
	print("-----------Titre-----------\n",titre,"-----------Auteur-----------\n",auteur,"-----------Abstract-----------\n",abstract,"-----------Conclusion-----------\n",conclusion)


def main (type_fich):
	init=0
	for path in pathlib.Path("txt/.").iterdir():
		if path.is_file():
			root, extension = os.path.splitext(path)
			if (extension == '.txt'):
					print (path)
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
