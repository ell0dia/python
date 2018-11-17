# https://projecteuler.net/problem=36
#
# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.

numbers_sum = 0

def cut_bin(x):
    x = bin(x)
    return x[2::]


for number in range(1, 1000000):
    if str(number) == str(number)[::-1] and str(cut_bin(number)) == str(cut_bin(number))[::-1]:
        numbers_sum += number


print(numbers_sum)
print(bin(numbers_sum))