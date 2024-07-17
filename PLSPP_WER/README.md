# Transcription from PLSPP and Computation of the WER

The goal here is to evaluate the quality of the transcription given by PLSPP by computing its WER and comparing it with the WER of the transcription from Whisper.   
PLSPP uses [whisperX](https://github.com/m-bain/whisperX) to produce the transcription and works on segmented parts of the recording instead of working on the whole recording.

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


