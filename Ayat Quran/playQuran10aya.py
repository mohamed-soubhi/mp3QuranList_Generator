#!/usr/bin/env python3

import pandas as pd
import pygame
import requests
import os
import random

debug = 0
playcount =1

Quraa2Name=0
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

Surah_ayah_max = [
                    [ 1 , 7 ],
                    [ 2 , 286 ],
                    [ 3 , 200 ],
                    [ 4 , 176 ],
                    [ 5 , 120 ],
                    [ 6 , 165 ],
                    [ 7 , 206 ],
                    [ 8 , 75 ],
                    [ 9 , 129 ],
                    [ 10 , 109 ],
                    [ 11 , 123 ],
                    [ 12 , 111 ],
                    [ 13 , 43 ],
                    [ 14 , 52 ],
                    [ 15 , 99 ],
                    [ 16 , 128 ],
                    [ 17 , 111 ],
                    [ 18 , 110 ],
                    [ 19 , 98 ],
                    [ 20 , 135 ],
                    [ 21 , 112 ],
                    [ 22 , 78 ],
                    [ 23 , 118 ],
                    [ 24 , 64 ],
                    [ 25 , 77 ],
                    [ 26 , 227 ],
                    [ 27 , 93 ],
                    [ 28 , 88 ],
                    [ 29 , 69 ],
                    [ 30 , 60 ],
                    [ 31 , 34 ],
                    [ 32 , 30 ],
                    [ 33 , 73 ],
                    [ 34 , 54 ],
                    [ 35 , 45 ],
                    [ 36 , 83 ],
                    [ 37 , 182 ],
                    [ 38 , 88 ],
                    [ 39 , 75 ],
                    [ 40 , 85 ],
                    [ 41 , 54 ],
                    [ 42 , 53 ],
                    [ 43 , 89 ],
                    [ 44 , 59 ],
                    [ 45 , 37 ],
                    [ 46 , 35 ],
                    [ 47 , 38 ],
                    [ 48 , 29 ],
                    [ 49 , 18 ],
                    [ 50 , 45 ],
                    [ 51 , 60 ],
                    [ 52 , 49 ],
                    [ 53 , 62 ],
                    [ 54 , 55 ],
                    [ 55 , 78 ],
                    [ 56 , 96 ],
                    [ 57 , 29 ],
                    [ 58 , 22 ],
                    [ 59 , 24 ],
                    [ 60 , 13 ],
                    [ 61 , 14 ],
                    [ 62 , 11 ],
                    [ 63 , 11 ],
                    [ 64 , 18 ],
                    [ 65 , 12 ],
                    [ 66 , 12 ],
                    [ 67 , 30 ],
                    [ 68 , 52 ],
                    [ 69 , 52 ],
                    [ 70 , 44 ],
                    [ 71 , 28 ],
                    [ 72 , 28 ],
                    [ 73 , 20 ],
                    [ 74 , 56 ],
                    [ 75 , 40 ],
                    [ 76 , 31 ],
                    [ 77 , 50 ],
                    [ 78 , 40 ],
                    [ 79 , 46 ],
                    [ 80 , 42 ],
                    [ 81 , 29 ],
                    [ 82 , 19 ],
                    [ 83 , 36 ],
                    [ 84 , 25 ],
                    [ 85 , 22 ],
                    [ 86 , 17 ],
                    [ 87 , 19 ],
                    [ 88 , 26 ],
                    [ 89 , 30 ],
                    [ 90 , 20 ],
                    [ 91 , 15 ],
                    [ 92 , 21 ],
                    [ 93 , 11 ],
                    [ 94 , 8 ],
                    [ 95 , 8 ],
                    [ 96 , 19 ],
                    [ 97 , 5 ],
                    [ 98 , 8 ],
                    [ 99 , 8 ],
                    [ 100 , 11 ],
                    [ 101 , 11 ],
                    [ 102 , 8 ],
                    [ 103 , 3 ],
                    [ 104 , 9 ],
                    [ 105 , 5 ],
                    [ 106 , 4 ],
                    [ 107 , 7 ],
                    [ 108 , 3 ],
                    [ 109 , 6 ],
                    [ 110 , 3 ],
                    [ 111 , 5 ],
                    [ 112 , 4 ],
                    [ 113 , 5 ],
                    [ 114 , 6 ],
                ]


def aya_index(Surah,aya):
    aya_index = df[(df['Surah_Number']==Surah)&
                  (df['Ayah_Number']==aya)]
    if debug == 1 :
        print_row(aya_index)
        
    return list(aya_index.Ayah_index.astype(int))[0] 

def Surah_aya(aya_index):
    Surah = list(df[(df['Ayah_index']==aya_index)]['Surah_Number'].astype(int))[0]
    Aya = list(df[(df['Ayah_index']==aya_index)]['Ayah_Number'].astype(int))[0]
    return [Surah,Aya]

def print_row(df_line):
    for column in df_line.columns:
        print(column, '\t\t' ,df_line[column].values[0])
    print()

def play_sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def sound(Quraa2Name, AyaIndex):    
    aya_path = os.getcwd()+'/'+Quraa2Name
    if debug == 1 :
        print(Quraa2Name)
    AyaNum = str('{:0>4d}'.format(AyaIndex))
    completeName = os.path.join(aya_path, AyaNum+".mp3")
    return completeName
    
def image( AyaIndex):    
    aya_path = os.getcwd()+'/'+'AyatImages'
    AyaNum = str('{:0>4d}'.format(AyaIndex))
    completeName = os.path.join(aya_path, AyaNum+".png")
    return completeName
    

df = pd.read_csv('Quran_aya_index.csv')
pygame.mixer.init()
pygame.mixer.music.set_volume(1)

    

while(playcount):
    
    Surah_start = 1 #int(input("Surah start: "))   
    Surah_end   = 114 #int(input("Surah end  : "))
    Ayah_start  = 1 #int(input("Ayah start : ")) 
    Ayah_end    = 6 #int(input("Ayah end   : "))
    
    Q = random.randrange(0, len(Quraa2))
    
    AyaIndexStart = aya_index(Surah_start,Ayah_start)
    AyaIndexEnd   = aya_index(Surah_end,Ayah_end)
    
    for AyaIndex in range(AyaIndexStart,AyaIndexEnd+1):
        if AyaIndex % 10 == 0:
            Q = random.randrange(0, len(Quraa2))
        Qare2name = Quraa2[Q][Quraa2Name]
        completeName = sound(Qare2name, AyaIndex)
        play_sound(completeName)

            
    
    


