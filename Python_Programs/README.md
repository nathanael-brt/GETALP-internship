# Python programs
## User manual

### whisper2txtgrid

When using Whisper on an audio file, several files are produced as output.  
This program converts the `.srt` output into a `.TextGrid` file. In this format, we can import our transcription into **Elan** or **Praat**.  
It takes 2 files as input (read from the keyboard):<br>
* The `.srt` file generated by Whisper
* A `.TextGrid` file (where the output will be written).  

--------------------------------------------------------------------------------------------
### WER

Computes the **Word Error Rate** between the reference from *Whisper* and the manually corrected version.
Provides one *WER* per speaker. 

It takes 2 inputs (to be provided when executing the file):
* The base name of the file you are working on (the name of the audio file without the `.wav` extension) 
* Either 0 or 1, depending on which WER you want to compute:
    * 0 to compute the WER from Whisper, reading automatically the reference and hypothesis files as long as they have the correct names:
         - `Whisper_WER/Whisper-split/<file_name>-split.txt`
         - `Corrigés/<file_name>/<file_name>.txt`.
    * 1 to compute the WER from PLSPP, reading automatically the reference and hypothesis files as long as they have the correct names:
        - `PLSPP_WER/PLSPP_WER_format/<file_name>_pipeRes.txt`
        - `PLSPP_WER/Corr_WER_format/<file_name>_corRes.txt`

In both cases, the program creates a `.res` result file in the corresponding directory (*"Whisper_WER/WER"* for 0 and *"PLSPP_WER/WER"* for 1).

**/!\\** Speakers need to be separated manually, both for the reference from Whisper and the corrected version.  
This needs to be done in **ELAN** and exported with the option *"texte délimité par des tabulations"* and all parameters unchecked.  
This results in a file in the format: 

```
speaker1_name      text text text text text
speaker1_name      text text text text text
speaker1_name      text text text text text
speaker2_name      text text text text text
speaker2_name      text text text text text
.
.
.
speakern_name      text text text text text
```
**Both the reference and the correction must be in this format, with speakers in the same order.**  

The WER is computed without taking into account punctuation and capital letters.  
It uses this formula:  $`\text{WER} = \frac{\text{Substitutions} + \text{Insertions} + \text{Deletions}}{\text{total\_number\_of\_words}}`$  

The algorithm uses the **Levenshtein distance method**.

--------------------------------------------------------------------------------------------
### WhisperCarbone

