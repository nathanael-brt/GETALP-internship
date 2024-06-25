#Execute plspp on all the textgrid files from pyannotes (for all the recording furnished)
#Compute the WER for each one of them
echo "---START (press any button)---"
read
#supress all the files in the necessary directories
cd ../plspp
rm audio/* benepar/* shape/* syll/* text/* tg/* tgpos/* whisperx/*