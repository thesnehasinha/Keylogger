from pynput.mouse import Controller
from pynput.keyboard import Controller

#(left to right, top to bottom)
#from top-left of the screen you can imagine the top-left to be (0,0)
def controlMouse():
    mouse = Controller()
    mouse.position = (100,200)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am freaking awesome!")

controlKeyboard()




