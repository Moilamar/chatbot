from corpus import readFile, processFile
from chatbot import ChatBot


file = readFile("corpus.txt")

processFile(file)

chatBot = ChatBot()

chatBot.readSentence("sup")
