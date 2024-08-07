#translation of the files given by plspp and the correction into the format needed for the WER calculation
#---
#takes the name of the  audio file as an argument and POSSIBLY a number reversing the determined order of the speakers by the function (parachute), 
# if 0 nothing is done if 1 reverse the order
#---
#The program creates automatically 2 results files :
#   PLSPP_WER/PLSPP_WER_format/<name_of_the_file>_pipeRes.txt for the transcription from PLSPP.
#   PLSPP_WER/Corr_WER_format/<name_of_the_file>_corRes.txt for the correction.
#----------------------------------------------------------------------------------------------------------------------
import os
import sys
import functions

#result files
pipeRes = open("../PLSPP_WER/PLSPP_WER_format/" + sys.argv[1] + "_pipeRes.txt", "w")    #result file for the pipeline's file
corRes = open("../PLSPP_WER/Corr_WER_format/" + sys.argv[1] + "_corRes.txt", "w")            #result file for the correction
timeInfo = open("../PLSPP_WER/TimeInfo/timeInfo_sorted.csv", "r")                             #file containing the time informations of each segment


#concatenation of all the text files from plspp into the wanted format

# Iterate over files in PLSPP_text directory
for name in os.listdir("../PLSPP_WER/PLSPP_text/" + sys.argv[1]+ "/"):
    pipeTxt = open("../PLSPP_WER/PLSPP_text/" + sys.argv[1] + "/" + name, "r")
    speaker_nb = name[28:30]  #get the speaker number from the file name
    pipeRes.write(speaker_nb) #write the speaker number in the result file
    pipeRes.write("		" + pipeTxt.read() + "\n")  #write the text 
    pipeTxt.close()

#translation of the corrected transcription into the wanted format by taking only the used segments (<8s)
#We take only the segments of the correrction which are strictly inside the segment from PLSPP

normal_order =  functions.is_speaker_order_normal("../PLSPP_WER/PLSPP_tg/" + sys.argv[1] +".TextGrid")  #get the order of the speakers
#help to keep track of the real orer of the speakers
if normal_order: 
    #first case : normal order of the speakers
    if sys.argv[2] == "0":
        real_speaker_nb = -1
        it = 1
    else :
        real_speaker_nb = 2
        it = -1
else:
    #second case : reverse order of the speakers
    if sys.argv[2] == "0":
        real_speaker_nb = 2
        it = -1
    else:
        real_speaker_nb = -1
        it = 1

speaker_nb = ""

#loop over the time information file to get the right segments
for line in timeInfo:
    Tab_line = line.split(";")    #split the line into a table
    
    if Tab_line[0] != "File":      #check that this is not the first line

        filename = os.path.splitext(Tab_line[0])[0]  #get the filename without the extension

        if filename == sys.argv[1]:  #check that we are on the right file

            TextGrid = open("../Corrigés/" + filename  +"/" + filename + ".TextGrid", "r")  #open the TextGrid file containing the correction
            prec_speaker_nb = speaker_nb   #save the previous speaker number
            speaker_nb = Tab_line[1][8:10] #get the speaker number
            
            if speaker_nb != prec_speaker_nb:  #if the speaker number has changed
                real_speaker_nb +=  it
                

            start = float(Tab_line[3])  #get the start time
            end = float(Tab_line[4])    #get the end time

            corRes.write("0" + str(real_speaker_nb) + "		" )   #write the speaker number
            #loop into the TextGrid file to get the right segment
            for lineGrid in TextGrid:
                if lineGrid.startswith("    item["): #speaker number
                    speaker_nb_grid = str(int(lineGrid[9]) -1) #get the speaker number 

                elif lineGrid.startswith("            xmin = "):     #min time
                    xmin = float(lineGrid[19:])     #get the min time

                elif lineGrid.startswith("            xmax = "):     #max time
                    xmax = float(lineGrid[19:])

                elif lineGrid.startswith("            text = "):     #text
                    if ((end >= xmin >= start) or (start <= xmax <= end) or ((xmin <= start) and (xmax >= end))) and real_speaker_nb == int(speaker_nb_grid):   #test that we are strictly inside the right segment, for the right speaker
                        text = lineGrid[19:]        #get the corrected text of the segment
                        text = text.strip('\n').strip('"')           #get rid of the \n and the "
                        
                        if text != "":  #write the text only if it is not empty (not a pause
                            corRes.write(text + " ")
                        if xmax > end :
                            corRes.write("\n")  #if we are out of the segment, we go to the next line
                            break           #we can stop the loop if we are out of the base segment
                    elif xmin > end and real_speaker_nb == int(speaker_nb_grid):
                        corRes.write("\n")  #if we are out of the segment, we go to the next line
                        break           #we can stop the loop if we are out of the base segment
        
            TextGrid.close()    #close the file

#close the files
pipeRes.close()     
corRes.close()      
timeInfo.close()    