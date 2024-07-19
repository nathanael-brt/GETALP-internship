# Transcription from Whisper and Computation of the WER

The goal here is to transcribe audio files using Whisper, correct this transcription for any errors to build a *gold corpus* (a corpus that has been meticulously transcribed by hand and guaranteed to be accurate), and compute the Word Error Rate for each speaker.  

It is important to precise that when we correct the transcription we mostly correct the text. The alignment has been rarely modified and we generally kept the one given by Whisper (even if it was not optimal).  

## Usage

* Launch the `Audio2txtgrid.sh` script. Use the **base** model (More information [here](../Scripts/README.md#audio2txtgrid)):
    ```bash
    ./Audio2txtgrid.sh
    ```
* Import the `.TextGrid` file and the audio into [Elan](https://archive.mpi.nl/tla/elan).
* Split the speakers into different tiers.
* Export using the option *"texte délimité par des tabulations"* into the directory *"Whisper_WER/Whisper-split"*. This will be the non-corrected version of the transcription.
* Correct the transcription.
* Export using the option *"texte délimité par des tabulations"* into the directory *"Corrigés/<name_of_the_audio>"*. If it doesn't exist, create it.
* Export using the option *"TextGrid Praat"* into the same directory.
* Execute the Python program `WER.py` (More information [here](../Python_Programs/README.md#WER)): 
    ```bash
    python WER.py <name_of_the_audio_file_without_ext> 0
    ```


