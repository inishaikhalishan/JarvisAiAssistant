import speech_recognition
from jarvis.plugins.mic import reconize


def recognize(audio):
    # try:
    #     text = reconize.recognize_google(audio, language="hi-IN")
    # except Exception as e:
    #     return "Alishan, Maaf Kijiye samjha nhi.{e}"
    text = reconize.recognize_google(audio, language="hi-IN")
    return text