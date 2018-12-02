# Написать функцию Фиббоначи fib(n), которая вычисляет
# элементы последовательности Фиббоначи:
# 1 1 2 3 5 8 13 21 34 55 .......

def fib(n):
    fiblist = [1, 1]
    if n == 1: return [1]
    elif n == 0: return []
    else:
        while len(fiblist) < n:
            new = fiblist[-1] + fiblist[-2]
            fiblist.append(new)

        return fiblist

# print(fib(0))
# print(fib(5))
# print(fib(1))
# print(fib(999))
