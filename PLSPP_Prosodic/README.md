# Impact of the transcription on prosodic measures

The goal here is to evaluate the impact of the quality of the transcription on the prosodic measures output of 3 different versions of PLSPP :   
* PLSPP v1 : the `pslpp.sh` script.  
* PLSPP_MFA (PLSPP v2) : the `pslpp_mfa.sh` script, version 2 of PLSPP using the MFA aligner to add a forced alignment step at phoneme level. Syllabic prosodic features are extracted at vowel level, rather than at syllable nucleus level. In this version, word level alignment is also performed by MFA.
* PLSPP_MFA but we replace the transcription by the corrected text of the gold corpus.   

## Usage
For PLSPP and PLSPP_MFA just launch the pipeline, move the `stressTable.csv` into the *"PLSPP_Prosodic/Tables/"* directory, rename it correctly and launch `ProsodicData.py` with either `0` or `1` as parameter.  

For PLSPP_MFA with the text from the gold corpus instead of using WhisperX for the transcription:  
* Make sure PLSPP is installed into the *"GETALP-internship/../plspp/"* directory as well as [MFA](https://montreal-forced-aligner.readthedocs.io/) to align the text.   
* Launch the `ProsodicDataFromCorpus.sh` script (more information [here](../Scripts/README.md#ProsodicDataFromCorpus)):  
```
./ProsodicDataFromCorpus.sh
```
* transfer the `stressTable.csv` file into the *"PLSPP_Prosodic/Tables/"* directory and rename it correctly.  
```bash
#from the GETALP-internship/ directory
mv ../plspp/stressTable.csv PLSPP_Prosodic/Tables/
cd PLSPP_Prosodic/Tables/
mv stressTable.csv RefstressTable.csv
```
* Launch the `ProsodicData.py` program with `2` as parameter (more information [here](../Python_Programs/README.md#ProsodicData)) :
```bash
python ProsodicData.py 2
```

