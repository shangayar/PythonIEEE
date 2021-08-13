def primo(n):
    if(n<=2):
        return False
    else:
        for i in range (2,n):
            if (n % i == 0):
                return False
            else:
                return True
"""  count=1
  inc=0
  if(n > 1):
     while(count<=n):
        if(n%count == 0):
            inc+=1
            count+=1
        else:
            count+=1
     if(inc == 2):
        return True
     else:
        return False
  else:
      return False"""

n=int(input("Ingrese un número entero: "))

if(primo(n)):
    print(f"el número {n} es Primo")
else:
    print(f"el número {n} no es Primo")