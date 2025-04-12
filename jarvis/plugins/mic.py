import speech_recognition

reconize = speech_recognition.Recognizer()

def Mic():
    with speech_recognition.Microphone() as mic:
        print("Boliye sun rha hoon...")
        reconize.adjust_for_ambient_noise(mic)
        audio = reconize.listen(mic)
    return audio