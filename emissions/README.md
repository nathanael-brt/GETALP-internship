# Comparison of models and carbon emissions

The goal here is to compare the *base* and *medium* models of Whisper and to compute the carbon emissions of a transcription on each of these models. 

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

### WhisperCarbone

Computes the carbon emissions produced by whisper in function on a chosen whisper model.  
Uses the [codecarbon](https://github.com/mlco2/codecarbon) and whisper packages for python.  

Takes a whisper model and an audio file as inputs.   

Returns a `.csv` with plenty of informations on not only the carbon emissions but also the power consumption, the cpu, gpu, etc...  
