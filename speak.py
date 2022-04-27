#!/usr/bin/python3

import os
import datetime
import random
hour = int(datetime.datetime.now().hour)

recs_path = '/home/pi/git/bark_translator/recs/'
speak_command = 'echo failed'

speak_root = 'aplay /home/pi/git/bark_translator/recs/'

"""
rec_list = os.listdir('/home/pi/git/bark_translator/recs/petco')
speak_command = speak_root+'petco/'+random.choice(rec_list)
"""

if hour in range(7, 9):
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/pee')
    speak_command = speak_root+'pee/'+random.choice(rec_list)

elif hour in range(12, 16):
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/hungry')
    speak_command = speak_root+'hungry/'+random.choice(rec_list)

elif hour in range(18, 20):
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/hungry')
    speak_command = speak_root+'hungry/'+random.choice(rec_list)

elif hour >= 22:
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/bed')
    speak_command = speak_root+'bed/'+random.choice(rec_list)

elif hour in range(9, 17):
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/garage')
    speak_command = speak_root+'garage/'+random.choice(rec_list)

else:
    rec_list = os.listdir('/home/pi/git/bark_translator/recs/alert')
    speak_command = speak_root+'alert/'+random.choice(rec_list)
# 7-9 pee
# 12-16 hungry
# 9-17 garage/left
# 24hrs alert
# 18-20 hungry
# > 22 bed

os.system(speak_command)
