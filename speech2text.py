import speech_recognition as sr
Audio_file = ("Recording.wav")

r = sr.Recognizer()  #Initialize the recognizer

with sr.AudioFile(Audio_file) as source:    #Reads the audio file
    audio = r.record(source)

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recogntion cant understand audio")
except sr.RequestError:
    print("Couldnt get results from google")    