from pynput.keyboard import Key, Controller
import time
import datetime
import pyautogui
import argparse
import random

parser = argparse.ArgumentParser(description='Python Script to press the send buttons in Tribalwars at a given time.')
parser.add_argument("--delay", default = 5)

args = parser.parse_args()



DELAY = datetime.timedelta(seconds=5)


def random_click_position(location):
    h = int(random.random() * location.height) 
    w = int(random.random() * location.width)
    loc={"x":location.left + w, "y" :  location.top  + h}
    return loc

def do_it(location):
    print("click ...")
    pyautogui.click(location["x"], location["y"])
    return

def find_button_on_screen(filename):
    # type ether "attack" or "support"
    location = pyautogui.locateOnScreen(filename, confidence = 0.9)
    return location

def get_coord_of_number(location):
    coord = {"x" : location.left - 25, "y" : location.top + 10}
    return coord
def get_coord_of_button(location):
    h = int(random.random() * location.height) 
    w = int(random.random() * location.width)
    coord={"x":location.left + w, "y" :  location.top  + h}
    return coord

def wait_and_reload(keyboard):
    time.sleep(args.delay)
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

def run():
    keyboard = Controller()
    while True:

        location = find_button_on_screen("praegen.PNG")
        if not location:
            print("cant find a button")
        else:
            coord = get_coord_of_number(location)
            pyautogui.click(coord["x"], coord["y"])
            time.sleep(0.5)
            coord = get_coord_of_button(location)
            pyautogui.click(coord["x"], coord["y"])
            print("Found!")


        wait_and_reload(keyboard)
    

run()