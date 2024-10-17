def fibo(lim):
    res = [1,1]
    while (res[len(res)-1]+res[len(res)-2]<=lim):
        res.append(res[len(res)-1]+res[len(res)-2])
    return res
    
    

temp = input("numero o termo limite da sequencia de fibbonaci: ")
print(f"fib({temp}) = ",end="")
print(fibo(int(temp)))