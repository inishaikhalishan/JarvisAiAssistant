from os import system

def Say(text):
    system(f"espeak-ng -v hi \"{text}\"")