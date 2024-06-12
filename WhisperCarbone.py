#calcule la consommation en carbone de whisper
import whisper
from codecarbon import EmissionsTracker

#on charge le modele
model = whisper.load_model(input("Model:\n"))

#tracking de la consommation
tracker = EmissionsTracker()
tracker.start()
#lancement de whisper (changer le nom du fichier si besoin)
result = model.transcribe("../Audios/dec2022-003_005-025.wav")
#fin du tracking
tracker.stop()

print(result["text"])

