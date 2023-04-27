#Урок 3. Функции, рекурсия, алгоритмы

#prime numbers as generator with yield
# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True


# def primeGenerator(a, b):
#     for i in range(a,b):
#         if isPrime(i):
#            yield i

    
# f = int(input())
# t = int(input())

# print(list(primeGenerator(f, t)))
# a = ( lambda x: x * (x+1)) 
# a = a(6)
# print(a)

# nums = {1,2,3,4,5,6,7,8}
# res = list(filter(lambda x: x%2 ==0, nums))
# print(res)

def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)