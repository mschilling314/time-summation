# t1 and t2 are strings in mm:ss format
def timeAdd(t1, t2):
    t1s = t1.split(':')
    t2s = t2.split(':')
    rsec = int(t1s[1]) + int(t2s[1])
    rh = int(t1s[0]) + int(t2s[0])
    if rsec >= 60:
        rsec = rsec % 60
        rh += 1
    if rsec < 10:
        rsec = '0' + str(rsec)
    else:
        rsec = str(rsec)
    return str(rh) + ':' + rsec
    
def addTimes(tarr):
    sum = '0:00'
    for t in tarr:
        sum = timeAdd(sum, t)
    return sum

def takeInput():
    flag = True
    times = []
    while flag:
        inn = input('Provide a time in mm:ss format or press q to quit: ')
        if inn == 'q':
            flag = False
        else:
            times.append(inn)
    return times
            
ts = takeInput()
print()
print(f'The result is: {addTimes(ts)}')
