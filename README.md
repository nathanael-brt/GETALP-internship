# GETALP-internship

Based on this tool : [plspp](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) and on [OpenAI's Whisper](https://github.com/openai/whisper).  
The important data is kept and organized [here](https://docs.google.com/spreadsheets/d/1V8g1R39eb_w_HWZOjSdOJWTzMdefQilUtBhCA2uvhWg/edit?usp=sharing).

# Python programs
--------------------------------------------------------------------------------------------
- **whisper2txtgrid** 

When using Whisper on an audio file, we get several files as an output.  
This program convert the ```.srt``` output into a ```.TextGrid``` file : In this format we can import  our transcription to **Elan** or **Praat**.  
It Take 2 files as an input (read on keyboard) :<br>
* The ```.srt``` file generated by Whisper<br>
* A ```.TextGrid``` file (Where the output will be written).  

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

It uses this formula:  $`\text{WER} = \frac{\text{Substitutions} + \text{Insertions} + \text{Deletions}}{\text{total\_number\_of\_words}}`$  
 
The Algorithm uses the **Levenshtein distance method**.


--------------------------------------------------------------------------------------------
- **WhisperCarbone**

Compute the carbon emissions produced by whisper depending on a chosen whisper model.  
Uses [codecarbon](https://github.com/mlco2/codecarbon) and the whisper library of python.  

Takes a whisper model and an audio file as inputs.  
**/!\\** The input file must be changed manually inside the python file. 

Return a .csv with plenty of informations on not only the carbon emissions but also the power consumption, the cpu, gpu, etc...  
