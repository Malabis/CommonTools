#在一大堆文件中遍历查找特定内容
import os
import re
import docx

os.chdir('D:/Desktop/five_month')
dires=os.listdir()#第一层目录，打开five_month目录，返回各文件组成的列表
for dire in dires:
    os.chdir(f'D:/Desktop/five_month/{dire}')
    dir=os.listdir()#第二层目录，打开从5.1-5.20的目录，返回各文件组成的列表
    for di in dir:
        os.chdir(f'D:/Desktop/five_month/{dire}/{di}')
        ds=os.listdir()#第三层目录，打开VR_1-20的目录
        for d in ds:
            path=(f'D:/Desktop/five_month/{dire}/{di}/{d}')
            #排除图片的干扰
            if re.search('(1|2|3|4|5|6).png',path) == None:
                #打开对应的word文档
                file=docx.Document(path)
                for pra in file.paragraphs:
                    #在对应段落中的文字查找KEY2
                    if re.search('KEY2',pra.text)!=None:
                        print(path)