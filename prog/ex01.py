def emcriptar(text):
    temp =  [ord(c)-96 for c in text]
    res = []
    for c in range(len(temp)):
        if temp[c]<=0:
            res.append(0)
        else:
            res.append(temp[c])
    return res
    
def descript(num):
    temp = []
    for c in num:
        if c==0:
            temp.append(" ")
        else:
            temp.append(chr(c+96))
    return temp

print(descript([0,1,2,3,4]))