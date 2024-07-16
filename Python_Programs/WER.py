#computes the word error rate of the transcription from whisper or plspp
#---
#parameters: name of the file + mode (0 if from whisper, 1 if from plspp)
#---
#the program creates a .res result file in the corresponding directory ("Whisper_WER/WER" for 0 and "PLSPP_WER/WER" for 1)
#----------------------------------------------------------------------------------------------------------------------
import os
import re 
import sys

if sys.argv[2] == "0":
    #opening files from whisper
    Whis = open("../Whisper_WER/Whisper-split/" + sys.argv[1] + "-split.txt", "r")
    Corr = open("../Corrigés/" + sys.argv[1] + "/" + sys.argv[1] + ".txt", "r")
    Res = open("../Whisper_WER/WER/" +sys.argv[1] + ".res", "w")
elif sys.argv[2] == "1":
    #opening files from plspp
    Whis = open("../PLSPP_WER/PLSPP_WER_format/" + sys.argv[1] + "_pipeRes.txt", "r")
    Corr = open("../PLSPP_WER/Corr_WER_format_segmented/" + sys.argv[1] + "_corRes_segmented.txt", "r")
    Res = open("../PLSPP_WER/WER/" +sys.argv[1] + "_PLSPP.res", "w")

#reading the files and storing the text in lists (one list per actor)
#We use a list of lists for each file, each element of the list corresponds to the text of an actor (list of words)

#initialization
List_Whis = []
List_Corr = []
List_act = []

Prec_actor = ""

#going through the Whis file
for lign in Whis:
    # Removes punctuation and converts the text to lowercase
    lign = re.sub(r'[^\w\s]', '', lign).lower()

    List_lign = lign.split()     #transforms the line into a list of words
    Actor = List_lign[0]         #we retrieve the actor's name
    List_lign.pop(0)             #we remove the name from the list

    if (Prec_actor == "") or (Actor == Prec_actor): 
        #we haven't changed actor
        List_act = List_act + List_lign    #we concatenate the lists 
    else:
        List_Whis.append(List_act)          #we append the actor's text to the general Whis list
        List_act = List_lign
    
    Prec_actor = Actor           #we save the previous actor

List_Whis.append(List_act)  

Prec_actor = ""
List_act = []

#going through the Corr file
for lign in Corr:
    # Remove punctuation and convert to lower case
    lign = re.sub(r'[^\w\s]', '', lign).lower()
    List_lign = lign.split()     #transforms the line into a list of words
    Actor = List_lign[0]         #we retrieve the actor's name
    List_lign.pop(0)             #we remove the name from the list

    if (Prec_actor == "") or (Actor == Prec_actor): 
        #we haven't changed actor
        List_act = List_act + List_lign    #we concatenate the lists 
    else:
        List_Corr.append(List_act)          #we append the actor's text to the general Corr list
        List_act = List_lign
    
    Prec_actor = Actor           #we save the previous actor

List_Corr.append(List_act)
#calculating WER - Levenshtein distance method
i_corr = 0

#going through both lists at the same time
for txt_whis in List_Whis:
    txt_corr = List_Corr[i_corr]
    #initialization of the matrix of size number of words in txt_whis + 1 * number of words in txt_corr +1
    d = [[0] * (len(txt_whis) + 1) for _ in range(len(txt_corr) + 1)]

    #base cases
    for i in range(len(txt_corr) + 1):
        d[i][0] = i
    for j in range(len(txt_whis) + 1):
        d[0][j] = j

    #we calculate the values of the matrix
    for i in range(1, len(txt_corr) + 1):
        for j in range(1, len(txt_whis) + 1):

            if txt_corr[i - 1] == txt_whis[j - 1]:
                #case where the two words are identical
                d[i][j] = d[i - 1][j - 1]
            else:
                #the two words are not identical
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                min_operation = min(substitution, insertion, deletion)
                d[i][j] = min_operation

    # calculating wer by taking the bottom right corner of the matrix
    wer = d[len(txt_corr)][len(txt_whis)] / len(txt_corr)
    print("WER actor " + str(i_corr + 1) + ": " + str(wer) +"\n")
    Res.write("WER actor" + str(i_corr + 1) + ": " + str(wer) +"\n")

    i_corr += 1

#closing files
Whis.close()
Corr.close()
Res.close()