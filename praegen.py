'''
Version 0.1.0
Arguments: 
"--delay" 
    in seconds
    example: 120 (default 60)
"--delay_range" 
    smaler than 1.0; range in which delay is randomised 
    example: 0.3 (default 0.2)

'''

from pynput.keyboard import Key, Controller
import time
import pyautogui
import argparse
import random

parser = argparse.ArgumentParser(description='Python Script, welches den Prägen-Button im Adelshof periodisch drückt.')
parser.add_argument("--delay", default = "60")
parser.add_argument("--delay_range", default = "0.2")
parser.add_argument("--delay_after_reload", default = "2")
parser.add_argument("--add_button", default = "5")


args = parser.parse_args()

delay_range = float(args.delay_range)
delay = int(args.delay)
delay_after_reload = int(args.delay_after_reload)

def print_info():
    print('Python Script, welches den Prägen-Button im Adelshof periodisch drückt.')
    print('Arguments:\n"--delay"\nin seconds\nexample: "--delay 120" (default 60)\n"--delay_range"\nsmaler than 1.0; range in which delay is randomised\nexample: "--delay_range 0.3" (default 0.2)\n"--delay_after_reload"\nexample: "--delay_after_reload 5"\n"--add_button"\nexample: "--add_button 5"\n\n')
    print("Stopp by pressing Ctrl + C")
    print('===========================\n\n')


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
    location = pyautogui.locateOnScreen(filename, confidence = 0.9)
    return location

def get_coord_of_button(location):
    h = int(random.random() * location.height) 
    w = int(random.random() * location.width)
    coord={"x":location.left + w, "y" :  location.top  + h}
    return coord

def wait_and_reload(keyboard):
    print("Waiting for refresh.")
    time.sleep(random_delay(delay))
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(random_delay(delay_after_reload))

def random_delay(base_delay):
    r = random.random()
    signed = 1 if random.random() > 0.5 else -1
    return base_delay + (base_delay * r * delay_range * signed)

def press_extra_script_button(keyboard):
    print("press " + args.add_button)
    keyboard.press(args.add_button)
    keyboard.release(args.add_button)
    time.sleep(random_delay(1))

def run():
    keyboard = Controller()
    while True:

        press_extra_script_button(keyboard)

        location = find_button_on_screen("praegen.PNG")
        if not location:
            print("cant find a button")
        else:
            print("Found!")
            coord = get_coord_of_button(location)
            pyautogui.click(coord["x"], coord["y"])

        wait_and_reload(keyboard)
    
print_info()
run()