import random
import time
import math
score =0
oyun = 0
while True:
    a =random.randint(1,4)
    oyun=oyun+1
    print("oyun",oyun)
    print("teze sual hazirlanir")
    time.sleep(1)
    if a==1:
        print ("toplama:")
        birinci = random.randint(1,20)
        ikinci = random.randint(1,10)
        print(birinci,ikinci,"nin cemini daxil et")
        cem= int(input("cavab: "))
        if(cem == birinci+ikinci):
            print("tebrik")
            score = score+1
            print("score: ",score)
            time.sleep(1)
        else:
            print("YANLIS",birinci+ikinci)
            score=score-3
            print("score: ",score)
            time.sleep(1)
    elif a==2:  
        print ("cixma:")
        birinci = random.randint(1,20)
        ikinci = random.randint(1,10)
        print(birinci,ikinci,"nin ferqini daxil et")
        ferq= int(input("cavab: "))
        if(ferq == birinci-ikinci):
            print("tebrik")
            score = score+1
            print("score: ",score)
            time.sleep(1)
        else:
            print("YANLIS",birinci-ikinci)
            score=score-3
            print("score: ",score)
            time.sleep(1)
    elif a==3:
        print ("vurma:")
        birinci = random.randint(1,20)
        ikinci = random.randint(1,10)
        print(birinci,ikinci,"nin hasilini daxil et")
        hasil= int(input("cavab: "))
        if(hasil == birinci*ikinci):
            print("tebrik")
            score = score+1
            print("score: ",score)
            time.sleep(1)
        else:
            print("YANLIS",birinci*ikinci)
            score=score-3
            print("score: ",score)
            time.sleep(2)
    elif a==4:
        print ("cixma:")
        birinci = random.randint(1,5)
        print(birinci,"nin faktorielini  daxil et")
        faktoriel= int(input("cavab: "))
        if(faktoriel == math.factorial(birinci)):
            print("tebrik")
            score = score+1
            print("score: ",score)
            time.sleep(1)
        else:
            print("YANLIS",math.factorial(birinci))
            score =score-3
            print("score: ",score)
            time.sleep(1)           