def Calc(oper,x,y):
    if oper=='+':
        return x+y
    if oper=='-':
        return x-y
    if oper=='*':
        return x*y
    if oper=='/':
        return x/y
def Enum(result,digit,oper):
    for i in range(0,len(oper)):
        if result==0:
            result = Calc(oper[i],digit[i],digit[i+1])
        else:
            result = Calc(oper[i],result,digit[i+1])
    return result

def FillList(text,digit,oper):
    for t in text.split(' '):
        if t.isdigit():
            digit.append(int(t))
        else:
            oper.append(t)

