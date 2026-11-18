def bincode(x):
    global signum
    try:
        signum
    except:
        if x < 0:
            signum = '-'
        else:
            signum = ''
        x = abs(x)
    
    if x < 2:
        return signum + str(x)
    else:
        return bincode(x // 2) + str(x % 2)

n = int(input())
print(bincode(n))
