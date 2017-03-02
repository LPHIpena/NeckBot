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
from discord.ext import commands

RECORD_FILE = 'record.txt'

# Setup discord api
description = ''' a bot made to track the total and
                  max time that nick has stayed in the call '''

#client = discord.Client()
bot = commands.Bot(command_prefix='!', description=descripion)

#initialize the timer to be used later
timer = None

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main API calls~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@client.event
async def on_voice_state_update(before, after):

    if (after.id == '191600966708101120'):

        if after.voice.voice_channel is None and timer is not None:
            timer.stop()

        elif after.voice.self_mute or after.voice.self_deaf \
                or after.voice.is_afk and timer is not None:
            pause_timer()

        else:
            start_timer()


# TODO: ADD BOT COMMANDS HERE
"""
@bot.event
async def max_time():
"""

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

class Stopwatch:

    def __init__(self):
        self._start_time = None
        self._stop_time = None
        self._pause_time = None

    def start(self):
        self._start_time = time.time()

    def pause(self):
        self._pause_time = time.time()

    def stop(self):
        self._stop_time = time.time()


    @property
    def time_elapsed(self):
        if not self._stop_time:
            return (time.time() - self._start_time)

    @property
    def total_run_time(self):
        return self._stop_time - self._start_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# client start
client.run('token')






















