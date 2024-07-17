# Transcription from PLSPP and Computation of the WER

The goal here is to evaluate the quality of the transcription given by PLSPP by computing its WER and comparing it with the WER of the transcription from Whisper.   
PLSPP transcribes audio recordings by dividing them into smaller segments based on the speaker. Transcription is performed using [whisperX](https://github.com/m-bain/whisperX), but only for segments longer than 8 seconds. This segmentation approach may lead to a loss of context, potentially affecting the understanding of the speech. Therefore, it's important to evaluate whether the transcription quality is impacted by this loss of context by calculating the Word Error Rate (WER) of the text produced by PLSPP.  

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


