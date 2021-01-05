import aiml
import os

kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml c")

# if os.path.isfile("bot_brain.brn"):
#     kernel.bootstrap(brainFile = "bot_brain.brn")
# else:
    # kernel.bootstrap(learnFiles = "startup.xml", commands = "load aiml c")
    # kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
message = input("Human: ")
while message != "exit":
    print("Bot: " + kernel.respond(message))
    message = input("Human: ")