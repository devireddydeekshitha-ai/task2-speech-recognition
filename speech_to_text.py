from pydub import AudioSegment
import speech_recognition as sr
import os

audio_path = r"C:\Users\D.DEEKSHITHA REDDY\task2_text_summarization\sample_audio.wav"

if not os.path.exists(audio_path):
    print("Audio file not found!")
    exit()

# Load audio
audio = AudioSegment.from_file(audio_path)

# Convert to wav (safe format)
wav_path = "converted.wav"
audio.export(wav_path, format="wav")

# Speech to text
recognizer = sr.Recognizer()

with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("Transcribed Text:")
    print(text)
except Exception as e:
    print("Error:", e)
    from pydub import AudioSegment
import speech_recognition as sr
import os

audio_path = r"C:\Users\D.DEEKSHITHA REDDY\task2_text_summarization\sample_audio.wav"

if not os.path.exists(audio_path):
    print("Audio file not found!")
    exit()

# Load audio
audio = AudioSegment.from_file(audio_path)

# Convert to wav (safe format)
wav_path = "converted.wav"
audio.export(wav_path, format="wav")

# Speech to text
recognizer = sr.Recognizer()

with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)

    print("Transcribed Text:")
    print(text)

    # Save output to file
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("Transcribed Text:\n")
        file.write(text)

    print("\nOutput saved to output.txt")

except Exception as e:
    print("Error:", e)  

  
   