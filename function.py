def épar(x):
    return x%2 ==0

def factorial(n):
   f = 1
   for i in range(0, n):
    f = f * n
    n = n- 1
   return f

m = factorial(10)
print(m)


      