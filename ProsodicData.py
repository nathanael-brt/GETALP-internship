#extract all the data from stress table generated by plspp (from the whisperx transcription or from the reference corpus) and generate a file by element inside
import os

#open the stress table 
table_file = open("PLSPP_Prosodic/Tables/stressTable.csv", "r")

next(table_file) #skip the first line of the table

prec_file_name = "" #name of the previous file
nb_syl_loc = [0,0,0,0]                  #number of syllabus 2, 3, 4 and other (other is for the words with more than 4 syllabus, not enough to be relevant) for each file
nb_correct_syl_loc = [0,0,0,0]          #number of correct syllabus 2, 3, 4 and other for each file
nb_syl_tot = [0,0,0,0]                  #total number on all files
nb_correct_syl_tot = [0,0,0,0]          # correct total number on all files
nb_pattern_loc = [0,0,0,0,0,0,0,0,0]    #number of stress patterns, Oo, oO, Ooo, oOo, ooO, Oooo, oOoo, ooOo and oooO on each file
nb_correct_pattern_loc = [0,0,0,0,0,0,0,0,0] #number of correct stress patterns, oO, Oo, Ooo, oOo, ooO, Oooo, oOoo, ooOo and oooO on each file
nb_pattern_tot = [0,0,0,0,0,0,0,0,0]    #total number on all files
nb_correct_pattern_tot = [0,0,0,0,0,0,0,0,0] # correct total number on all files
nb_words_loc = 0                        #number of words for each file
nb_words_tot = 0                           #total number of words on all files

