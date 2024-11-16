import pyttsx3
import speech_recognition as sr

class AI:
    def __init__(self, name=None):
        # Private attributes
        self.__name = name if name is not None else ""
        self.__skill = []
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Initialize speech recognition
        self.rec = sr.Recognizer()
        self.m = sr.Microphone()
        
        # Adjust microphone for ambient noise
        print("Listening")
        with self.m as source:
            self.rec.adjust_for_ambient_noise(source)

    @property
    def name(self):
        #Getter for the AI's name
        return self.__name

    @name.setter
    def name(self, value):
        #Setter for the AI's name
        sentence = f"Hello, my name is {self.__name}"
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        #Method to make the AI speak a sentence
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        #Method to listen for and process speech input
        print("Say something")
        with self.m as source:
            audio = self.rec.listen(source)
        
        print("Got it")
        
        try:
            phrase = self.rec.recognize_google(audio, show_all=False, language="en_US")
            sentence = "Got it, you said:" + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
            print("You said:" + phrase)
            return phrase
            
        except Exception as error:
            print("Sorry, didn't catch that", str(error))
            self.engine.say("Sorry, didn't catch that")
            self.engine.runAndWait()
            return phrase