import math as math
import re as re
import string as string
import functions as f

# Уровень 1
text1 = "12 + 15"
digit = []
oper = []
f.FillList(text1,digit,oper)
res = 0
res = f.Enum(res,digit,oper)
print(f"{text1} = {res}")

# Уровень 2
text2 = "12 + 15 - 4"
digit = []
oper = []
f.FillList(text2,digit,oper)
res = 0
res = f.Enum(res,digit,oper)
print(f"{text2} = {res}")

# Уровень 3
text3 = "12 - 4 * 2 + 6 / 3"
# text3 = "12 - 4 * 2 + 6 / 3 + 5"
digit = []
oper = []
f.FillList(text3,digit,oper)
res = 0
res = f.EnumPrime(res,digit,oper)
print(f"{text3} = {res}")

text4 = "(12 - 4) * 2 + 5 * 6"
digit = []
oper = []
temp = text4
while True:
    start = temp.find('(')
    if start>=0:
        end = temp.find(')')
        textPrime = temp[start+1:end] 
        f.FillList(textPrime,digit,oper)
        res = 0
        if textPrime.find('*')>0 or temp.find('/')>0:
            res = f.EnumPrime(res,digit,oper)
        else:
            res = f.Enum(res,digit,oper)
        t1 = temp[0:start]
        t2 = temp[end+1:len(temp)]
        temp = t1+str(res)+t2
    else:
        break
digit = []
oper = []
f.FillList(temp,digit,oper)
res = 0
if len(oper)>1 and (temp.find('*')>0 or temp.find('/')):
    res = f.EnumPrime(res,digit,oper)
else:
    res = f.Enum(res,digit,oper)
print(f"{text4} = {res}")
