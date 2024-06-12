# GETALP-internship

Globally this internship has been based on [OpenAI's Whisper](https://github.com/openai/whisper).  

- **whisper2txtgrid** 

Convert the *whisper* ".srt" output into a TextGrid file --> Can import to Elan and Praat
Take 2 files as an input (read on keyboard) :<br>
* whisper ".srt" file<br>
* ".TextGrid" file

--------------------------------------------------------------------------------------------
- **WER** 

Compute the *Word Error Count* between the reference from *whisper* and the corrected version.
Give one *WER* by speaker. 

take 3 files as an input (read on keyboard) :
* reference file from whisper
* file containing the corrected text
* result file

**/!\\** the speakers need to be separated manually, both for the reference from whisper and the corrected version :  
    This has to be done on ELAN and exported with the option "texte délimité par des tabulations" and all parameters unchecked.  
    This gives a file of the format : 
    
        speaker1_name      text text text text text
        speaker1_name      text text text text text
        speaker1_name      text text text text text
        speaker2_name      text text text text text
        speaker2_name      text text text text text
        .
        .
        .
        speakern_name      text text text text text

The WER is computed without taking into account ponctuation and capital letters.  
It uses this formula: WER = (Substitutions + insertions + deletions) / total_number_of_words.  
The Algorithm uses the **Levenshtein distance method**.


--------------------------------------------------------------------------------------------
- **WhisperCarbone**

Compute the carbon emissions produced by whisper.  
Uses [codecarbon](https://github.com/mlco2/codecarbon).  

**/!\\** The input file must be changed manually inside the python file. 

Return a .csv with plenty of informations.  
