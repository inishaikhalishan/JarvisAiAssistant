from jarvis.plugins.mic import Mic
from jarvis.plugins.recognize import recognize
from jarvis.plugins.say import Say


while True:
    audio = Mic()
    answer = recognize(audio)
    Say(answer)
    