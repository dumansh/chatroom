import asyncio
from websockets.sync.client import connect
import threading
websocket=connect("ws://localhost:8765")
username=input("Choose an username: ")

def sendmessage():

    done = False
    print("\nEnter message to chat and reply")
    print("Enter !quit to quit the chat room\n")
    while not done:
        msg=input("\r")
        if msg=="!quit":
            done=True
        else:
            websocket.send(f"{username}: {msg}")
    print("Bye")
    websocket.close()

def receivemessage():
    done=False
    while True:
        try:
            message = websocket.recv()
            print(f"\033[1F\033[K{message}")

        except:
            break


sendthread=threading.Thread(target=sendmessage)
receivethread=threading.Thread(target=receivemessage)

sendthread.start()
receivethread.start()

