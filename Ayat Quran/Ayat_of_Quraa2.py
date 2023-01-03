import requests
import os
import os.path

Name=0
bitrate=1
All_Ayat =6236
Quraa2 = [["ar.ahmedajamy",128],
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



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


for Q in Quraa2 :

    if not os.path.exists(Q[Name]):
        os.mkdir(Q[Name])
    print(Q[Name])

    save_path = os.getcwd()+'/'+Q[Name]


    for i in range(1,All_Ayat+1):
    #for i in range(1,7):
        AyaNum = str('{:0>4d}'.format(i))

        completeName = os.path.join(save_path, AyaNum+".mp3") 
        
        if os.path.exists(completeName):
            print(Q[Name],'\t',i,'\t',i/6236, "File exist")
            xx=1
            
        else:
            
            printProgressBar(0, All_Ayat, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
            url = "https://cdn.islamic.network/quran/audio/"+str(Q[bitrate])+"/"+Q[Name]+"/"+str(i)+'.mp3'
            r = requests.get(url, allow_redirects=True)
            
          
            #print(completeName)

            #open(completeName, 'wb').write(r.content)
            File = open(completeName, 'wb')
            File.write(r.content)
            File.close()
            print(Q[Name],'\t',i,'\t',i/6236)
            #printProgressBar(i, All_Ayat, prefix = 'Progress:', suffix = 'Complete', length = 50)
        













