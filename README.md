# sendbutton

Simple Script to send timed attacks in die-staemme.de .

# Installation

You'll need Python 3.6+
> pip install -r requirements.txt

# Simple Start

> python .\sendbutton.py --time 2021-12-27T22:45:00.500

There are more optional arguments (with examples):
> --server de197

Which server should be pinged to determine timedelay between your PC and the server. Default "de197"
> --delay -10

Manual timedelay in ms if you have an consistent offset. Default "0"
> --type support

Needs to be set, if you want to send support instead of an attack. Default "attack"
