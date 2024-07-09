#script computing the prosodic data but from the gold corpus

cd ../plspp/
#segment the audio files
#./praat_barren scripts/intervalles2wavAndtimetable.praat ../data/ ../pyannote/ .TextGrid ../audio/ 3 0.01 8
#cd ../GETALP-internship/

#segment the text 
#python MFA_segmented_files.py 
#cp PLSPP_Prosodic/Corpus_segmented/* ../plspp/audio/

#cd ../plspp
rm benepar/* shape/* syll/* tg/* tgpos/* whisperx/*

#plspp 
#### SYLLABLE NUCLEI DETECTION
echo Syllable nuclei detection...
mkdir syll
./praat_barren scripts/SyllableNucleiv3_DeJongAll2021.praat ../audio/*.wav "Band pass (300..3300 Hz)" -25 2 0.3 "no" "English" 1.00 "TextGrid(s) only" "OverWriteData" "yes"
# arguments: list_of_input_files, option ("None", "Band pass (300..3300 Hz)", or "Reduce noise"), silence_threshold (dB), minimum_dip_near_peak (dB), minimum_pause_duration (s), filled_pause_detection ("yes" or "no"), language ("English" or "Dutch"), filled_pause_threshold, and some output options (cf. praat script)
mv audio/*.TextGrid syll/

#### MFA word & phoneme alignment
echo Word and phoneme alignment...
mkdir tgmfa
mfa align audio/ english_us_arpa english_us_arpa tgmfa/ --clean # Add --beam 20 or --beam 50 (or 100) if needed
mv audio/*.txt text/

#### SYLLABLE NUCLEI DETECTION
echo Syllable nuclei detection...
mkdir syll
./praat_barren scripts/SyllableNucleiv3_DeJongAll2021.praat ../audio/*.wav "Band pass (300..3300 Hz)" -25 2 0.3 "no" "English" 1.00 "TextGrid(s) only" "OverWriteData" "yes"
# arguments: list_of_input_files, option ("None", "Band pass (300..3300 Hz)", or "Reduce noise"), silence_threshold (dB), minimum_dip_near_peak (dB), minimum_pause_duration (s), filled_pause_detection ("yes" or "no"), language ("English" or "Dutch"), filled_pause_threshold, and some output options (cf. praat script)
mv audio/*.TextGrid syll/

echo Merging transcription, MFA alignement and syllable files...
mkdir tg
./praat_barren scripts/Merge_tiers_of_different_TextGrids.praat ../tgmfa/ ../syll/ '1-1,words/1-2,phones/2-1,Nuclei' ../tg/
# arguments: input_folderA, input_folderB, target tiers, output_folder

#### SYNTACTIC ANALYSIS WITH SPACY
echo Syntactic analysis...
mkdir tgpos
python scripts/spacyTextgrid_v2.py tg/ tgpos/ 'en_core_web_md' 'words'
# arguments: input_folder, output_folder, model_name, words_tier_name

#### LEXICAL STRESS ANALYSIS
echo Lexical stress pattern analysis...
mkdir shape
python scripts/syllcheck_mfa.py tgpos/ audio/ shape/ CMU/cmudict-0.7b
# arguments: textgrid_folder, audio_folder, output_folder, path_to_CMU_dictionary

#### PAUSE ANALYSIS
# echo Pause pattern analysis...
# mkdir benepar
# # Make constituency analysis from text files with Berkeley Neural Parser
# python scripts/text2benepar.py text/ benepar/ 'benepar_en3' 'en_core_web_md'
# # arguments: input_folder, output_folder, benepar_model_name, spacy_model_name
# # Run pause analysis
# python scripts/pausecheck.py shape/ benepar/


echo Done!