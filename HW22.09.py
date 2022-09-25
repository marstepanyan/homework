# 1 checks and prints whether the number is even or odd
number = input('Enter a number: ')


if not number.isnumeric():
    print('that\'s not a number')
else:
    if int(number) % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


# 2 checks and prints whether the character is a consonant or a vowel
char = input('Enter a character: ')
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
if len(char) > 1 or not char.isalpha():
    print('that\'s not a character')
else:
    if char in vowels:
        print(f'{char} is vowel')
    else:
        print(f'{char} is consonant')


# 3 prints the n-th Fibonacci number
n = input('Enter a number: ')


if not n.isnumeric():
    print('that\'s not a number')
else:
    a, b = 0, 1
    count = 1
    while count < int(n):
        a, b = b, a + b
        count += 1
    print(f'{n}-th Fibonacci number is {a}')


# 4 prints the sum of nums digits on the screen
num = input('Enter a number: ')


if not num.isnumeric():
    print('that\'s not a number')
else:
    sum_of_digits = 0
    for digit in num:
        sum_of_digits += int(digit)
    print(f'the sum of {num}\'s digits is {sum_of_digits}')


# 5 prints the image
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
