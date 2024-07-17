# GETALP-internship
This repository has been created in the context of an internship in the team *GETALP* of the computer science laboratory of Grenoble (*LIG)**=. The subject of this internship was:  
**Evaluation of the automatic analysis of French accent in English**.  

The aim was to implement **speech transcription** and **analysis** tools, check and correct the systems' outputs, and finally evaluate the automatic analysis tools on these manually validated annotations.  

----------------------------------------------------------------------------------------------------

* Based on this tool : [plspp](https://gricad-gitlab.univ-grenoble-alpes.fr/lidilem/plspp) and on [OpenAI's Whisper](https://github.com/openai/whisper).  
* The important data is kept and organized [here](https://docs.google.com/spreadsheets/d/1V8g1R39eb_w_HWZOjSdOJWTzMdefQilUtBhCA2uvhWg/edit?usp=sharing).
* The Shell scripts are kept [here](Scripts/)
* The Python programs are kept [here](Python_Programs/)  

----------------------------------------------------------------------------------------------------

**It has been divided into 4 mains steps** :  

## Transcription from Whisper and Computation of the WER

As the PLSPP pipeline is based on OpenAI's Whisper transcription tool, the first objective was to test this tool. To do this, it was needed to compute the Word Error Rate (WER) on a sample of audio files, between the transcription hypothesis issued by Whisper and the reference given manually. At the same time it also permitted to create a *gold corpus* (a corpus that has been meticulously transcribed by hand and guaranteed to be accurate) to use as a reference.  

[See more](Whisper_WER/)  

## Transcription from PLSPP and Computation of the WER  

After testing the PLSPP base individually, the aim was to evaluate the pipeline as a whole and observe the impact of transcription quality on the rest of the measurements.  

PLSPP transcribes audio recordings by dividing them into smaller segments based on the speaker. Transcription is performed using whisperX, but only for segments longer than 8 seconds. This segmentation approach may lead to a loss of context, potentially affecting the understanding of the speech. Therefore, it's important to evaluate whether the transcription quality is impacted by this loss of context by calculating the Word Error Rate (WER) of the text produced by PLSPP.  

[See more](PLSPP_WER/)  

## Impact of the transcription on prosodic measures

One of PLSPP's key features is the measurement of prosody and lexical stress (in other words, the measurement of accentuation). However to compute these measurements uses a transcription performed by [WhisperX](https://github.com/m-bain/whisperX). It is therefore interesting to evaluate the influence of transcription quality on the prosodic results provided by PLSPP. In addition, this evaluation will also enable us to visualize how the accent of French speakers behaves in English, based on the data provided by WhisperX.  

[See more](PLSPP_Prosodic)  

## Comparison of Models and Carbon Emissions

Whisper is a tool that has been trained on different models, some heavier than others. However, in theory, heavier models are supposed to provide better results. The aim of this section is to test this, while also calculating the CO2 emissions of each model, in order to assess the relevance of using a heavier model in PLSPP.  

[See more](emissions)

