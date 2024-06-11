# GETALP-internship

- whisper2txtgrid -

Convert the whisper ".srt" output into a TextGrid file --> Can import to Elan and Praat
Take 2 files as an input (read on keyboard) : 
    -whisper ".srt" file
    -output ".TextGrid" file

--------------------------------------------------------------------------------------------
- WER -

Compute the Word Error Count between the reference from whisper and the corrected version.
Give one WER by speaker. 

take 3 files as an input (read on keyboard) :
    -reference file from whisper 
    -file containing the corrected text 
    -result file

/!\ the speakers need to be separated manually, both for the reference from whisper and the corrected version : 
    This has to be done on ELAN and exported with the option "texte délimité par des tabulations" and all parameters unchecked. 
    This gives a file of the format : 
    
        speaker1_name	   text text text text text
        speaker1_name      text text text text text
        speaker1_name      text text text text text
        speaker2_name      text text text text text
        speaker2_name      text text text text text
        .
        .
        .
        speakern_name      text text text text text

The WER is computed without taking into account ponctuation and capital letters 
It uses this formula: WER = (Substitutions + insertions + deletions) / total_number_of_words 
The Algorithm uses the Levenshtein distance method
