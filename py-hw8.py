import math as math
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