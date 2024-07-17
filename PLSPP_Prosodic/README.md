# Impact of the transcription on prosodic measures

The goal here is to evaluate the impact of the quality of the transcription on the prosodic measures output of 3 different versions of PLSPP:   
* PLSPP v1: the `pslpp.sh` script. Uses WhisperX for the transcription. 
* PLSPP_MFA (PLSPP v2): the `pslpp_mfa.sh` script, version 2 of PLSPP using the MFA aligner to add a forced alignment step at the phoneme level. Syllabic prosodic features are extracted at the vowel level, rather than at the syllable nucleus level. In this version, word-level alignment is also performed by MFA. Still uses WhisperX for yhe transcription.
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