#loop on the table and extract the data for each file
for line in table_file :
    Tab_line = line.split(';')  #split each element of the line into a list
    file_name = Tab_line[0]  #get the file name
    nb_words_loc += 1      #increment the number of words for the file
    nb_words_tot += 1      #increment the total number of words

    if (file_name != prec_file_name):  #if the file name is different from the previous one, create a new file
        if (prec_file_name != ""):  #if it is not the first file, write the data and close the previous file
            #we write all the data
            data.write("number of words;" + str(nb_words_loc) + "\n")
        if nb_syl_loc[0] != 0:
            data.write("prop correct 2-syll;" + str(float(nb_correct_syl_loc[0])/float(nb_syl_loc[0])) + "\n")
            if nb_pattern_loc[0] != 0:
                data.write("prop correct Oo;" + str(float(nb_correct_pattern_loc[0])/float(nb_pattern_loc[0])) + "\n")
            if nb_pattern_loc[1] != 0:
                data.write("prop corect oO;" + str(float(nb_correct_pattern_loc[1])/float(nb_pattern_loc[1])) + "\n")
        if nb_syl_loc[1] != 0:
            data.write("prop correct 3-syll;" + str(float(nb_correct_syl_loc[1])/float(nb_syl_loc[1])) + "\n")
            if nb_pattern_loc[2] != 0:
                data.write("prop correct Ooo;" + str(float(nb_correct_pattern_loc[2])/float(nb_pattern_loc[2])) + "\n")
            if nb_pattern_loc[3] != 0:
                data.write("prop correct oOo;" + str(float(nb_correct_pattern_loc[3])/float(nb_pattern_loc[3])) + "\n")
            if nb_pattern_loc[4] != 0:
                data.write("prop correct ooO;" + str(float(nb_correct_pattern_loc[4])/float(nb_pattern_loc[4])) + "\n")
        if nb_syl_loc[2] != 0:
            data.write("prop correct 4-syll;" + str(float(nb_correct_syl_loc[2])/float(nb_syl_loc[2])) + "\n")
            if nb_pattern_loc[5] != 0:
                data.write("prop correct Oooo;" + str(float(nb_correct_pattern_loc[5])/float(nb_pattern_loc[5])) + "\n")
            if nb_pattern_loc[6] != 0:
                data.write("prop correct oOoo;" + str(float(nb_correct_pattern_loc[6])/float(nb_pattern_loc[6])) + "\n")
            if nb_pattern_loc[7] != 0:
                data.write("prop correct ooOo;" + str(float(nb_correct_pattern_loc[7])/float(nb_pattern_loc[7])) + "\n")
            if nb_pattern_loc[8] != 0:
                data.write("prop correct oooO;" + str(float(nb_correct_pattern_loc[8])/float(nb_pattern_loc[8])) + "\n")
            data.close() #close the file
        #create a new file
        data = open("PLSPP_Prosodic/Ref_data/" + file_name + ".csv", "w")
        #initialize the data
        nb_syl_loc = [0,0,0,0]                  #number of syllabus 2, 3, 4 and other (other is for the words with more than 4 syllabus, not enough to be relevant) 
        nb_correct_syl_loc = [0,0,0,0]          #number of correct syllabus 2, 3, 4 and other
        nb_pattern_loc = [0,0,0,0,0,0,0,0,0]    #number of stress patterns, oO, Oo, Ooo, oOo, ooO, Oooo, oOoo, ooOo and oooO
        nb_correct_pattern_loc = [0,0,0,0,0,0,0,0,0] #number of correct stress patterns, oO, Oo, Ooo, oOo, ooO, Oooo, oOoo, ooOo and oooO
        nb_words_loc = 0                        #number of words 

    
    prec_file_name = file_name  #update the previous file name

    if Tab_line[3] == "2":   #we have a 2-syllabus word
        #increment the 2-syllabus counter
        nb_syl_loc[0] += 1
        nb_syl_tot[0] += 1
        
        #find which accentuation pattern we are on 
        if Tab_line[6] == "Oo":
            patt_index = 0       
        elif Tab_line[6] == "oO":
            patt_index = 1

        #increment the pattern counters
        nb_pattern_loc[patt_index] += 1
        nb_pattern_tot[patt_index] += 1

        #verify the correctness of the accentuation
        if Tab_line[5] == Tab_line[6]:
            #increment the correct syllabus counter
            nb_correct_syl_loc[0] += 1
            nb_correct_syl_tot[0] += 1
            #increment the correct pattern counter
            nb_correct_pattern_loc[patt_index] += 1
            nb_correct_pattern_tot[patt_index] += 1
    
    elif Tab_line[3] == "3":  #we have a 3-syllabus word
        #increment the 3-syllabus counter
        nb_syl_loc[1] += 1
        nb_syl_tot[1] += 1

        #find which accentuation pattern we are on 
        if Tab_line[6] == "Ooo":
            patt_index = 2
        elif Tab_line[6] == "oOo":
            patt_index = 3
        elif Tab_line[6] == "ooO":
            patt_index = 4

        #increment the pattern counters
        nb_pattern_loc[patt_index] += 1
        nb_pattern_tot[patt_index] += 1

        #verify the correctness of the accentuation
        if Tab_line[5] == Tab_line[6]:
            #increment the correct syllabus counter
            nb_correct_syl_loc[1] += 1
            nb_correct_syl_tot[1] += 1
            #increment the correct pattern counter
            nb_correct_pattern_loc[patt_index] += 1
            nb_correct_pattern_tot[patt_index] += 1

    elif Tab_line[3] == "4":  #we have a 4-syllabus word
        #increment the 4-syllabus counter
        nb_syl_loc[2] += 1
        nb_syl_tot[2] += 1

        #find which accentuation pattern we are on 
        if Tab_line[6] == "Oooo":
            patt_index = 5
        elif Tab_line[6] == "oOoo":
            patt_index = 6
        elif Tab_line[6] == "ooOo":
            patt_index = 7
        elif Tab_line[6] == "oooO":
            patt_index = 8

        #increment the pattern counters
        nb_pattern_loc[patt_index] += 1
        nb_pattern_tot[patt_index] += 1

        #verify the correctness of the accentuation
        if Tab_line[5] == Tab_line[6]:
            #increment the correct syllabus counter
            nb_correct_syl_loc[2] += 1
            nb_correct_syl_tot[2] += 1
            #increment the correct pattern counter
            nb_correct_pattern_loc[patt_index] += 1
            nb_correct_pattern_tot[patt_index] += 1


