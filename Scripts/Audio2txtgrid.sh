#simultaneously launch Whisper on a given audio file, create the necessary files/directories and translate the newly generated .srt file into a .TextGrid file
#---
#takes 2 inputs (read on keyboard during the script's execution):   
#   The audio file to be transcripted.  
#   The model of Whisper to use.  
#----------------------------------------------------------------------------------------------------------------------
echo "--STARTING--"
read
#read the parameters
echo Audio file path : 
read file_path 
echo Model : 
read model
#create the corresponding directory
file_name=$(basename $file_path .wav)   #get the file name from the path
cd ../Whisper_WER
cd Whisper
mkdir $file_name
cd $file_name
#execute whisper
whisper $file_path --model $model --language en
#Textgrid format
cp *.srt ../../srt/  #copy the .srt file in the correspondind directory
cd ../../
touch Textgrid/$file_name.TextGrid  #create the .TextGrid file
chmod a+w Textgrid/$file_name.TextGrid
#execute the python program
cd Python_Programs
python whisper2txtgrid.py
cd ..
echo "--GOODBYE--"