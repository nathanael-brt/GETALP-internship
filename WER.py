#compute the word error rate 
import os
import re 

#ouverture des fichiers
Whis = open(input("Whisper split file:\n"), "r")
Corr = open(input("Corrected file:\n"), "r")
Res = open(input("Result file :\n"), "w")

#lecture des fichiers et stockage du texte dans des listes (une liste par acteur)
#On utilise une liste de liste par fichier, chaque élément de la liste correspond au texte d'un acteur (liste de mots)

#initialisation
List_Whis = []
List_Corr = []
List_act = []

Prec_actor = ""

#on parcourt le fichier whis
for lign in Whis:
    # Supprime la ponctuation et passe le texte en miniscule
    lign = re.sub(r'[^\w\s]', '', lign).lower()

    List_lign = lign.split()     #transforme la ligne en liste de mots
    Actor = List_lign[0]         #on recupère le nom de l'acteur
    List_lign.pop(0)             #on supprime le nom de la liste

    if (Prec_actor == "") or (Actor == Prec_actor): 
        #on a pas changé d'acteur
        List_act = List_act + List_lign    #on concatène les listes 
    else :
        List_Whis.append(List_act)          #on append le texte de l'acteur à liste générale de Whis
        List_act = List_lign
    
    Prec_actor = Actor           #on sauvegarde l'ancien acteur

List_Whis.append(List_act)  

Prec_actor = ""
List_act = []

#on parcourt le fichier Corr
for lign in Corr:
    # Remove punctuation and convert to lower case
    lign = re.sub(r'[^\w\s]', '', lign).lower()
    List_lign = lign.split()     #transforme la ligne en liste de mots
    Actor = List_lign[0]         #on recupère le nom de l'acteur
    List_lign.pop(0)             #on supprime le nom de la liste

    if (Prec_actor == "") or (Actor == Prec_actor): 
        #on a pas changé d'acteur
        List_act = List_act + List_lign    #on concatène les listes 
    else :
        List_Corr.append(List_act)          #on append le texte de l'acteur à liste générale de Whis
        List_act = List_lign
    
    Prec_actor = Actor           #on sauvegarde l'ancien acteur

List_Corr.append(List_act)
#calcul du WER - Levenshtein distance method
i_corr = 0

#on parcourt les 2 listes en même temps
for txt_whis in List_Whis:
    txt_corr = List_Corr[i_corr]

    #initialisation de la matrice de taille nbr de mots dans txt_whis + 1 * nbr de mots dans txt_corr +1
    d = [[0] * (len(txt_whis) + 1) for _ in range(len(txt_corr) + 1)]

    #cas de bases
    for i in range(len(txt_corr) + 1):
        d[i][0] = i
    for j in range(len(txt_whis) + 1):
        d[0][j] = j

    #on calcule les valeurs de la matrice 
    for i in range(1, len(txt_corr) + 1):
        for j in range(1, len(txt_whis) + 1):

            if txt_corr[i - 1] == txt_whis[j - 1] :
                #cas ou les 2 mots sont identiques
                d[i][j] = d[i - 1][j - 1]
            else:
                #les 2 mots ne sont pas identiques
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)
            
    # calcul du wer en prenant le coin en bas à droite de la matrice
    wer = d[len(txt_corr)][len(txt_whis)] / len(txt_corr)
    print("WER actor " + str(i_corr + 1) + ": " + str(wer) +"\n")
    Res.write("WER actor" + str(i_corr + 1) + ": " + str(wer) +"\n")

    i_corr += 1

#fermeture des fichiers
Whis.close()
Corr.close()
Res.close()