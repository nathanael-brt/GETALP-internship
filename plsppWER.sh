#Execute plspp on all the textgrid files from pyannotes (for all the recording furnished)
#Compute the WER for each one of them
echo "---START (press any button)---"
read
#supress all the files in the necessary directories
cd ../plspp
#rm audio/* benepar/* shape/* syll/* text/* tg/* tgpos/* whisperx/*
#launch the pipeline
#./praat_barren scripts/intervalles2wavAndtimetable.praat ../data/ ../pyannote/ .TextGrid ../audio/ 3 0.01 8
#bash plspp.sh 

#create all the directories 
for file in data/*
do
    file_name=$(basename $file .wav)   #get the file name 
    mkdir ../GETALP-internship/PLSPP_WER/PLSPP_text/$file_name
done

#copy the txt files in the right directory
for txt_file in text/*
do
    txt_file_name=$(basename $txt_file)   #get the file name
    txt_file_name=${txt_file_name:0:19}   #get the base file name 
    cp $txt_file ../GETALP-internship/PLSPP_WER/PLSPP_text/$txt_file_name        #copy the file in the corresponding directory
done

cd ../GETALP-internship

echo
echo PLEASE SUPPRESS THE TEACHER SEGMENTS FROM THE TEXT FILES DIRECTORY 
echo you can find them by looking a the recording with a speaker2 and supressing the person speaking the least
echo "(press to continue)" 
read

#sort into alphabetical order the timeInfo.csv file
touch PLSPP_WER/TimeInfo/timeInfo_sorted.csv
sort PLSPP_WER/TimeInfo/timeInfo.csv > PLSPP_WER/TimeInfo/timeInfo_sorted.csv


for dir in PLSPP_WER/PLSPP_text/*
do 
    #get the name of the file
    file_name=$(basename $dir)
    echo "working on $file_name..."
    #launch the WER computation
    python PipeFormat4WER.py $file_name  0       #put in the right format + segmentation
    python WER.py $file_name 1                  #compute the WER
    
    #verify that the WER is not too high 
    wer=$(awk '/WER/ {print $3; exit}' "PLSPP_WER/WER/${file_name}_PLSPP.res")      #extract the WER
    wer_float=$(echo "$wer" | bc)   #convert the WER in float
    if (( $(echo "$wer_float >= 0.6" | bc -l) )) 
    then    #the WER is too high
        python PipeFormat4WER.py $file_name  1   #we re-launch the programm but with the speakers in the other order
        python WER.py $file_name 1 
    fi

done

echo "---END---"
