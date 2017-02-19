#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/usr/bin/env python                         ~
# -*- coding: utf-8 -*-                       ~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author: Louis Pena                          ~
#                                             ~
# Date: 2/18/2017                             ~
#                                             ~
# Description:                                ~
#    Discord bot that records how long Nick   ~
#    manages to stay in the call              ~
#                                             ~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                             ~
#                                             ~
#                NICKS BOT                    ~
#                                             ~
#                ( ͡☉ ͜ʖ ͡☉)                     ~
#                                             ~
#                                             ~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Includes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import asyncio
import discord
import time

from threading import Timer, Thread, Event

RECORD_FILE = 'record.txt'

# Setup discord api
description = ''' a bot made a for an autistic little shit '''

client = discord.Client()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main API calls~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@client.event
async def on_voice_state_update(before, after):

    if (after.id == '191600966708101120'):

        if after.voice.voice_channel is None:
            end_timer()

        elif after.voice.self_mute or after.voice.self_deaf or after.voice.is_afk:
            pause_timer()

        else:
            start_timer()


#TODO: all this stuff...
def start_timer():
    #start = time.time()
def end_timer():

def get_record():
    rec = open(RECORD_FILE, "r")
    record = readline()
    rec.close()
    return record

def update_record(new_record):
    rec = open(RECORD_FILE, "w")
    rec.write(new_record)
    rec.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Stopwatch(Thread):

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# client start
client.run('token')






















