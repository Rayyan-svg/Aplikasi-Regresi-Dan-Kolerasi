# Nama  : Rayyan
# Nrp   : 152018079
# Kelas : C

def sigma1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

def sigma2(inpX, inpY):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

def sigpow1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

def FindA(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi2, nXi2 = sigpow1(inpX)[:2]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((Yi * Xi2) - (Xi * XiYi)) / ((inpN * nXi2[x]) - (Xi ** 2)), 3))
    return out

def FindB(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((inpN * XiYi) - (Xi * Yi)) / ((inpN * Xi) - (Xi ** 2)), 3))
    return out

def Input():
    global n
    print('Please Input The A Value (Constants)')
    while True:
        entry = input('Number : ')
        if entry == '':
            break
        try:
            x.append(int(entry))
        except:
            print("The Number Is Not Valid!")
    print('Please Input The B Value (Coefficient))')
    while True:
        entry = input('Number : ')
        if entry == '':
            break
        try:
            y.append(int(entry))
        except:
            print("The Number Is Not Valid!")
    n = int(input('N Value : '))


'''MAIN PROGRAM'''
x = []
y = []
n = 0
Input()
a = FindA(x,y,n)
b = FindB(x,y,n)
print('Summary')
print('Nama : Rayyan Nrp : 152018079')
print('The A Value = ', a)
print('The B Value = ', b)
print('Equation')
for i in range(n):
    print('(', i+1 ,') Y = ', a[i], ' + (', b[i], ')x')
