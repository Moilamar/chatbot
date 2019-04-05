import random


class ChatBot:
    GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "hey"]
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello"]

    def __init__(self):
        pass

    def readSentence(self, sentence: str):
        for word in sentence.split():
            if word.lower() in self.GREETING_INPUTS:
                self.__say(random.choice(self.GREETING_RESPONSES))

    def __say(self, sentence: str):
        print("ChatBot: " + sentence)
