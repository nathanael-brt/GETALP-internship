#translation of the files given by plspp and the correction into the format needed for the WER calculation
import os

#result files
pipeRes = open(input("First result file (from the pipeline's results): "), "w")
corRes = open(input("Second result file (from the correction): "), "w")
timeInfo = open(input("Time information file: "), "r")

#concatenation of all the text files from plspp into the wanted format

# Iterate over files in PLSPP_text directory
for name in os.listdir("PLSPP_text"):
    pipeTxt = open("PLSPP_text/" + name, "r")
    speaker_nb = name[28:29]  #get the speaker number from the file name
    pipeRes.write(speaker_nb) #write the speaker number in the result file
    pipeRes.write("		" + pipeTxt.read())  #write the text 
    pipeTxt.close()

#translation of the corrected transcription into the wanted format by taking only the used segments (<8s)

#loop over the time information file to get the right segments
for lign in timeInfo:
    Tab_lign = lign.split(";")    #split the line into a table
    filename = os.path.splitext(Tab_lign[0])[0]  #get the filename without the extension
    TextGrid = open("Corrigés/" + filename  +"/" + filename + ".TextGrid", "r")  #open the TextGrid file conatining the correction
    nb_speaker = Tab_lign[1][8:9] #get the speaker number
    
    start = float(Tab_lign[3])  #get the start time
    end = float(Tab_lign[4])    #get the end time

    it = 0 #iterator to keep track of the position in the TextGrid
  