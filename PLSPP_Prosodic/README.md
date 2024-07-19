# Impact of the transcription on prosodic measures

The goal here is to evaluate the impact of the quality of the transcription on the prosodic measures output of 3 different versions of PLSPP:   
* PLSPP v1: the `pslpp.sh` script. Uses [WhisperX](https://github.com/m-bain/whisperX) for the transcription. 
* PLSPP_MFA (PLSPP v2): the `pslpp_mfa.sh` script, version 2 of PLSPP using the MFA aligner to add a forced alignment step at the phoneme level. Syllabic prosodic features are extracted at the vowel level, rather than at the syllable nucleus level. In this version, word-level alignment is also performed by MFA. Still uses WhisperX for the transcription.
* PLSPP_MFA but we replace the transcription with the corrected text of the gold corpus.   

We also want to compare these versions using the data the we obtained: 

**Table of comparison of PLSPP versions**

| \|**Text source**<br> -------------<br> **Version PLSPP**\|<br> | **WhisperX**           | **Gold Corpus** |
|-----------------------------------------------------------------|------------------------|-----------------|
| **PLSPP (v1)**                                                  |    x<br>     \|        |                 |
| **PSLPP_MFA (v2)**                                              |    \|<br>    x-------------- | <br>  ------x   |

## Usage
For PLSPP and PLSPP_MFA just launch the pipeline, move the `stressTable.csv` into the *"PLSPP_Prosodic/Tables/"* directory, rename it correctly (respectively `PLSPPstressTable.csv` and `PLSPPMFAstressTable.csv`), and launch `ProsodicData.py` with either `0` or `1` as the parameter.  

For PLSPP_MFA with the text from the gold corpus instead of using WhisperX for the transcription:  
* Make sure PLSPP is installed in the *"../plspp/"* directory as well as [MFA](https://montreal-forced-aligner.readthedocs.io/) to align the text.   
* Launch the `ProsodicDataFromCorpus.sh` script (more information [here](../Scripts/README.md#ProsodicDataFromCorpus)):  
    ```bash
    ./ProsodicDataFromCorpus.sh
    ```
* Transfer the `stressTable.csv` file into the *"PLSPP_Prosodic/Tables/"* directory and rename it correctly.  
    ```bash
    # from the GETALP-internship/ directory
    mv ../plspp/stressTable.csv PLSPP_Prosodic/Tables/
    cd PLSPP_Prosodic/Tables/
    mv stressTable.csv RefstressTable.csv
    ```
* Launch the `ProsodicData.py` program with `2` as the parameter (more information [here](../Python_Programs/README.md#ProsodicData)):  
    ```bash
    python ProsodicData.py 2
    ```

## Data Informations 
Here is a description of what each folder contains:  
* **Corpus_segmented** : Files representing all segments of the gold corpus to be used with MFA. One ile represents one line of the files in [PLSPP_WER/Corr_WER_format_segmented/](../PLSPP_WER/Corr_WER_format_segmented). Outputs of [MFA_segmented_files.py](../Python_Programs/README.md#MFA_segmented_files).  
* **PLSPP_MFA_data** : Outputs of [ProsodicData.py](../Python_Programs/README.md#ProsodicData) using the data from PLSPP_MFA.  
* **PLSPP_data** : Outputs of [ProsodicData.py](../Python_Programs/README.md#ProsodicData) using the data form PLSPP.  
* **Ref_data** : Outputs of [ProsodicData.py](../Python_Programs/README.md#ProsodicData) using the data form PLSPP_MFA but with the transcription replaced by the text of the gold corpus.  
* **Summaries** : Summaries of the data from the 3 precedent folder in form of global `.csv` tables.  
* **Tables** : sressTable outputs from PLSPP.
* **Total_data** : Outputs of [ProsodicData.py](../Python_Programs/README.md#ProsodicData). Total data tables. 

