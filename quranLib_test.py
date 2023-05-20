#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from quranLib import *

def test_Radio():
    radio = Radio() 
    assert radio.fileName() == 'radio.m3u'

def test_Ayat_raises():    
    # good senario
    ayat = Ayat()     
    try :   
        ayat.Surah_start = 1
        ayat.Surah_end = 114
        ayat.Ayah_start = 1
        ayat.Ayah_end = 6
    except ValueError:
        pytest.fail("Unexpected MyError ..")



