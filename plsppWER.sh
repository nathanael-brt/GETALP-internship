#Execute plspp on all the textgrid files from pyannotes (for all the recording furnished)
#Compute the WER for each one of them
echo "---START (press any button)---"
read
#supress all the files in the necessary directories
cd ../plspp
echo "Do you want to launch the pipeline (y/n) ?"
read answer

if [ $answer = "y" ]
then
    rm audio/* benepar/* shape/* syll/* text/* tg/* tgpos/* whisperx/*
    #launch the pipeline
    ./praat_barren scripts/intervalles2wavAndtimetable.praat ../data/ ../pyannote/ .TextGrid ../audio/ 3 0.01 8
    bash plspp.sh 
fi

#create all the directories 
for file in ../GETALP-internship/PLSPP_WER/PLSPP_tg/*
do
    file_name=$(basename $file .TextGrid)   #get the file name 
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
echo Suppression of the teacher transcription files 
echo "(press to continue)" 
read
rm /home/getalp/berthnat/GETALP/GETALP-internship/PLSPP_WER/PLSPP_text/dec2022-003_017-029/dec2022-003_017-029_SPEAKER_00_0.txt
rm /home/getalp/berthnat/GETALP/GETALP-internship/PLSPP_WER/PLSPP_text/jan2023-401_120-034/jan2023-401_120-034_SPEAKER_02_0.txt

#sort into alphabetical order the timeInfo.csv file
touch PLSPP_WER/TimeInfo/timeInfo_sorted.csv
sort PLSPP_WER/TimeInfo/timeInfo.csv > PLSPP_WER/TimeInfo/timeInfo_sorted.csv


for dir in PLSPP_WER/PLSPP_text/*
do 
    #get the name of the file
    file_name=$(basename $dir)
    echo "working on $file_name..."
    #launch the WER computation
    python PipeFormat4WER.py $file_name 0        #put in the right format + segmentation
    python TrueSegmentation.py $file_name          #get the true segmentation
    python WER.py $file_name 1                  #compute the WER
    
    #verify that the WER is not too high 
    wer=$(awk '/WER/ {print $3; exit}' "PLSPP_WER/WER/${file_name}_PLSPP.res")      #extract the WER
    wer_float=$(echo "$wer" | bc)   #convert the WER in float
    if (( $(echo "$wer_float >= 0.9" | bc -l) )) 
    then    #the WER is too high
        python PipeFormat4WER.py $file_name  1   #we re-launch the programm but with the speakers in the other order
        python TrueSegmentation.py $file_name
        python WER.py $file_name 1 
    fi

done

echo "---END---"
