from guessing_game import recognize_speech_from_mic
import speech_recognition as sr
# check version
sr.__version__
r = sr.Recognizer()
short_file = 'demo-voice.wav'
large_file = 'demo-voice-large.wav'
def translate_all_file(filename):
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source)

    type(audio)
    #transcript the audio
    return r.recognize_google(audio)

def translate_part_of_file(filename, offset, duration):
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source, offset=offset, duration=duration)

    return r.recognize_google(audio)

def get_audio_from_mic():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("say something short")
    return recognize_speech_from_mic(r, m)  # speak after running this line
    #{'success': True, 'error': None, 'transcription': 'hello'}

##invoque
print(translate_all_file(short_file))
print(translate_part_of_file(large_file, 0, 3))
print(translate_part_of_file(large_file, 10, 10))
audio = get_audio_from_mic()
print("You said: ", audio['transcription'])
