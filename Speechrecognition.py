# pip install speechrecognition
import speech_recognition as sr
r = sr.Recognizer()

#    supported formats: WAV, AIFF, AIFF-C, FLAC
file = sr.AudioFile('D:/bol.wav')
with file as source:
      r.adjust_for_ambient_noise(source)
      audio = r.record(source)
      result = r.recognize_google(audio,language='eng')
print(result)

