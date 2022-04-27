#!/usr/bin/python3

import os

while True:
    os.system('python3 /home/pi/git/bark_translator/listen.py record -t 30 -d 0')
    os.system('python3 /home/pi/git/bark_translator/speak.py')
