#translation of the files given by plspp and the correction into the format needed for the WER calculation
import os
import sys

#result files
pipeRes = open("PLSPP_WER/PLSPP_WER_format/" + sys.argv[1] + + "_pipeRes.txt", "w")    #result file for the pipeline's file
corRes = open("PLSPP_WER/Corr_WER_format/" + sys.argv[1] + "_corRes.txt", "w")            #result file for the correction
timeInfo = open("PLSPP_WER/TimeInfo/timeInfo.csv", "r")                             #file containing the time informations of each segment

#concatenation of all the text files from plspp into the wanted format

# Iterate over files in PLSPP_text directory
for name in os.listdir("PLSPP_text/" + sys.argv[1]+ "/"):
    pipeTxt = open("PLSPP_text/" + name, "r")
    speaker_nb = name[28:30]  #get the speaker number from the file name
    pipeRes.write(speaker_nb) #write the speaker number in the result file
    pipeRes.write("		" + pipeTxt.read() + "\n")  #write the text 
    pipeTxt.close()

#translation of the corrected transcription into the wanted format by taking only the used segments (<8s)
#We take only the segments of the correrction which are strictly inside the segment from PLSPP

#loop over the time information file to get the right segments
for line in timeInfo:
    Tab_line = line.split(";")    #split the line into a table
    
    if Tab_line[0] != "File":      #check that this is not the first line

        filename = os.path.splitext(Tab_line[0])[0]  #get the filename without the extension

        if filename == sys.argv[1]:  #check that we are on the right file

            TextGrid = open("Corrigés/" + filename  +"/" + filename + ".TextGrid", "r")  #open the TextGrid file containing the correction
            speaker_nb = Tab_line[1][8:10] #get the speaker number
            
            start = float(Tab_line[3])  #get the start time
            end = float(Tab_line[4])    #get the end time

            #loop into the TextGrid file to get the right segment
            for lineGrid in TextGrid:
                if lineGrid.startswith("    item["): #speaker number
                    speaker_nb_grid = str(int(lineGrid[9]) -1) #get the speaker number 

                elif lineGrid.startswith("            xmin = "):     #min time
                    xmin = float(lineGrid[19:])     #get the min time

                elif lineGrid.startswith("            xmax = "):     #max time
                    xmax = float(lineGrid[19:])

                elif lineGrid.startswith("            text = "):     #text
                    if ((end >= xmin >= start) or (start <= xmax <= end)) and int(speaker_nb) == int(speaker_nb_grid):   #test that we are strictly inside the right segment, for the right speaker
                        text = lineGrid[19:]        #get the corrected text of the segment
                        text = text.strip('\n').strip('"')           #get rid of the \n and the "
                        
                        if text != "":  #write the text only if it is not empty (not a pause)
                            corRes.write(speaker_nb)    #write the speaker number
                            corRes.write("		" + text + "\n")
                    elif xmin > end and int(speaker_nb) == int(speaker_nb_grid):
                        break           #we can stop the loop if we are out of the base segment
        
            TextGrid.close()    #close the file

#close the files
pipeRes.close()     
corRes.close()      
timeInfo.close()    