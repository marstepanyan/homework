# 1 Create a string that consists of the user’s numbers separated by plus signs
res = ''
for i in range(1, 6):
    num = input(f'Enter number {i}: ')
    res += num + '+'

print(res[:-1])


# 2 print Valid if the phone number is a real phone number, and Invalid otherwise
number = input('Enter a phone number: ')


def is_phone_number(phone_number):
    if '-' not in phone_number:
        return 'Invalid'

    number_parts = phone_number.split('-')

    if (not number_parts[0].isnumeric()) or (number_parts[0] != '1' and len(number_parts[0]) != 3):
        return 'Invalid'

    if number_parts[0] == '1':
        if len(number_parts) != 4 or \
                (len(number_parts[1]) != 3) or (len(number_parts[2]) != 3) or (len(number_parts[-1]) != 4):
            return 'Invalid'

    if len(number_parts[0]) == 3:
        if len(number_parts) != 3 or (len(number_parts[1]) != 3) or (len(number_parts[2]) != 4):
            return 'Invalid'

    return 'Valid'


print(is_phone_number(number))


# 3 a list that consists of all palindromic numbers between 100 and 1000
def is_palindromic(n):
    return n[::-1] == n


res = [num for num in range(100, 1000) if is_palindromic(str(num))]
print('Palindromic numbers between 100 and 1000: ', res)


# 4 produce a list of the gaps, find the maximum gap size and the percentage of gaps that have size 2
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
len_L = len(L)
gaps = [L[i] - L[i - 1] for i in range(1, len_L)]
print('All gaps: ', gaps)
max_gap = max(gaps)
print('Max gap: ', max_gap)
percentage_of_gaps2 = (gaps.count(2) / len(gaps)) * 100
print(f'The percentage of gaps that have size 2 is {percentage_of_gaps2}%')


# 5
product = {}
while True:
    product_name = input('Enter the name of product: ')
    if product_name == '':
        break
    product_price = int(input('Enter the price of that product: '))
    product[product_name] = product_price

print(product)

while True:
    product_name = input('Enter the name of product to see price: ')
    if product_name == '':
        break
    if product_name not in product.keys():
        print('There isn\'t such product')
    else:
        print(product[product_name])


# 6
di = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
      {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
      {'name': 'Princess', 'phone': '555-3141', 'email': ''},
      {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

print('Phone ends with 8: ')
for i in di:
    if i['phone'].endswith('8'):
        print(i['name'])

print('Don’t have an email address: ')
for i in di:
    if i['email'] == '':
        print(i['name'])


# 7
lst = [[1, 3, 7, 9, 5],
       [2, 44, 63, 81, 10],
       [3, 3, 3, 4, 15],
       [6, 7, 8, 3, 10],
       [10, 10, 11, 3, 7]]

num_dict = {}
for i in range(len(lst)):
    for j in range(len(lst)):
        num_dict[lst[i][j]] = num_dict.get(lst[i][j], 0) + 1

print(num_dict)

sorted_values = list(set(num_dict.values()))
sorted_values.sort(reverse=True)
print('The three most common numbers: ')
for item in sorted_values[:3]:
    for k in num_dict.keys():
        if num_dict[k] == item:
            print(k)
