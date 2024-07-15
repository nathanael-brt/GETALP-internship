#Computes the carbon emissions produced by whisper in function on a chosen whisper model.
#Need the cordecarbon package to be installed to work
#---
#Returns a .csv with plenty of informations on not only the carbon emissions but also the power consumption, the cpu, gpu, etc...
#----------------------------------------------------------------------------------------------------------------------

import whisper
from codecarbon import EmissionsTracker

#we charge the model
model = whisper.load_model(input("Model:\n"))

#tracking of the consumption
file = input("Audio file:")     #ask the audio file to transcribe

tracker = EmissionsTracker()
tracker.start()
#starts whisper 
result = model.transcribe(file, language='en')
#end of tracking
tracker.stop()

print(result["text"])

