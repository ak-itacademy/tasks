'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple


# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return ..., ..., ...

# def add_mul(first: float, second: float, round_amount = 10) -> Tuple[float, float, float]:
#     sum = round(first + second, round_amount)
#     sub = round(first - second, round_amount)
#     mul = round(first * second, round_amount)
#
#     return sum, sub, mul
#
# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# z = int(input("Enter rounding accuracy -> "))
# print(add_mul(a, b, z))


# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return ..., ..., ...


# def div_int_rem(first: float, second: float, round_amount = 10) -> Tuple[float, float, float]:
#     try:
#         div = round(first / second, round_amount)
#         int_div = first // second
#         rem = round(first % second, round_amount)
#     except ZeroDivisionError:
#         print("Division by zero!")
#         div, int_div, rem = None, None, None
#
#     return div, int_div, rem
#
# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# z = int(input("Enter rounding accuracy -> "))
# print(div_int_rem(a, b, z))


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> int:
    return ...

# def xor_swap(first: int, second: int) -> Tuple[int, int]:
#     first = first ^ second
#     second = first ^ second
#     first = first ^ second
#
#     return first, second
#
# a = int(input("Enter the first int number -> "))
# b = int(input("Enter the second int number -> "))
# print(xor_swap(a, b))


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float:
    return ...

# def min_conditional(first: float, second: float) -> float:
#     return first if first < second else second
#
# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# print(min_conditional(a, b))


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return ..., ..., ...

# def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
#     mul_shift_2 = value << 1
#     mul_shift_8 = value << 3
#     mul_shift_32 = value << 5
#     return mul_shift_2, mul_shift_8, mul_shift_32
#
# a = input("Enter int number -> ")
# a = int(a)
# print(mul_shift_2_8_32(a))


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return ..., ..., ...

# def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
#     div_shift_2 = value >> 1
#     div_shift_8 = value >> 3
#     div_shift_32 = value >> 5
#     return div_shift_2, div_shift_8, div_shift_32
#
# a = input("Enter int number -> ")
# a = int(a)
# print(div_shift_2_8_32(a))


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    return ...

# def exponentiation(divident: float, divider: float, power: float) -> float:
#     try:
#         result = (divident % divider) ** power
#     except ZeroDivisionError:
#         print("Division by zero!")
#         result = None
#     return result
#
#
# divident = float(input("Enter float divident number -> "))
# divider = float(input("Enter float divider number -> "))
# power = float(input("Enter float power number -> "))
# print(exponentiation(divident, divider, power))


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    return ...

# def sign(value: int) -> int:
#     return -1 if value & (2 ** 32) else 1
#
# value = int(input("Enter int number -> "))
# print(sign(value))

# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    return ...

# def change_sign(value: int) -> int:
#     return ~value + 1
#
# value = int(input("Enter int number -> "))
# print(change_sign(value))


# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    return ...

# def check_32_even_bit_set(value: int) -> bool:
#     i = 0
#     result = False
#     while i < 32:
#         if (value >> i) & 1:
#             result = True
#             break
#
#         i += 2
#     return result
#
# value = int(input("Enter int number -> "))
# print(bin(value))
# print(check_32_even_bit_set(value))


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    return ...

# def calculate_32_zero_bits(value: int) -> int:
#     i = 0
#     result = 0
#     while i < 32:
#         if not (value >> i) & 1:
#             result += 1
#
#         i += 1
#     return result
#
# value = int(input("Enter int number -> "))
# print(calculate_32_zero_bits(value))

# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    return ...

# def pack_4_4(first: int, second: int) -> int:
#     if(first > 15 or second > 15):
#         print("Some data will be lost!")
#
#     result = (second & 15) << 4 | (first & 15)
#     return result
#
# value_1 = int(input("Enter int number in the range 0...15 -> "))
# value_2 = int(input("Enter int number in the range 0...15 -> "))
# print(pack_4_4(value_1, value_2))


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(first: int, second: int) -> int:
    return ...

