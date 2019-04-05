from corpus import readFile, processFile
from chatbot import ChatBot

# Testing
# file = readFile("corpus.txt")
# processFile(file)

chatBot = ChatBot()

while (True):
    userInput = input('You: ')

    chatBot.readSentence(userInput)

    print()
