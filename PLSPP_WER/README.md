# Transcription from PLSPP and Computation of the WER

The goal here is to evaluate the quality of the transcription given by PLSPP by computing its WER and comparing it with the WER of the transcription from Whisper.   

PLSPP transcribes audio recordings by segmenting them (by speaker) into smaller segments. Transcription is conducted using [whisperX](https://github.com/m-bain/whisperX), but only for segments longer than 8 seconds. This segmentation approach may introduce contextual losses that could potentially impact speech transcription. Therefore, it is crucial to assess whether transcription quality is affected by these contextual losses by calculating the Word Error Rate (WER) of the text produced by PLSPP.

## Usage

* Create the directory to install PLSPP in:
    ```bash
    mkdir ../plspp
    ```
* Install [PLSPP](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) in this directory.
* Launch the script `plsppWER.sh` (more information [here](../Scripts/README.md#plsppWER)):
    ```bash
    ./plsppWER.sh
    ```

## Data Informations
Here is a description of what contains each folder : 
* **Corr_WER_format** : The corrected transcription with only the segments corresponding to PLSPP segments (but not segmented correctly) in the format necessary to compute the WER. Outputs of [PipeFormat4WER.py](../Python_Programs/README.md#PipeFormat4WER).  
* **Corr_WER_format_segmented** : The corrected transcription with only the segments corresponding to PLSPP segments in the format necessary to compute the WER but this time segmented correctly. Outputs of [TrueSegmentation.py](../Python_Programs/README.md#TrueSegmentation).
* **PSLPP_WER_format** : The transcription files from PLSPP put in the format necessary to compute the WER. Outputs of [PipeFormat4WER.py](../Python_Programs/README.md#PipeFormat4WER).  
* **PLSPP_text** : The direct transcription outputs of PLSPP, one file per segment.   
* **PLSPP_tg** : The TextGrids used to run PLSPP, normally given by pyannote. Give the segmentation.  
* **TimeInfo** : Output of the `intervalles2wavAndtimetable.praat` script, as well as the sorted version of it.  
* **WER** : Results files containing the WER of each speaker.  
