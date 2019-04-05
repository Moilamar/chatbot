# imports
import os
import nltk
import numpy as np
import random
import string

# File for testing stuff

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
__lemmer = nltk.stem.WordNetLemmatizer()

def readFile(fileName: str):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets/' + fileName)
    f = open(file, 'r', errors = 'ignore')

    raw = f.read()

    raw = raw.lower().translate(remove_punct_dict)

    print('File ' + fileName + ' loaded')

    return raw

def processFile(file: str):
    sent_tokens = nltk.sent_tokenize(file)
    word_tokens = nltk.word_tokenize(file)

    __lemTokens(word_tokens)

def __lemTokens(tokens: list):
    return [__lemmer.lemmatize(token) for token in tokens]
