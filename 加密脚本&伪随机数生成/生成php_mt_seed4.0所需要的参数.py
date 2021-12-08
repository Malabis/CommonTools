s = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'c1z5DuPZXT'
m = ''
for i in key:
    for j in range(len(s)):
        if i == s[j]:
            m += "{} {} 0 {} ".format(j,j,len(s)-1)
print(m)
#2 2 0 61 27 27 0 61 25 25 0 61 31 31 0 61 39 39 0 61 20 20 0 61 51 51 0 61 61 61 0 61 59 59 0 61 55 55 0 61 