str1 ='FpCyLNvPOj'
str2 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result =''

length = str(len(str2)-1)
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i] ==  str2[j]:
            result += str(j) + ' ' +str(j) + ' ' + '0' + ' ' + length + ' '
            break

print(result)
```
php脚本
<?php
mt_srand(490664240);

$str_long1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$str='';
$len1=20;
for ( $i = 0; $i < $len1; $i++ ){
$str.=substr($str_long1, mt_rand(0, strlen($str_long1) - 1), 1);
}
echo $str;
```
