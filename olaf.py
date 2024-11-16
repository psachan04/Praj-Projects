import pyjokes
from myAI import AI

olaf = AI()

def jokes():
    funny = pyjokes.get_joke()
    print(funny)
    olaf.say(funny)

command = ""
while True and command != "goodbye":
    command = olaf.listen()
    print("commmand was:", command)

    if command == "tell me a joke":
        jokes()

olaf.say("Goodbye!")
