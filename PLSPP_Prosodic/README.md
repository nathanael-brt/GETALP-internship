# Impact of the transcription on prosodic measures

The goal here is to evaluate the impact of the quality of the transcription on the prosodic measures output of PLSPP.  

## Usage
For PLSPP and PLSPP_MFA just launch the pipeline, move the `stressTable.csv` into the *"PLSPP_Prosodic/Tables/"* directory, rename it correctly and launch `ProsodicData.py` with either `0` or `1` as parameter.  

For PLSPP_MFA with the text from the gold corpus instead of using WhisperX for the transcription:  
* Make sure PLSPP is installed into the *"GETALP-internship/../plspp/"* directory as well as [MFA](https://montreal-forced-aligner.readthedocs.io/) to align the text.   
* Launch the `ProsodicDataFromCorpus.sh` script (more information [here](#ProsodicDataFromCorpus)):  
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
* Launch the `ProsodicData.py` program with `2` as parameter (more information [here](#ProsodicData)) :
```bash
python ProsodicData.py 2
```

# User Manual

## Python programs

--------------------------------------------------------------------------------------------
### MFA_segmented_files
This program transforms all the segments of corrected text (that have been correctly segmented according to the segments form PSLPP using [TrueSegmentation.py ](PLSPP_WER/README.md#TrueSegmentation)) into single files (1 file by segment).  

It takes no input and automatically reads all the files that are stored into the directory *"PLSPP_WER/Corr_WER_format_segmented/"*.   

It creates all the files into the directory *"PLSPP_Prosodic/Corpus_segmented/"*.

--------------------------------------------------------------------------------------------
### ProsodicData 
This program is useful to recolt and organize all the prosodic data contained into the "*stress_table*" output from PLSPP. More precisely the proportion of words pronounced correctly.  

It generates one data file per speaker as well as a final file containing the total data for all the table.  

It take one integer as an argument.   

* If `0` is given :  
  This is to recolt the data when PLSPP alone has been used.  
  The program reads the data from the file `PLSPP_Prosodic/Tables/PLSPPstressTable.csv`.  
  The program writes the speaker files into the *"PLSPP_Prosodic/PLSPP_data/"* directory and generates this total file :  `PLSPP_Prosodic/Total_data/PLSPP_total_data.csv`.  
  
* If `1` is given :  
  This is to recolt the data when PLSPP_MFA alone has been used.  
  The program reads the data from the file `PLSPP_Prosodic/Tables/PLSPPMFAstressTable.csv`.  
  The program writes the speaker files into the *"PLSPP_Prosodic/PLSPP_MFA_data/"* directory and generates this total file :  `PLSPP_Prosodic/Total_data/PLSPP_MFA_total_data.csv`.

* Else :  
  This is to recolt the data when PLSPP_MFA has been used with the text from the reference instead of using WhisperX.  
  The program reads the data from the file `PLSPP_Prosodic/Tables/RefstressTable.csv`.  
  The program writes the speaker files into the *"PLSPP_Prosodic/Ref_data/"* directory and generates this total file :  `PLSPP_Prosodic/Total_data/Ref_total_data.csv`.  

The speaker files are of this format (if there is no data for one line it is not written) :  
```
number of words;<>
prop correct 2-syll;<>
prop correct Oo;<>
prop corect oO;<>
prop correct 3-syll;<>
prop correct Ooo;<>
prop correct oOo;<>
prop correct ooO;<>
prop correct 4-syll;<>
prop correct Oooo;<>
prop correct oOoo;<>
prop correct ooOo;<>
prop correct oooO;<>
```

The total data file is of this format :  
```
number of words;<>

number of 2-syll words;<>
number of correct 2-syll words;<>
prop correct 2-syll;<>

number of Oo pattern words;<>
number of correct Oo pattern words;<>
prop correct Oo;<>

number of oO pattern words;<>
number of correct oO pattern words;<>
prop corect oO;<>

number of 3-syll words;<>
number of correct 3-syll words;<>
prop correct 3-syll;<>

number of Ooo pattern words;<>
number of correct Ooo pattern words;<>
prop correct Ooo;<>

number of oOo pattern words;<>
number of correct oOo pattern words;<>
prop correct oOo;<>

number of ooO pattern words;<>
number of correct ooO pattern words;<>
prop correct ooO;<>

number of 4-syll words;<>
number of correct 4-syll words;<>
prop correct 4-syll;<>

number of Oooo pattern words;<>
number of correct Oooo pattern words;<>
prop correct Oooo;<>

number of oOoo pattern words;<>
number of correct oOoo pattern words;<>
prop correct oOoo;<>

number of ooOo pattern words;<>
number of correct ooOo pattern words;<>
prop correct ooOo;<>

number of oooO pattern words;<>
number of correct oooO pattern words;<>
prop correct oooO;<>
```
  
## Scripts

### ProsodicDataFromCorpus
This script permits to launch PLSPP_MFA but replaces the WhisperX step output by the text from the gold corpus to have a manual transcription instead of an automatic one.  

To work, it needs PLSPP to be installed into the *"GETALP-internship/../plspp/"* directory. It also needs [MFA](https://montreal-forced-aligner.readthedocs.io/) to align the text. 
It also need the `intervalles2wavAndtimetable.praat` script to be into the *"plspp/scripts"* directory.  

It first creates and transfer the file necessary to PLSPP_MFA using [MFA_segmented_files.py](#MFA_segmented_files) and then launch the pipeline without the transcription part. 
