#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any
import arabic_reshaper
from bidi.algorithm import get_display
import csv
import json
import requests
import pandas as pd
import os
import pytest

import warnings
warnings.filterwarnings("ignore")

'''
help links
https://docs.globalquran.com/#/operations/get-quran-ayah
https://alquran.cloud/
https://alquran.cloud/cdn
https://globalquran.com/download/
https://github.com/GlobalQuran/site/archive/v3.4.0.zip
https://cdn.islamic.network/quran/audio/128/ar.alafasy/2826.mp3
'''

print(''' 
**** Repeate Quran V0.1.0 ****
هذا البرنامج لاختيار أيات متتالية او سور محددة للتلاوة  لمختلف القراء 
و يقدمها لك كقائمة تشغيل يمكن تشغيلها على جهازك 
تطلب انترنت لتعمل 

البرنامج قيد التجريب
ننصح بإستخدام برنامج VLC
فضلا انتظر للتحميل
This program to play certain Ayat or Souar continously
with diffrent readers 
we recommend to use VLC player 
Please wait for loading...
'''
)

log_file = open('log.log', 'a')

def arabic_fix(text) -> str:
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

class Radio:
    def __init__(self) -> None:
        log_file.write('\nRadio start')
        radio_url = "https://mp3quran.net/api/v3/radios"
        # Send GET request to the URL
        response = requests.get(radio_url)
        # Raise exception if the request failed
        response.raise_for_status()
        # Parse the response as JSON
        data = response.json()
        #print(json.dumps(data,indent = 4))
        radio_file = open('radio.m3u', 'wb')
        radio_file.write("#EXTM3U\n".encode('utf-8'))
        for radio in data['radios']:
            radio_file.write(('#EXTINF:0,'+radio['name']+'\n').encode('utf-8'))
            radio_file.write('#EXTVLCOPT:network-caching=1000\n'.encode('utf-8'))
            radio_file.write((radio['url']+'\n').encode('utf-8'))
        radio_file.close()
        log_file.write('\nRadio generated')

        
    def fileName(self) -> str:
        log_file.write('\nRadio sent')
        return 'radio.m3u'
    
class Ayat:
    Surah_start=1
    Surah_end=114
    Ayah_start=1
    Ayah_end=6
    def __init__(self, Surah_start=Surah_start, Surah_end=Surah_end, Ayah_start=Ayah_start, Ayah_end=Ayah_end) -> None:
        self.Surah_start = Surah_start
        self.Surah_end = Surah_end
        self.Ayah_start = Ayah_start
        self.Ayah_end = Ayah_end
        log_file.write('\nSurah start '+ str(self.Surah_start) +' - '+ str(self.Surah_end) +' - '+ str(self.Ayah_start) +' - '+ str(self.Ayah_end) )
        

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "Surah_start":
            if isinstance(value, int) and value > 0 and value <= 114:
                self.__dict__[name] = value
            else:
                raise ValueError("Surah_start must be a non-negative integer between 1&114")
        elif name == "Surah_end":
            if isinstance(value, int) and value >= self.Surah_start  and value <= 114:
                self.__dict__[name] = value
            else:
                raise ValueError("Surah_end must be a non-negative integerand greater than Surah_start and between 1&114")
        elif name == "Ayah_start":
            if isinstance(value, int) and value > 0 and value <= surah_ayah_count[self.Surah_start]:
                self.__dict__[name] = value
            else:
                raise ValueError("Ayah_start must be a non-negative integerand")
        elif name == "Ayah_end":
            if self.Surah_end == self.Surah_start:                    
                if ( isinstance(value, int) and 
                     (value > self.Ayah_start) and 
                     (value > 0) and 
                     (value <= surah_ayah_count[self.Surah_start])
                     ):
                    self.__dict__[name] = value
                else:
                    raise ValueError("Ayah_end must be a non-negative integerand greater than Surah_start")
            else:                    
                if ( isinstance(value, int) and
                     (value <= surah_ayah_count[self.Surah_start]) and
                     (value > 0) and 
                     (value > self.Ayah_start) 
                     ):
                    self.__dict__[name] = value
                else:
                    raise ValueError("Ayah_end must be a non-negative integerand greater than Surah_start")

        log_file.write('\nset '+ str(name) +' - '+ str(value) )

            




# Global variables
surah_ayah_count = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75, 9: 129, 10: 109,
    11: 123, 12: 111, 13: 43, 14: 52, 15: 99, 16: 128, 17: 111, 18: 110, 19: 98,
    20: 135, 21: 112, 22: 78, 23: 118, 24: 64, 25: 77, 26: 227, 27: 93, 28: 88,
    29: 69, 30: 60, 31: 34, 32: 30, 33: 73, 34: 54, 35: 45, 36: 83, 37: 182, 38: 88,
    39: 75, 40: 85, 41: 54, 42: 53, 43: 89, 44: 59, 45: 37, 46: 35, 47: 38, 48: 29,
    49: 18, 50: 45, 51: 60, 52: 49, 53: 62, 54: 55, 55: 78, 56: 96, 57: 29, 58: 22,
    59: 24, 60: 13, 61: 14, 62: 11, 63: 11, 64: 18, 65: 12, 66: 12, 67: 30, 68: 52,
    69: 52, 70: 44, 71: 28, 72: 28, 73: 20, 74: 56, 75: 40, 76: 31, 77: 50, 78: 40,
    79: 46, 80: 42, 81: 29, 82: 19, 83: 36, 84: 25, 85: 22, 86: 17, 87: 19, 88: 26,
    89: 30, 90: 20, 91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19, 97: 5, 98: 8,
    99: 8, 100: 11, 101: 11, 102: 8, 103: 3, 104: 9, 105: 5, 106: 4, 107: 7, 108: 3,
    109: 6, 110: 3, 111: 5, 112: 4, 113: 5, 114: 6,
}

#TODO: to be replaced by json 
Quraa2 = [
            ["ar.ahmedajamy",128],
            ["ar.alafasy",128],
            ["ar.hudhaify",128],
            ["ar.husary",128],
            ["ar.husarymujawwad",128],
            ["ar.mahermuaiqly",128],
            ["ar.minshawi",128],
            ["ar.muhammadayyoub",128],
            ["ar.muhammadjibreel",128],
            ["ar.shaatree",128],
            ["ar.abdulbasitmurattal",192],
            ["ar.abdullahbasfar",192],
            ["ar.abdurrahmaansudais",192],
            ["ar.hanirifai",192],
            ["ar.abdullahbasfar",32],
            ["ar.hudhaify",32],
            ["ar.ibrahimakhbar",32],
            ["ar.abdulsamad",64],
            ["ar.aymanswoaid",64],
            ["ar.minshawimujawwad",64],
            ["ar.saoodshuraym",64],
          ] 
 #numbers
debug = 0 
 #string
 #DataFrame
df = pd.read_csv('Quran_aya_index.csv')


# if __name__ == '__main__' checks if a file is imported as a module or not.
def main():
    while True:
        choice = input("send [A] for ayat  \nsend [S] for complete suar\n")
        print(choice)
        if choice.lower() == 'a':
            Ayat_program()
        elif choice.lower() == 's':
            Surah_program()       
        print('\n\n\tAllah bless the coder\n\n')
 


    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    #main()

    radio = Radio()
    ayat = Ayat()

    ayat.Ayah_end=5





