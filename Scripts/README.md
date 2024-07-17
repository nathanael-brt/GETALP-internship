# Scripts

## Audio2txtgrid

This script simultaneously launch Whisper on a given audio file, create the necessary files/directories and translate the newly generated `.srt` file into a `.TextGrid` file (by executing the [whisper2txtgrid](#whisper2txtgrid) python program).  
It takes 2 inputs (read on keyboard during the script's execution):   
* The audio file to be transcripted.  
* The model of Whisper to use.  

When executing the `whisper2txtgrid.py` program, 2 files are needed as inputs, these files have been created earlier in the script:   
* The `.srt` has been created in the *"srt"* folder.   
* The `.TextGrid` has been created in the *"Textgrid"* folder.
These files have the same name as the audio file. 

The script also create a folder in the *"Whisper"* folder, who's name is the same as the name of the audio file. This where all the files generated by Whisper will be kept. 

--------------------------------------------------------------------------------------------
## plsppWER

This script permits to compute the WER of the transcription from PLSPP.  

**/!\\** To work correctly this script needs plspp to be installed in this directory: *"GETALP-internship/../plspp"* as well the `intervalles2wavAndtimetable.praat` script to be into the *"plspp/scripts"* directory.    

It also needs the `timeInfo.csv` giving info on the timing of each PLSPP segment in this format:
```csv
File;Speaker;Segment;Start;End;Duration
<name_of_the_file1>.wav;SPEAKER_01;<name_of_the_file1>_SPEAKER_01_0;<start_timing>;<end_timing>;<duration>
...
<name_of_the_filen>.wav;SPEAKER_m;<name_of_the_filen>_SPEAKER_m_k;<start_timing>;<end_timing>;<duration>
```
If you launch the pipeline this file is generated automatically else it needs to be stored into the directory *"PLSPP_WER/TimeInfo"*.  

When executing the script it is possible to decide if it launches or not PSLPP, it then transfer all the necessary files into the right directories, sort the `timeInfo.csv` file into the `timeInfo_sorted.csv` file, then calls [PipeFormat4WER.py](#PipeFormat4WER), [TrueSegmentation.py](#TrueSegmentation) and [WER.py](#WER) on each file to compute the WER.  

If the script detects that the WER is too big (≥0.9) it considers that there is an error, changes the order of the speaker and recomputes the WER. 

--------------------------------------------------------------------------------------------
## ProsodicDataFromCorpus
This script permits to launch PLSPP_MFA but replaces the WhisperX step output by the text from the gold corpus to have a manual transcription instead of an automatic one.  

To work, it needs PLSPP to be installed into the *"GETALP-internship/../plspp/"* directory. It also needs [MFA](https://montreal-forced-aligner.readthedocs.io/) to align the text. 
It also need the `intervalles2wavAndtimetable.praat` script to be into the *"plspp/scripts"* directory.  

It first creates and transfer the file necessary to PLSPP_MFA using [MFA_segmented_files.py](#MFA_segmented_files) and then launch the pipeline without the transcription part. 