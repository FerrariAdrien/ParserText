import sys

def main(argv, taille):
	if ( taille < 3 ):
		print("Argument manquant.")
		return 1
		
	if ( argv[1] != "-t" and argv[1] != "-x" ) :
		print("Argument non reconnu : ",argv[1]," (deux possibilitées : -t ou -x).")
		return 1
		
	fichier = open(argv[2],'r')

	texte = fichier.readlines()

	B = True
	j = 0
	titre = False

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
	return 0
		

if __name__ == '__main__':
	e = main(sys.argv,len(sys.argv))
	print("Processus terminé : ",e)
