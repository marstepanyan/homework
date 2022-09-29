def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# 1 a program that asks the user for a weight in kilograms and converts it to pounds
weight = input('enter weight in kilograms: ')

if not is_number(weight):
    print('that\'s not a number')
else:
    weight_in_pounds = float(weight) * 2.2
    print('weight in pounds: ', "{:.2f}".format(weight_in_pounds))


# 2 a program that generates and prints 50 random integers
import random
for i in range(51):
    print(i, '-', random.randint(3, 6))


# 3 computes | x − y | /  x+y
num1 = input('enter first number: ')
num2 = input('enter second number: ')

if not is_number(num1) or not is_number(num2):
    print('that\'s not a number')
else:
    num1 = float(num1)
    num2 = float(num2)
    print("{:.2f}".format(abs(num1 - num2) / (num1 + num2)))


# 5 a program that finds all four of the perfect numbers that are less than 10000
import math


def find_divisors(n):
    divisors = []
    j = 2
    while j <= math.sqrt(n):

        if n % j == 0:

            # If divisors are equal, print only one
            if n / j == j:
                divisors.append(j)
            else:
                # Otherwise, print both
                divisors.append(j)
                divisors.append(int(n / j))

        j = j + 1
    return divisors


def is_perfect(n):
    return int(n) == sum(find_divisors(int(n))) + 1


res = []
for num in range(2, 10000):
    if is_perfect(num):
        res.append(num)

print('All four of the perfect numbers that are less than 10000: ', res)
