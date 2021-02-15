import os
import aiml
from autocorrect import spell

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    #caricamento del file 
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LOAD AIML")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


while True:
    #inserimento del messaggio
    message = input("\t\t\Insert your message: ")
    #risposta del bot
    bot_response = k.respond(message)
    if message == "quit":
        exit()
    if message == "save":
        k.saveBrain("brain.dump")
    if bot_response:
        print("\t\t\Sara: ", bot_response)
    else:
        #caso in cui il bot non ha una risposta alla domanda, 
        #risposta standard
        print("\t\t\Sara: Sorry, I have an answer! Try again :) !")
    
        
