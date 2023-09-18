n = int(input("Введите номер числа Фибоначчи: "))

if n == 0:
    fib = 0
elif n == 1:
    fib = 1
else:
    fib_prev = 0
    fib = 1
    for i in range(2, n+1):
        fib_new = fib_prev + fib
        fib_prev = fib
        fib = fib_new

print(fib)


n = int(input("Введите число: "))
temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if n == rev:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