Computes the carbon emissions produced by Whisper based on a chosen Whisper model.  
Uses the [codecarbon](https://github.com/mlco2/codecarbon) and Whisper packages for Python.  

Takes a Whisper model and an audio file as inputs.   
Returns a `.csv` with extensive information not only on carbon emissions but also on power consumption, CPU, GPU, etc...  

--------------------------------------------------------------------------------------------
### functions

Python file containing several functions to be used and included in other programs: 
* `teacher_nb()`  
  Function that computes the tier number of the teacher in the TextGrid file from Pyannote in PLSPP. It finds the teacher by identifying the speaker who speaks during the fewest number of segments. Returns -1 if there is no teacher (only 2 speakers).
* `is_speaker_order_normal()`  
  Function that returns a boolean indicating if the speaker order is reversed or not (if the speaker with the least number, other than the teacher, speaks first or not).

--------------------------------------------------------------------------------------------
### PipeFormat4WER

This program is useful for computing WER using the segments provided by **PLSPP**.   
It formats the transcription from PLSPP and the correction for the WER computation program (the format described [here](#WER)).   
It selects only the segments from the reference that are at least partially merged (timing-wise) with a segment from PLSPP.  

It takes 2 inputs (provided as arguments when executing it):
* The base name of the audio file that has been transcribed (without the `.wav` extension).
* An integer, `0` or `1`: if `0` is given, the program runs as is; if `1` is given, the order of the speakers returned by the function `is_speaker_order_normal()` is reversed.  

The program automatically creates 2 result files:
* `PLSPP_WER/PLSPP_WER_format/<name_of_the_file>_pipeRes.txt` for the transcription from PLSPP.
* `PLSPP_WER/Corr_WER_format/<name_of_the_file>_corRes.txt` for the correction.

To convert the transcription from PLSPP into the correct format, it uses the `.txt` output files of the pipeline (files containing only the text of each segment) placed in the *"PLSPP_WER/PLSPP_text/<name_of_the_file>/"* directory.  

To convert the correction into the correct format, it uses the file `PLSPP_WER/TimeInfo/timeInfo_sorted.csv`, which provides timing information for each segment, and the TextGrid file containing the correction.   

To ensure that both files have speakers in the same order (necessary for WER computation), it uses the function `is_speaker_order_normal()` to determine who speaks first according to the PLSPP transcription, then writes the correction file accordingly. 

The program concatenates all segments from the reference corresponding to the same segment from PLSPP into a single line to make it a single segment. 

--------------------------------------------------------------------------------------------
### TrueSegmentation

The segmentation of PLSPP and the segmentation from the reference are sometimes different. This can affect the WER, as words may be deleted or added incorrectly when compared.   

This program attempts to detect misplaced words in the reference segments (always at the end or beginning of these segment) and removes them according to the PLSPP segments to minimize the impact of segmentation errors on WER.  

It takes as input the name of the audio file we are working on (without the extension).  

It resegments the text in the file `PLSPP_WER/PLSPP_WER_format/<name_of_the_file>_pipeRes.txt` using the file `PLSPP_WER/Corr_WER_format/<name_of_the_file>_corRes.txt`.  

It stores the result in the file `PLSPP_WER/Corr_WER_format_segmented/<name_of_the_file>_corRes_segmented.txt` (creating it if it doesn't exist).  

The method is detailed in the internship's report.  

--------------------------------------------------------------------------------------------
### MFA_segmented_files

This program transforms all segments of corrected text (correctly segmented according to segments from PLSPP using [TrueSegmentation.py](#TrueSegmentation)) into individual files (one file per segment).  

Concretely, for every file it reads, it divides this file into smaller files with one file per line (as each line represents a segment). It also names each new file correctly depending on the speaker, the line number, and the recording.  

It requires no input and automatically reads all files stored in the directory *"PLSPP_WER/Corr_WER_format_segmented/"*.   

It creates these files in the directory *"PLSPP_Prosodic/Corpus_segmented/"*.

--------------------------------------------------------------------------------------------
### ProsodicData 

This program gathers and organizes all prosodic data contained in the `stressTable.csv` output from PLSPP, specifically the proportion of words pronounced correctly.  

It generates one data file per speaker as well as a final file containing total data for all tables.  

It takes one integer as an argument.   

* If `0` is given:  
  This collects data when PLSPP alone has been used.  
  The program reads data from the file `PLSPP_Prosodic/Tables/PLSPPstressTable.csv`.  
  Speaker files are written to the directory *"PLSPP_Prosodic/PLSPP_data/"* and generates the total file: `PLSPP_Prosodic/Total_data/PLSPP_total_data.csv`.  
  
* If `1` is given:  
  This collects data when PLSPP_MFA alone has been used.  
  The program reads data from the file `PLSPP_Prosodic/Tables/PLSPPMFAstressTable.csv`.  
  Speaker files are written to the directory *"PLSPP_Prosodic/PLSPP_MFA_data/"* and generates the total file: `PLSPP_Prosodic/Total_data/PLSPP_MFA_total_data.csv`.

* Otherwise:  
  This collects data when PLSPP_MFA has been used with text from the reference instead of using WhisperX.  
  The program reads data from the file `PLSPP_Prosodic/Tables/RefstressTable.csv`.  
  Speaker files are written to the directory *"PLSPP_Prosodic/Ref_data/"* and generates the total file: `PLSPP_Prosodic/Total_data/Ref_total_data.csv`.  

The speaker files are in this format (if there is no data for one line, it is not written):

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


The total data file is in this format:

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
