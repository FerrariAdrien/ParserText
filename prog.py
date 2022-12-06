fichier = open('/home/gadrew/Documents/corpus/CORPUS_TRAIN/fichier1.txt','r')

texte = fichier.readlines()

"""Vérifie si mot a une occurrence dans texte en position i"""
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

