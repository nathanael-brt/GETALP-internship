import os

#Ouverture des fichiers
Whis = open(input("Whisper file (.srt):\n"), "r")
Txtgrid = open(input("Textgrid file:\n"), "r+")

#prologue du fichier
Txtgrid.write("File type = \"ooTextFile\"\nObject class = \"TextGrid\"\n")

#xmin - xmax
Txtgrid.write("\nxmin = 0\n")
Txtgrid.write("                                            \n")    #on reviendra ici plus tard

#tiers
Txtgrid.write("tiers? <exists>\n")
Txtgrid.write("size = 1\n")

#items
Txtgrid.write("item []:\n")
Txtgrid.write("    item [1]:\n")
Txtgrid.write("        class = \"IntervalTier\"\n")
Txtgrid.write("        name = \"all\"\n")
Txtgrid.write("        xmin = 0\n")
Txtgrid.write("                                                      \n")    #on reviendra ici plus tard
Txtgrid.write("                                                      \n")    #on reviendra ici plus tard

#on parcourt le fichier généré par whisper (le format .srt)
local_it = 0   #itérateur permettant de se reperer dans chaque paragraphe (valeurs entre 0 et 3)
for line in Whis:
    match local_it:
        case 0: 
            #première ligne
            line = line.rstrip(line[-1])
            interval = int(line)  #numéro de l'intervalle 
            Txtgrid.write("        intervals [" + str(interval) + "]:\n")
            local_it+= 1 
        case 1:
            #deuxième ligne 
            Numbers = line.split(" --> ")  #on sépare min et max
            
            T_min_list = Numbers[0].split(":")  #on sépare les chiffres de min
            Unit_list = T_min_list[2].split(",")   #transformation en float pour la virgule
            Unit = float(Unit_list[0]) + float(Unit_list[1])*0.001
            T_min = float(T_min_list[0])*3600 + float(T_min_list[1])*60 + Unit   #on calcule le temps min
            
            T_max_list = Numbers[1].split(":")  #on sépare les chiffres de max
            Unit_list = T_max_list[2].split(",")   #transformation en float pour la virgule
            Unit = float(Unit_list[0]) + float(Unit_list[1])*0.001
            T_max = float(T_max_list[0])*3600 + float(T_max_list[1])*60 + Unit  #on cacule le temps max

            Txtgrid.write("            xmin = " + str(T_min) + "\n")
            Txtgrid.write("            xmax = " + str(T_max) + "\n")
            local_it+= 1 
        case 2:
            #troisième ligne 
            line = line.rstrip(line[-1])
            Txtgrid.write("            text = \"" + line + "\"\n")
            local_it+= 1 
        case 3: 
            local_it = 0 

#on écrit le temps max à la 5eme ligne du fichier
Txtgrid.seek(61,0)
Txtgrid.write("xmax = " + str(T_max))

#on écrit le temps max à la 13eme ligne du fichier
Txtgrid.seek(227,0)
Txtgrid.write("    xmax = " + str(T_max))

#on écrit le nombre d'intervalles à la 14eme ligne du fichier
Txtgrid.seek(282,0)
Txtgrid.write("    intervals: size = " + str(interval))

#fermeture des fichiers
Whis.close()
Txtgrid.close()