#we write all the data on the last file
data.write("number of words;" + str(nb_words_loc) + "\n")
if nb_syl_loc[0] != 0:
    data.write("prop correct 2-syll;" + str(float(nb_correct_syl_loc[0])/float(nb_syl_loc[0])) + "\n")
    if nb_pattern_loc[0] != 0:
        data.write("prop correct Oo;" + str(float(nb_correct_pattern_loc[0])/float(nb_pattern_loc[0])) + "\n")
    if nb_pattern_loc[1] != 0:
        data.write("prop corect oO;" + str(float(nb_correct_pattern_loc[1])/float(nb_pattern_loc[1])) + "\n")
if nb_syl_loc[1] != 0:
    data.write("prop correct 3-syll;" + str(float(nb_correct_syl_loc[1])/float(nb_syl_loc[1])) + "\n")
    if nb_pattern_loc[2] != 0:
        data.write("prop correct Ooo;" + str(float(nb_correct_pattern_loc[2])/float(nb_pattern_loc[2])) + "\n")
    if nb_pattern_loc[3] != 0:
        data.write("prop correct oOo;" + str(float(nb_correct_pattern_loc[3])/float(nb_pattern_loc[3])) + "\n")
    if nb_pattern_loc[4] != 0:
        data.write("prop correct ooO;" + str(float(nb_correct_pattern_loc[4])/float(nb_pattern_loc[4])) + "\n")
if nb_syl_loc[2] != 0:
    data.write("prop correct 4-syll;" + str(float(nb_correct_syl_loc[2])/float(nb_syl_loc[2])) + "\n")
    if nb_pattern_loc[5] != 0:
        data.write("prop correct Oooo;" + str(float(nb_correct_pattern_loc[5])/float(nb_pattern_loc[5])) + "\n")
    if nb_pattern_loc[6] != 0:
        data.write("prop correct oOoo;" + str(float(nb_correct_pattern_loc[6])/float(nb_pattern_loc[6])) + "\n")
    if nb_pattern_loc[7] != 0:
        data.write("prop correct ooOo;" + str(float(nb_correct_pattern_loc[7])/float(nb_pattern_loc[7])) + "\n")
    if nb_pattern_loc[8] != 0:
        data.write("prop correct oooO;" + str(float(nb_correct_pattern_loc[8])/float(nb_pattern_loc[8])) + "\n")
data.close() #close the file

#we write the total data file : 
data = open("PLSPP_Prosodic/Ref_data/total_data.csv", "w")
data.write("number of words;" + str(nb_words_tot) + "\n")
data.write("prop correct 2-syll;" + str(float(nb_correct_syl_tot[0])/float(nb_syl_tot[0])) + "\n")
data.write("prop correct Oo;" + str(float(nb_correct_pattern_tot[0])/float(nb_pattern_tot[0])) + "\n")
data.write("prop corect oO;" + str(float(nb_correct_pattern_tot[1])/float(nb_pattern_tot[1])) + "\n")
data.write("prop correct 3-syll;" + str(float(nb_correct_syl_tot[1])/float(nb_syl_tot[1])) + "\n")
data.write("prop correct Ooo;" + str(float(nb_correct_pattern_tot[2])/float(nb_pattern_tot[2])) + "\n")
data.write("prop correct oOo;" + str(float(nb_correct_pattern_tot[3])/float(nb_pattern_tot[3])) + "\n")
data.write("prop correct ooO;" + str(float(nb_correct_pattern_tot[4])/float(nb_pattern_tot[4])) + "\n")
data.write("prop correct 4-syll;" + str(float(nb_correct_syl_tot[2])/float(nb_syl_tot[2])) + "\n")
data.write("prop correct Oooo;" + str(float(nb_correct_pattern_tot[5])/float(nb_pattern_tot[5])) + "\n")
data.write("prop correct oOoo;" + str(float(nb_correct_pattern_tot[6])/float(nb_pattern_tot[6])) + "\n")
data.write("prop correct ooOo;" + str(float(nb_correct_pattern_tot[7])/float(nb_pattern_tot[7])) + "\n")
data.write("prop correct oooO;" + str(float(nb_correct_pattern_tot[8])/float(nb_pattern_tot[8])) + "\n")
data.close() #close the file
