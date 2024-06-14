# GETALP-internship

Based on this tool : [plspp](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) and on [OpenAI's Whisper](https://github.com/openai/whisper).  
The important data is kept and organized [here](https://docs.google.com/spreadsheets/d/1V8g1R39eb_w_HWZOjSdOJWTzMdefQilUtBhCA2uvhWg/edit?usp=sharing).

# Transcription from Whisper and computation of the WER

The goal here is to transcript audio files using Whisper, to correct this transcription from eventual errors and to compute the Word Error Rate for each speaker. 

## Usage

* Launch the ```Audio2txtgrid.sh``` script. More information [here](#audio2txtgrid).
* Import the ```.TextGrid``` file and the audio on [Elan](https://archive.mpi.nl/tla/elan).
* Split the speakers in different tiers.
* Export using the option *"texte délimité par des tabulations"* into the directory *"Whisper-split"*. This will be the non-corrected version of the transcription.
* Correct the transcription
* Export using the option *"texte délimité par des tabulations"* into the directory *"Corrigés/<name_of_the_audio>"*. If it doesn't exist, create it.
* Export using the option *"TextGrid Praat"* into the same directory.
* Create the result file (```.res```) in the directory *"WER"*.
* Execute the python programm ```WER.py```. More information [here](#WER)
  
# User Manual

## Python programs

### whisper2txtgrid

When using Whisper on an audio file, we get several files as an output.  
This program converts the ```.srt``` output into a ```.TextGrid``` file : In this format we can import our transcription into **Elan** or **Praat**.  
It Take 2 files as an input (read on keyboard) :<br>
* The ```.srt``` file generated by Whisper<br>
* A ```.TextGrid``` file (Where the output will be written).  

--------------------------------------------------------------------------------------------
### WER

Computes the **Word Error Count** between the reference from *whisper* and the manually corrected version.
Gives one *WER* by speaker. 

It takes 3 files as an input (read on keyboard) :
* The reference file from whisper
* The file containing the corrected text
* The result file (```.res```)  

**/!\\** the speakers need to be separated manually, both for the reference from whisper and the corrected version :  
    This has to be done on **ELAN** and exported with the option *"texte délimité par des tabulations"* and all parameters unchecked.  
    This gives a file of the format : 

```
speaker1_name      text text text text text
speaker1_name      text text text text text
speaker1_name      text text text text text
speaker2_name      text text text text text
speaker2_name      text text text text text
.
.
.
speakern_name      text text text text text
```
**The reference and the correction both need to be in this format, with the speakers in the same order**  

The WER is computed without taking into account ponctuation and capital letters.  

It uses this formula:  $`\text{WER} = \frac{\text{Substitutions} + \text{Insertions} + \text{Deletions}}{\text{total\_number\_of\_words}}`$  
 
The Algorithm uses the **Levenshtein distance method**.

--------------------------------------------------------------------------------------------
### WhisperCarbone

Computes the carbon emissions produced by whisper in function on a chosen whisper model.  
Uses the [codecarbon](https://github.com/mlco2/codecarbon) and whisper packages for python.  

Takes a whisper model and an audio file as inputs.   

Returns a ```.csv``` with plenty of informations on not only the carbon emissions but also the power consumption, the cpu, gpu, etc...  

## Scripts

### Audio2txtgrid

This script simultaneously launch Whisper on a given audio file, create the necessary files/directories and translate the newly generated ```.srt``` file into a ```.TextGrid``` file (by executing the [whisper2txtgrid python program](#whisper2txtgrid).
It takes 2 inputs: 
*The audio file that to be transcripted.
*The model of whisper to use.  

When executing the ```whisper2txtgrid.py``` program, 2 files are needed as inputs, these files have been created earlier in the script:   
* The ```.srt```has been created in the *"srt"* folder.   
* The ```.TextGrid``` has been created in the *"Textgrid"* folder.
These files have the same name as the audio file. 

The script also create a folder in the *"Whisper"* folder, who's name is the same as the name of the audio file. This where all the files generated by Whisper will be kept. 




