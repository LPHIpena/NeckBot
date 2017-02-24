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
description = ''' a bot made to track the total and
                  max time that nick has stayed in the call '''

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

    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._stop_time = time.time()

   @property
    def time_elapsed(self):
        assert not self._stop_time, \
        return time.time() - self._start_time

    @property
    def total_run_time(self):
        return self._stop_time - self._start_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()
        if type:
            raise type, value, traceback

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# client start
client.run('token')






















