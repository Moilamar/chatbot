import os
import random
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from corpus import readFile, processFile


class ChatBot:
    GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "hey"]
    GREETING_RESPONSES = ["hi", "hey", "hello"]

    def __init__(self):
        self.name = "ChatBot"
        self.removePunctDict = dict((ord(punct), None) for punct in string.punctuation)
        self.lemmer = nltk.stem.WordNetLemmatizer()
        self.tfidfVec = TfidfVectorizer(tokenizer = self.lemNormalize, stop_words = 'english')
        self.readCorpus('corpus.txt')

        self.afterInit()

    def afterInit(self):
        self.say('Hello, I am a ChatBot.')

    def readCorpus(self, fileName: str):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/' + fileName)
        f = open(file, 'r', errors = 'ignore')

        raw = f.read().lower().translate(self.removePunctDict)

        self.sentTokens = nltk.sent_tokenize(raw)
        self.wordTokens = nltk.word_tokenize(raw)

    def readSentence(self, sentence: str):
        if self.checkForGreeting(sentence):
            self.say(random.choice(self.GREETING_RESPONSES))

        else:
            self.sentTokens.append(sentence)

            tfidf = self.tfidfVec.fit_transform(self.sentTokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]

            if (req_tfidf == 0):
                self.say("I am sorry.")

    def checkForGreeting(self, sentence: str):
        for word in sentence.split():
            if word.lower() in self.GREETING_INPUTS:
                return True

    def say(self, text: str):
        print(self.name + ": " + text)

    def lemNormalize(self, text):
        return self.lemTokens(nltk.word_tokenize(text.lower().translate(self.removePunctDict)))

    def lemTokens(self, tokens: list):
        return [self.lemmer.lemmatize(token) for token in tokens]
