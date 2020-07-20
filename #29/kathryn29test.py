#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:40:20 2020

@author: kmi20042005
"""

from kathryn29 import encoder, decoder

print(encoder('eded'))
print(encoder('a'))
print(encoder("aaagggbdbgtssss"))

print(decoder('4a4b4c'))
print(decoder('1b0g0f0g'))
print(decoder('1a'))

print(decoder(encoder('aaabbbggg')))