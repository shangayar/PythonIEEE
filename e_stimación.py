#Aproximación del número e
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

def euler(n):
    fact=1
    while(n!=0):
        fact= fact + 1/factorial(n)
        n-=1
    return fact


print(f"El número Euler es {euler(20)}")