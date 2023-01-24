import math as math
import functions as f

text1 = "12 + 15"

digit = []
oper = []

# for t in text1.split(' '):
#     if t.isdigit():
#         digit.append(int(t))
#     else:
#         oper.append(t)
f.FillList(text1,digit,oper)
# Уровень 1
res = 0
# for i in range(0,len(oper)):
#     if res==0:
#         res = f.Calc(oper[i],digit[i],digit[i+1])
#     else:
#         res = f.Calc(oper[i],res,digit[i+1])
res = f.Enum(res,digit,oper)

print(f"{text1} = {res}")

# Уровень 2
text2 = "12 + 15 - 4"
digit = []
oper = []
for t in text2.split(' '):
    if t.isdigit():
        digit.append(int(t))
    else:
        oper.append(t)
res = 0
for i in range(0,len(oper)):
    if res==0:
        res = f.Calc(oper[i],digit[i],digit[i+1])
    else:
        res = f.Calc(oper[i],res,digit[i+1])
print(f"{text2} = {res}")