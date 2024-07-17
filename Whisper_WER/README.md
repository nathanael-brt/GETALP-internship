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


