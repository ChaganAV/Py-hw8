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

def EnumPrime(result,digit,oper):
    digSimp = []
    opSimp = []
    for i in range(0,len(oper)):
        if result==0:
            if oper[i] == '*' or oper[i] == '/':
                result = Calc(oper[i],digit[i],digit[i+1])
                digSimp.append(result)
            else:
                digSimp.append(digit[i])
                opSimp.append(oper[i])
                if i==len(oper)-1:
                    digSimp.append(digit[i+1])

        else:
            if oper[i] == '*' or oper[i] == '/':
                result = Calc(oper[i],result,digit[i+1])
                digSimp.append(result)
            else:
                opSimp.append(oper[i])
                result = 0
                if i==len(oper)-1:
                    digSimp.append(digit[i+1])
    if len(oper)>1:
        result=0
        result = Enum(result,digSimp,opSimp)

    return result


