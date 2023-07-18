import speech_recognition as sr
# check version
sr.__version__
r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
