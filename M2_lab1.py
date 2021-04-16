"""
Lab 1.1 - Chữ số cuối của một số Fibonacci bé
Mẫu 1.

Input:          
3
Output:
2

Input:
10
Output:
55

"""
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
n = int("Nhập vào số fibonaci muốn tìm: ")
print(Fibonacci(n))
 
# Driver Program
print(Fibonacci(9))
"""
Lab 1.2 - Chữ số cuối của một số Fibonacci lớn
"""
def fib(n): 
    F = [0,1]
    for i in range(2, n+1):
        F.append((F[i-1]+F[i-2])%10)
    return F[n]

n = int(input("Nhập vào số fibonaci muốn tìm số cuối cùng: "))
print(fib(n))