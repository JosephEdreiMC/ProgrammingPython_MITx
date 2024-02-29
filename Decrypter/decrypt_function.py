# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:09:06 2023

@author: j_edr
"""
from ps6 import *

def decrypt_story():
    story_encrypted=get_story_string()
    intermediate=CiphertextMessage(story_encrypted)
    return intermediate.decrypt_message()

