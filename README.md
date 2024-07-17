# GETALP-internship
This repository has been created in the context of an internship in the team GETALP of the computer science laboratory of Grenoble (LIG). The subject of this internship was:  
**Evaluation of the automatic analysis of French accent in English**.  

Based on this tool : [plspp](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) and on [OpenAI's Whisper](https://github.com/openai/whisper).  
The important data is kept and organized [here](https://docs.google.com/spreadsheets/d/1V8g1R39eb_w_HWZOjSdOJWTzMdefQilUtBhCA2uvhWg/edit?usp=sharing).

The aim of this internship was to implement the speech transcription and analysis tools, check and correct the systems' outputs, and finally evaluate the automatic analysis tools on these manually validated annotations. 

It has been divided into 4 mains steps :  

## Transcription from Whisper and Computation of the WER

[See more](Whisper_WER/)

As the PLSPP pipeline is based on OpenAI's Whisper transcription tool, the first objective was to test this tool. To do this, it was needed to compute the Word Error Rate (WER) on a sample of audio files, between the transcription hypothesis issued by Whisper and the reference given manually. At the same time it also permitted to create a *gold corpus* (a corpus that has been meticulously transcribed by hand and guaranteed to be accurate) to use as a reference. 





