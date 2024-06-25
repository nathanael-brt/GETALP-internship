#Execute plspp on all the textgrid files from pyannotes (for all the recording furnished)
#Compute the WER for each one of them
echo "---START (press any button)---"
read
#supress all the files in the necessary directories
cd ../plspp
rm audio/* benepar/* shape/* syll/* text/* tg/* tgpos/* whisperx/*
#launch the pipeline
./praat_barren scripts/intervalles2wavAndtimetable.praat ../data/ ../pyannote/ .TextGrid ../audio/ 3 0.01 8
bash plspp.sh 

#create all the directories 
for file in data/*
do
    file_name=$(basename $file .wav)   #get the file name 
    mkdir ../GETALP-internship/PLSPP_WER/PLSPP_text/$file_name
done

#copy the txt files in the right directory
for txt_file in text/*
do
    txt_file_name=${txt_file:0:19}   #get the base file name 
    cp txt_file ../GETALP-internship/PLSPP_WER/PLSPP_text/$txt_file_name        #copy the file in the corresponding directory
done

cd ../GETALP-internship

for dir in PLSPP_WER/PLSPP_text/*
do 
    #get the name of the file
    file_name=$(basename $dir)
    echo "working on $file_name..."
    #launch the WER computation
    python PipeFormat4WER.py $file_name         #put in the right format + segmentation
    python WER.py $file_name 1                  #compute the WER
done

echo "---END---"
