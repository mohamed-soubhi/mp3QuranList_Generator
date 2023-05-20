#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from quranLib import *

def test_Radio():
    radio = Radio() 
    assert radio.fileName() == 'radio.m3u'

def test_Ayat_no_raises():    
    # good senario
    ayat = Ayat(1,114,1,6)     
    
    assert ayat.Surah_start == 1
    assert ayat.Surah_end == 114
    assert ayat.Ayah_start == 1
    assert ayat.Ayah_end == 6

def test_Ayat_Surah_start_raises(): 
    ayat = Ayat()
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 0
    assert str(exp.value) == "Surah_start must be a non-negative integer between 1&114"
    
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 1000
    assert str(exp.value) == "Surah_start must be a non-negative integer between 1&114"

def test_Ayat_Surah_end_raises(): 
    ayat = Ayat()   
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 0
    assert str(exp.value) == "Surah_end must be a non-negative integerand greater than Surah_start and between 1&114" 

    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 120
    assert str(exp.value) == "Surah_end must be a non-negative integerand greater than Surah_start and between 1&114"

def test_Ayat_Ayah_start_raises(): 
    ayat = Ayat()   
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 20
        ayat.Ayah_start = 0
    assert str(exp.value) == "Ayah_start must be a non-negative integerand" 

    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 20
        ayat.Ayah_start = 136
    assert str(exp.value) == "Ayah_start must be a non-negative integerand" 

  

def test_Ayat_Ayah_end_raises(): 
    ayat = Ayat()   
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 20
        ayat.Ayah_start = 100
        ayat.Ayah_end = 0 # <-- the error 
    assert str(exp.value) == "Ayah_end must be a non-negative integerand greater than Surah_start" 

    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 20
        ayat.Ayah_start = 100        
        ayat.Ayah_end = 136 # <-- the error 
    assert str(exp.value) == "Ayah_end must be a non-negative integerand greater than Surah_start" 
  
    with pytest.raises(ValueError) as exp:
        ayat.Surah_start = 5
        ayat.Surah_end = 5
        ayat.Ayah_start = 111        
        ayat.Ayah_end = 100 # <-- the error 
    assert str(exp.value) == "Ayah_end must be a non-negative integerand greater than Surah_start" 

  
