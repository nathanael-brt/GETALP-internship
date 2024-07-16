#Segment correctly the correction text using the PLSPP output
#---
#takes as an input the name of the audio file we are working on (without the extension)
#resegments the text in the file PLSPP_WER/PLSPP_WER_format/<name_of_the_file>_pipeRes.txt using the file PLSPP_WER/Corr_WER_format/<name_of_the_file>_corRes.txt
#---
#puts the result into the file PLSPP_WER/Corr_WER_format_segmented/<name_of_the_file>_corRes_segmented.txt (creates it if it doesn't exist)
#----------------------------------------------------------------------------------------------------------------------
import os
import re 
import sys

#open the files
Trans = open("../PLSPP_WER/PLSPP_WER_format/" + sys.argv[1] + "_pipeRes.txt", "r")
Corr = open("../PLSPP_WER/Corr_WER_format/" + sys.argv[1] + "_corRes.txt", "r")
Res = open("../PLSPP_WER/Corr_WER_format_segmented/" + sys.argv[1] + "_corRes_segmented.txt", "w")

#read the files 
txt_Trans = []  #list containing the lists of the lines
for lign in Trans :
    # suppress the punctuation and put the text in lower case
    lign = re.sub(r'[^\w\s]', '', lign).lower()

    List_lign = lign.split()     #transform the line into a list of words
    txt_Trans.append(List_lign)  #append the line to the list 

txt_Corr = []  #list containing the lists of the lines
for lign in Corr :
    # suppress the punctuation and put the text in lower case
    lign = re.sub(r'[^\w\s]', '', lign).lower()

    List_lign = lign.split()     #transform the line into a list of words
    txt_Corr.append(List_lign)  #append the line to the list

#loop on both texts at the same time and segment the correction text using the PLSPP output
i_corr = 0      #iterator to loop on the correction text
for lign_Trans in txt_Trans:
    lign_Res = []   #list containing the words of the segmented line
    lign_Corr = txt_Corr[i_corr]    #get the corresponding line in the correction text

    speaker = lign_Trans.pop(0)  #get the speaker of the line
    lign_Corr.pop(0) 

    size_lc = len(lign_Corr)    #size of the correction line

    #correction of the end of the segment
    i_word_corr = 0  #iterator to loop on the correction line
    #we loop on both lines 
    for word_trans in lign_Trans:
        if i_word_corr == size_lc:
            #we are at the end of the correction line
            break
        lign_Res.append(lign_Corr[i_word_corr])  #append the word to the result
        i_word_corr += 1    #increment the iterator
    
    #test if we are not at the end the lign in the correction text 
    if i_word_corr < size_lc:

        word_trans = lign_Trans[-1] #we get the last word of the transcription line

        if word_trans in lign_Corr[i_word_corr:size_lc]:
            #the last word of the transcription line is after the current position
            while lign_Corr[i_word_corr] != word_trans : 
                #we append all words until we find the last word of the transcription line
                lign_Res.append(lign_Corr[i_word_corr])
                i_word_corr += 1
            lign_Res.append(lign_Corr[i_word_corr])

        elif word_trans in lign_Corr[0:i_word_corr]:
            #the last word of the transcription line is before the current position
            i_word_corr -= 1
            while lign_Corr[i_word_corr] != word_trans :
                #we suppress all words until we find the last word of the transcription line
                lign_Res.pop(-1)
                i_word_corr -= 1
        
    #correction of the beginning of the segment

    #we loop on both lines but in reverse
    for word_trans in reversed(lign_Trans):
        if i_word_corr == -1:
            #we are at the beginning of the correction line
            break
        i_word_corr -= 1   #decrement the iterator
    
    #test if we are not at the beginning of the lign in the correction text
    if i_word_corr > -1:

        word_trans = lign_Trans[0] #we get the first word of the transcription line

        if word_trans in lign_Res:
            #the first word of the transcription line is in the line
            while lign_Res[0] != word_trans:
                #we suppress all the words before the first word of the transcription line
                lign_Res.pop(0)
        else :
            #the first word of the transcription line is not in the line
            #we suppress all the words before the first word of the transcription line
            while i_word_corr > -1:
                lign_Res.pop(0)
                i_word_corr -= 1
    
    #append the line to the result
    i_corr += 1

    Res.write(speaker + "		")
    for word in lign_Res:
        Res.write(word + " ")
    Res.write("\n")









    