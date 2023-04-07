print("加载中……")
import json
import unicodedata
import os
import random
score = int("0")

datafile = 'idiom.json'
f = open(datafile,'r', encoding="utf-8") 
g = f.read()
database = json.loads(g) 
data = {}
for item in database:
    word = item["word"]
    pinyin1 = item["pinyin"]
    pinyin=unicodedata.normalize('NFKD', pinyin1).encode('ascii','ignore')
    data[word] = pinyin
# print(data)
print("欢迎来到成语接龙！\n首尾相接的字可以是同音不同调哦！\n不想玩了说【结束】退出哦！\n现在是你先来还是我先来呢？")
iscf = True
hfocfunknown = True
computerword = ""
computerpinyin = ""
computerpinyinInCharList = []
humanword = ""
humanpinyin = ""
humanpinyinInCharList = []
while hfocfunknown:
    hfocf_str = input("【你先来】/【我先来】") 
    if hfocf_str == "结束":
            print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
            quit()
    if hfocf_str=="你先来":
        iscf = True
        hfocfunknown = False
        print("那我先来吧！我接——")
        key, value = random.choice(list(data.items()))
        computerword = key
        computerpinyin = value
        print("（电脑：）",computerword,"\n现在轮到你了——")
        humanword = input("（人脑：）")
        if humanword == "结束":
            print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
            quit()
    elif hfocf_str=="我先来":
        iscf = False
        hfocfunknown = False
        print("那你来一个——")
        humanword = input("（人脑：）")
        if humanword == "结束":
            print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
            quit()
    else:
        print("我没懂，你说你先来还是我先来？")
        hfocfunknown = True
while True:
    while humanword not in data.keys():
        print("你说的成语我可能不知道，换一个试试——")
        humanword = input("（人脑：）")
        if humanword == "结束":
            print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
            quit()
        #humanword = input("你再来一个——\n（人脑：）")
    humanpinyin = data[humanword]
    humanpinyinInCharList = humanpinyin.decode().split(" ")
    #print(humanpinyinInCharList)
    if not computerword == "":
        computerpinyin = data[computerword]
        computerpinyinInCharList = computerpinyin.decode().split(" ")
        while computerpinyinInCharList[-1] != humanpinyinInCharList[0]:
            print("你说的成语首字不匹配，换一个试试——")
            humanword = input("（人脑：）")
            if humanword == "结束":
                print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
                quit()
            humanpinyin = data[humanword]
            humanpinyinInCharList = humanpinyin.decode().split(" ")
            # computerpinyin = data[computerword]
            # computerpinyinInCharList = computerpinyin.decode().split(" ")
    for key,value in data.items():
        datapinyinInCharList = value.decode().split(" ")
        if datapinyinInCharList[0] == humanpinyinInCharList[-1]:
            computerword = key
            computerpinyin = value
            datapinyinInCharList = value.decode().split(" ")
    score += 1
    print("真棒！我接一个——\n（电脑：）"+computerword)
    humanword = input("你再来一个——\n（人脑：）")
    if humanword == "结束":
        print("本轮游戏你接对了"+str(score)+"个成语。欢迎下次再来！")
        quit()
