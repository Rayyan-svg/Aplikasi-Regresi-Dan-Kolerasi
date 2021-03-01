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

def FindResult(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Yi2= sigpow1(inpY)[0]
    Xi2= sigpow1(inpX)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = round(((inpN * XiYi) - (Xi * Yi)) / ((((inpN * Xi2) - (Xi ** 2)) * ((inpN * Yi2)-(Yi ** 2))) ** 0.5), 3)
    return out

def GuilfordScale(inp):
    if (inp < 0.2) and (inp >= 0):
        Scale = 'Very Weak'
    elif (inp < 0.4) and (inp >= 0.2):
        Scale = 'Weak'
    elif (inp < 0.6) and (inp >= 0.4):
        Scale = 'Medium'
    elif (inp < 0.8) and (inp >= 0.6):
        Scale = 'Strong'
    elif (inp <= 1.0) and (inp >= 0.8):
        Scale = 'Very Strong'
    return Scale
    
def Input():
    global n
    print('Please Input The X Value')
    while True:
        entry = input('Number : ')
        if entry == '':
            break
        try:
            x.append(int(entry))
        except:
            print("The Number Is Not Valid!")
    print('Please Input The Y Value')
    while True:
        entry = input('Number : ')
        if entry == '':
            break
        try:
            y.append(int(entry))
        except:
            print("The Number Is Not Valid!")
    n = int(input('Please Input The Amount Of Numbers : '))


'''MAIN PROGRAM'''
x = []
y = []
n = 0
Input()
print('Summary')
Result = FindResult(x,y,n)
print('Numbers Scale = ', Result)
print('Skala Guilford =', GuilfordScale(Result))
print('Coefficient Of Determination =', (Result ** 2)*100,'%')
print('There Are', 100-((Result ** 2)*100), '% Contribution From Other Factors')

print('Nama : Rayyan Nrp : 152018079')