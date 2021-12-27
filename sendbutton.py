'''
Version 0.1.0
Arguments: 
"--time" 
    example: 2021-12-27T22:45:00.500
"--server" 
    optional
    example: de197
"--type"
    example: attack   or   support
'''

import pyautogui
import dateutil.parser
import datetime
import ntplib
import time
import os
import argparse
from tcp_latency import measure_latency


parser = argparse.ArgumentParser(description='Python Script to press the send buttons in Tribalwars at a given time.')
parser.add_argument("--time")
parser.add_argument("--server", default = "de197")
parser.add_argument("--type", default = "attack")

args = parser.parse_args()

#domain = "de197.die-staemme.de"
domain = args.server + ".die-staemme.de"
#departure_time = "2021-12-27T22:45:00.500"
departure = dateutil.parser.parse(args.time)

print("Sending date: {0}".format(departure))

def get_local_offset():
    try:
        client = ntplib.NTPClient()
        response = client.request("de.pool.ntp.org", version=3)
        return datetime.timedelta(seconds=response.offset)
    except:
        return datetime.timedelta(seconds=0.0)

def get_ping(domain):
    pingList = measure_latency(host=domain, runs=3, timeout=0.2)
    if not list(filter(None, pingList)):
        pingList = measure_latency(host=domain, runs=5, timeout=1)
    avgPing = sum(filter(None, pingList)) / len(list(filter(None, pingList)))
    return datetime.timedelta(microseconds=avgPing * 1000)

def wait_to_send():
    offset = get_local_offset()
    print("Time Offset: {0} ms".format(round(offset.total_seconds() * 1000)))
    ping = get_ping(domain)
    print("Ping for {0}: {1} ms".format(domain, ping.total_seconds() * 1000))
    print("Waiting")
    real_departure = departure - offset - ping

    while real_departure - datetime.datetime.now() > datetime.timedelta(seconds=5):
        time_left = real_departure - datetime.datetime.now() - datetime.timedelta(
                        seconds=5)
        if time_left.total_seconds() <= 0:
            break
        time.sleep((time_left / 2).total_seconds())
    print("Five second left.. searching for button")

    location = find_button_on_screen()
    if not location:
        print("cant find a button")
        return

    while real_departure - datetime.datetime.now() > datetime.timedelta(milliseconds=1):
        time_left = real_departure - datetime.datetime.now()
        if time_left.total_seconds() <= 0:
            break
        time.sleep((time_left / 2).total_seconds())
    do_it(location)

def do_it(location):
    print("click ...")
    pyautogui.click(location)
    return


def find_button_on_screen():
    # type ether "attack" or "support"
    location = pyautogui.locateCenterOnScreen(args.type + ".PNG", confidence = 0.9)
    if not location:
        # when starting the attack from the map, the button looks different
        location = pyautogui.locateCenterOnScreen(args.type + "_map.PNG")
    return location


if departure < datetime.datetime.now():
    print("Time is in the past.")
else:
    wait_to_send()