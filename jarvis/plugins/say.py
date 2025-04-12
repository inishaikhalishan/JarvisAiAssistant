from os import system

def Say(text):
    system(f"flite -t \"{text}\"")