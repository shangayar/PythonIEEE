# 0 1 1 2 3 5 8 13 21
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n=int(input())
for i in range(n):
    print(fibo(i))