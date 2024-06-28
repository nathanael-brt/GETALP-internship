# GETALP-internship

Based on this tool : [plspp](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) and on [OpenAI's Whisper](https://github.com/openai/whisper).  
The important data is kept and organized [here](https://docs.google.com/spreadsheets/d/1V8g1R39eb_w_HWZOjSdOJWTzMdefQilUtBhCA2uvhWg/edit?usp=sharing).

# Transcription from Whisper and computation of the WER

The goal here is to transcript audio files using Whisper, to correct this transcription from eventual errors and to compute the Word Error Rate for each speaker. 

## Usage

* Launch the `Audio2txtgrid.sh` script. Use the **base** model (More information [here](#audio2txtgrid)):
```bash
./Audio2txtgrid.sh
```
* Import the `.TextGrid` file and the audio on [Elan](https://archive.mpi.nl/tla/elan).
* Split the speakers in different tiers.
* Export using the option *"texte délimité par des tabulations"* into the directory *"Whisper_WER/Whisper-split"*. This will be the non-corrected version of the transcription.
* Correct the transcription
* Export using the option *"texte délimité par des tabulations"* into the directory *"Corrigés/<name_of_the_audio>"*. If it doesn't exist, create it.
* Export using the option *"TextGrid Praat"* into the same directory.
* Execute the python program `WER.py` (More information [here](#WER)): 
```bash
python WER.py <name_of_the_audio_file_without_ext> 0
```
   

# Comparison of models and carbon emissions

The goal here is to compare the models base and medium of Whisper and to compute the carbon emissions of a transcription on each of these models. 

## Usage

* Install the [codecarbon](https://github.com/mlco2/codecarbon) package for python :
```bash
#using pip
pip install codecarbon

#using conda
conda install -c conda-forge codecarbon
```
* Launch the ```WhisperCarbone.py``` program. More information [here](#WhisperCarbone).
```bash
python WhisperCarbone.py
```

# User Manual

## Python programs

### whisper2txtgrid

When using Whisper on an audio file, we get several files as an output.  
This program converts the `.srt` output into a `.TextGrid` file : In this format we can import our transcription into **Elan** or **Praat**.  
It Take 2 files as an input (read on keyboard) :<br>
* The `.srt` file generated by Whisper<br>
* A `.TextGrid` file (Where the output will be written).  

--------------------------------------------------------------------------------------------
### WER

Computes the **Word Error Count** between the reference from *whisper* and the manually corrected version.
Gives one *WER* by speaker. 

It takes 2 inputs (to give when executing the file) :
* The base name of the file you are working on (the name of the audio file without the `.wav` extension) 
* Either 0 or 1 depending on which WER you want to compute :
    * 0 to compute the WER from whisper, read automatically the reference and hypothesis files as long as they have the right name :
         - `Whisper_WER/Whisper-split/<file_name>-split.txt`
         - `Corrigés/<file_name>/<file_name>.txt`.
    * 1 to compute the WER from PLSPP, ead automatically the reference and hypothesis files as long as they have the right name :
        - `PLSPP_WER/PLSPP_WER_format/<file_name>_pipeRes.txt`
        - `PLSPP_WER/Corr_WER_format/<file_name>_corRes.txt`

In both cases the program creates a `.res` result file in the corresponding directory (*"Whisper_WER/WER"* for 0 and *"PLSPP_WER/WER"* for 1)

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

Returns a `.csv` with plenty of informations on not only the carbon emissions but also the power consumption, the cpu, gpu, etc...  

--------------------------------------------------------------------------------------------
### functions

Python file containing several fucntions to be used and included in other programs : 
* `teacher_nb()`  
  Function computing the tier number of the teacher in the TextGrid file from pyannote in PLSPP. It finds the teacher by searching the speakers who speaks during the least number of segments. Returns -1 if there is no teacher (only 2 speakers).
* `is_speaker_order_normal()`  
  Function returning a boolean stating if the speaker order is in reverse or not (if the speaker with the least number, other than the teacher, is speaking first or not).

--------------------------------------------------------------------------------------------
### PipeFormat4WER

This program is useful for the computation of the WER using the segments given by **PLSPP**.   
It puts the transcription from PLSPP and the correction into the **right format** to give to the WER compuation program (the format described [here](#WER).  

It it takes 2 inputs (to give as arguments when executing it):
* The name of the base audio file that has been transcripted (without the ```.wav``` of the extension).
* An integer, `0` or `1`: if `0` is given then nothing changes in the program, but if ```1``` is given then the order of the speakers returned by the function `is_speaker_order_normal()`  is reversed.  

The program creates automatically 2 results files :
* `PLSPP_WER/PLSPP_WER_format/<name_of_the_file>_pipeRes.txt` for the transcription from PLSPP.
* `PLSPP_WER/Corr_WER_format/<name_of_the_file>_corRes.txt` for the correction.

To convert the transcription from PLSPP into the right format it uses the `.txt` output files of the pipeline (the ones that contain only the text of each segment) that sould have been placed into the *"PLSPP_WER/PLSPP_text/<name_of_the_file>/"* directory.  

To convert the correction into the right format it uses the file `PLSPP_WER/TimeInfo/timeInfo_sorted.csv` that give info on the timing of each segment and the TextGrid file containing the correction.   

To assure ourselves that we write both files with the speakers in the same order (necessary for the WER computation) we use the function `is_speaker_order_normal()` to find who is the first to speak according to PLSPP transcription, then write the correction file accordingly.   

## Scripts

### Audio2txtgrid

This script simultaneously launch Whisper on a given audio file, create the necessary files/directories and translate the newly generated `.srt` file into a `.TextGrid` file (by executing the [whisper2txtgrid](#whisper2txtgrid) python program).  
It takes 2 inputs:   
* The audio file to be transcripted.  
* The model of Whisper to use.  

When executing the `whisper2txtgrid.py` program, 2 files are needed as inputs, these files have been created earlier in the script:   
* The `.srt` has been created in the *"srt"* folder.   
* The `.TextGrid` has been created in the *"Textgrid"* folder.
These files have the same name as the audio file. 

The script also create a folder in the *"Whisper"* folder, who's name is the same as the name of the audio file. This where all the files generated by Whisper will be kept. 




