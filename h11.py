# Напишите функцию letters_range, которая ведет себя
# похожим на range образом, однако в качестве start и
# stop принимает не числа, а буквы латинского алфавита
# (в качестве step принимает целое число) и возращает
# не перечисление чисел, а список букв, начиная с
# указанной в качестве start, до указанной в качестве
# stop с шагом step (по умолчанию равным 1).
#
# Пример:
# >>>letters_range('b', 'w', 2)
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']
#
# >>>letters_range('a', 'g')
# ['a', 'b', 'c', 'd', 'e', 'f']
#
# >>>letters_range('g', 'p')
# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
#
# >>>letters_range('p', 'g', -2)
# ['p', 'n', 'l', 'j', 'h']
#
# >>>letters_range('a','a')
# []

ALPHABET = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def letters_range(start, stop, step = 1):
    start = ALPHABET.index(start.upper())
    stop = ALPHABET.index(stop.upper())
    print(ALPHABET[start:stop:step])
letters_range('p', 'g', -2)

