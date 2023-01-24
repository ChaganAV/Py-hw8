import math as math

def Calc(oper,x,y):
    if oper=='+':
        return x+y
    if oper=='-':
        return x-y
    if oper=='*':
        return x*y
    if oper=='/':
        return x/y

text1 = "12 + 15"
text2 = "12 + 15 - 4"

digit = []
oper = []

for t in text1.split(' '):
    if t.isdigit():
        digit.append(int(t))
    else:
        oper.append(t)
# print(len(oper))
res = 0
for i in range(0,len(oper)):
    if res==0:
        res = Calc(oper[i],digit[i],digit[i+1])
    else:
        res = Calc(oper[i],res,digit[i+1])
print(f"{text1} = {res}")