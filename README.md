# Simple ChatBot

## Setting up the environment (for Ubuntu 18.04)
Checkout the repository
```
git clone https://github.com/Moilamar/chatbot.git chatbot
```
Python 3.6
```
sudo apt-get update
sudo apt-get install python3.6
```
Pip
```
sudo apt-get install -y python3-pip
```
Essentials
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo pip3 install -U nltk
sudo pip3 install -U numpy
sudo pip3 install -U scikit-learn
```
## Build virtual environment
Create environment
```
python3 -m venv chatbot
```
Run environment
```
cd chatbot
source bin/activate
```
Install dependencies (first time only)
```
python3 install.py
```
## Running application
Run test script manually
```
python3 src/index.py
```
