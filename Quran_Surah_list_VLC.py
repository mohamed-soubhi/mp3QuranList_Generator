# import csv
import json
import requests
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


Surah_nums = ['']

# Prompt the user for input on which Surahs to include in the playlist
Surah_nums_inp = input('Enter the numbers of Surah separated by : OR , :-\n')

# Generate a playlist name based on the user's input
playlist_name = ('quranList_' + Surah_nums_inp + '.xspf').replace(':', 'to').replace(',', 'and')


# Process the user's input to create a list of Surah numbers
if ':' in Surah_nums_inp:
    # If the input includes a range (e.g. "1:5"), create a list of numbers from the range
    Surah_nums = range(int(Surah_nums_inp.replace(' ', '').split(':')[0]), int(Surah_nums_inp.replace(' ', '').split(':')[1])+1)
elif ',' in Surah_nums_inp:
    # If the input includes a list of numbers separated by commas (e.g. "1,2,3"), create a list from the input
    Surah_nums = Surah_nums_inp.replace(' ', '').split(',')
else:
    Surah_nums[0] = int(Surah_nums_inp)

print(*Surah_nums, sep = ", ")

# URL of the mp3quran API
url = 'https://www.mp3quran.net/api/v3/reciters?language=ar'

# List to store the URLs of all audio files
mp3QuranURL = []

# List to store the URLs of the audio files for the Surahs specified by the user
listen_URL = []

# Send a GET request to the API to retrieve a list of reciters and their corresponding audio files
response = requests.get(url)

# Load the JSON data from the response
data = response.json()

# Get the list of reciters from the JSON data
reciters = data['reciters']



df = pd.DataFrame(['id', 'name', 'letter','moshaf_id','moshaf_name','moshaf_surah_num','moshaf_surah_url'])


# Iterate through the list of reciters and write each row to the CSV file
for reciter in reciters:
    for moshaf in reciter['moshaf']:
        # Write the reciter's information and the information for each moshaf (edition of the Quran)
        
        # Split the list of Surahs for the moshaf into a list of individual Surah numbers
        surah_list = moshaf['surah_list'].split(',')
        for surah in surah_list:
            mp3Url = moshaf['server'] + f'{int(surah):03d}' +'.mp3'
            mp3QuranURL.append(mp3Url)
            df= df.append([reciter['id'],reciter['name'],reciter['letter'],moshaf['id'],moshaf['name'],surah,mp3Url])
                    
            for Surah_num in Surah_nums:
                if f'{int(Surah_num):03d}' in mp3Url :
                    listen_URL.append(mp3Url)

#df.to_csv('mp3Quran.csv',index=False,sep=',')
#print("Finished writing CSV file")



with open(playlist_name, 'w',encoding="utf-8") as quranList:
    quranList.write("""<?xml version="1.0" encoding="UTF-8"?>
    <playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">
            <title>Playlist</title>
            <trackList>""")
    i = 0
    for link in listen_URL:
        quranList.write("""		<track>
                            <location>"""+link+"""</location>
                            <extension application="http://www.videolan.org/vlc/playlist/0">
                                    <vlc:id>"""+str(i)+"""</vlc:id>
                                    <vlc:option>network-caching=1000</vlc:option>
                            </extension>
                    </track>""")
        i+=1

    quranList.write("""	</trackList>
            <extension application="http://www.videolan.org/vlc/playlist/0">
                    <vlc:node title="qurango.xspf">""")
    for i in range(len(listen_URL)):
        quranList.write('			<vlc:item tid="'+str(i)+'"/>')

    quranList.write("""		</vlc:node>
            </extension>
    </playlist>
    """)
print("Finished writing "+playlist_name)
