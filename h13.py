# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def temp(t, scale):
    if scale == "to_c":
        return float(5 / 9 * (t - 32))
    elif scale == "to_f":
        return float(9 / 5 * t + 32)
    else:
        return "Incorrect temp scale"


print(temp(0, 'to_c'))
print(temp(0, 'to_f'))
