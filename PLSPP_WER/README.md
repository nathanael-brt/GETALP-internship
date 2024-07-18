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