# def unpack_4_4(number: int) -> Tuple[int, int]:
#     if number > 255:
#         print("Some data will be lost!")
#     first = number & 15
#     second = (number >> 4) & 15
#     return first, second
#
# value = int(input("Enter int number in the range 0...255 -> "))
# print(unpack_4_4(value))


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
def clamp(value: float, low: float, high: float) -> float:
    return ...

# def clamp(value: float, low: float, high: float) -> float:
#     if low > high:
#         print("Lower range limit is higher than higher range limit!")
#         result = None
#     else:
#         if value < low:
#             print("Value {} is less than {}!".format(value, low))
#             result = low
#         elif value > high:
#             print("Value {} is more than {}!".format(value, high))
#             result = high
#         else:
#             result = value
#     return result
#
# low = float(input("Enter float number of lower range limit-> "))
# high = float(input("Enter float number of higher range limit-> "))
# value = float(input("Enter float number-> "))
# print(clamp(value, low, high))


# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    return ...

# def clamp_any(value: float, low: float, high: float) -> float:
#     if value > low and value > high:
#         result = max(low, high)
#     elif value < low and value < high:
#         result = min(low, high)
#     else:
#         result = value
#     return result
#
# low = float(input("Enter float number of lower range limit-> "))
# high = float(input("Enter float number of higher range limit-> "))
# value = float(input("Enter float number-> "))
# print(clamp_any(value, low, high))


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    return ...

# def event_and_match_interval_m10_10(value: int) -> bool:
#     return True if -10 <= value <= 10 and value % 2 else False
#
# value = int(input("Enter int number-> "))
# print(event_and_match_interval_m10_10(value))


# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** 4 * 0.5 + 0.25

# def reverse_operations(value: float):
#     return value ** (4 * (0.5 + 0.25))
#
# value = float(input("Enter float number-> "))
# print(reverse_operations(value))


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    return ...

# def set_nth_bit(value: int, n: int) -> int:
#     return value | 2 ** n
#
# value = int(input("Enter int number-> "))
# n = int(input("Enter int number-> "))
# print(bin(value))
# print(bin(set_nth_bit(value, n)))


# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    return ...

# def switch_nth_bit(value: int, n: int) -> int:
#     return value ^ 2 ** n
#
# value = int(input("Enter int number-> "))
# n = int(input("Enter int number-> "))
# print(bin(value))
# print(bin(switch_nth_bit(value, n)))


# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return x + 3 ** 3

# def change_priorities(x: float) -> float:
#     return (x + 3) ** 3
#
# x = float(input("Enter float number-> "))
# print(change_priorities(x))

'''
Задачи повышенной сложности.
'''


# Ковертировать целое число в формат float32.
# Для того, чтобы разобраться с форматом, можно использовать следующие источники:
# https://goo.su/ipKzbY
# https://learn.microsoft.com/ru-ru/cpp/build/ieee-floating-point-representation?view=msvc-170
# https://habr.com/ru/post/337260/
# Для решения этой задачи нужно также выяснить, как конвертировать байты в целые и дробные числа.
def int_to_float(value: int) -> float:
    return ...

# import struct
#
# def int_to_float(value: int) -> float:
#     if value == 0:
#         result = 0.0
#     else:
#         sign = 0 if value > 0 else 1
#
#         if value < 0:
#             value = ~(value - 1)
#
#         i = 0
#         while value >= 2 ** i:
#             i += 1
#
#         exp = 127 + i - 1
#         man = int(2 ** 23 * ((value - 2 ** (i - 1)) / (2 ** i - 2 ** (i - 1))))
#         my_value = sign << 31 | exp << (31 - 8) | man
#
#         my_bytes = struct.pack("L", my_value)
#         result = struct.unpack("f", my_bytes)
#
#     return result[0]
#
# x = int(input("Enter int number-> "))
# print(int_to_float(x))


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    return ...

# def min_raw(first: int, last: int) -> int:
#     difference = first ^ last
#
#     n = 0
#     remainder = difference
#     while remainder != 0:
#         n += 1
#         remainder = difference >> n
#
#     last_bit = n - 1
#
#     result = last if first & (1 << last_bit) else first
#
#     return result
#
#
# first = int(input("Enter int number-> "))
# last = int(input("Enter int number-> "))
# print(min_raw(first, last))