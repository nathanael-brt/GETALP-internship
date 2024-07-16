#transform all the segments of corrected text into single files 
#---
#takes no input and automatically reads all the files that are stored into the directory "PLSPP_WER/Corr_WER_format_segmented/"
#---
#creates all the files into the directory "PLSPP_Prosodic/Corpus_segmented/"
#----------------------------------------------------------------------------------------------------------------------
import os 

prec_speaker= ""
#loop on all the files in the directory
for name in os.listdir("../PLSPP_WER/Corr_WER_format_segmented/"):
    it = 0 #iterator to write on file names
    #open the file
    Corr_seg = open("../PLSPP_WER/Corr_WER_format_segmented/" + name, "r")
    #read the content of the file
    for line in Corr_seg:
        Tab_line = line.split("		")  #split the text from the speaker number

        if prec_speaker != Tab_line[0]:
            #if we have are on a new speaker
            it = 0
        prec_speaker = Tab_line[0]

        #open the file where we will write the segment text
        Seg = open("../PLSPP_Prosodic/Corpus_segmented/" + name.split("_corRes")[0] + "_SPEAKER_" + Tab_line[0] +"_" + str(it) + ".txt", "w")

        #write the text in the file
        Seg.write(Tab_line[1])

        Seg.close()
        #increment the iterator
        it += 1

    Corr_seg.close()
    
    
    