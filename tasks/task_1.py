'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''


from typing import Tuple, Optional
import struct


# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return first + second, first - second, first * second


# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# print(add_mul(a, b))


# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return first / second, first // second, first % second


# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# print(div_int_rem(a, b))


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> Tuple[int, int]:
    first = first ^ second
    second = first ^ second
    first = first ^ second
    return first, second


# a = int(input("Enter the first int number -> "))
# b = int(input("Enter the second int number -> "))
# print(xor_swap(a, b))


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float:
    return first if first < second else second


# a = float(input("Enter the first float number -> "))
# b = float(input("Enter the second float number -> "))
# print(min_conditional(a, b))


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value << 1, value << 3, value << 5


# a = int(input("Enter int number -> "))
# print(mul_shift_2_8_32(a))


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5


# a = int(input("Enter int number -> "))
# print(div_shift_2_8_32(a))


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(dividend: float, divider: float, power: float) -> Optional[float]:
    try:
        result = (dividend % divider) ** power
    except ZeroDivisionError:
        print("Division by zero!")
        result = None
    return result


# dividend = float(input("Enter float dividend number -> "))
# divider = float(input("Enter float divider number -> "))
# power = float(input("Enter float power number -> "))
# print(exponentiation(dividend, divider, power))


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    return -1 if value & (1 << 32) else 1


# value = int(input("Enter int number -> "))
# print(sign(value))

# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    return ~value + 1


# value = int(input("Enter int number -> "))
# print(change_sign(value))


# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    return any(value & (1 << i) for i in range(0, 32, 2))


# value = int(input("Enter int number -> "))
# print(bin(value))
# print(check_32_even_bit_set(value))


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    return sum(not value & (1 << i) for i in range(0, 32))


# value = int(input("Enter int number -> "))
# print(calculate_32_zero_bits(value))


# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    if first > 15 or second > 15:
        print("Some data will be lost!")
    return (second & 0x0f) << 4 | (first & 0x0f)


# value_1 = int(input("Enter int number in the range 0...15 -> "))
# value_2 = int(input("Enter int number in the range 0...15 -> "))
# print(pack_4_4(value_1, value_2))


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(number: int) -> Tuple[int, int]:
    if number > 255:
        print("Some data will be lost!")
    return number & 0x0f, (number >> 4) & 0x0f


# value = int(input("Enter int number in the range 0...255 -> "))
# print(unpack_4_4(value))


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.


def clamp(value: float, low: float, high: float) -> Optional[float]:
    if low > high:
        print("Lower range limit is higher than higher range limit!")
        return None
    else:
        if value < low:
            return low

        if value > high:
            return high
        return value


# low = float(input("Enter float number of lower range limit-> "))
# high = float(input("Enter float number of higher range limit-> "))
# value = float(input("Enter float number-> "))
# print(clamp(value, low, high))


# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> Optional[float]:
    if low > high:
        low, high = high, low
    return clamp(value, low, high)


# low = float(input("Enter float number of lower range limit-> "))
# high = float(input("Enter float number of higher range limit-> "))
# value = float(input("Enter float number-> "))
# print(clamp_any(value, low, high))


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    return -10 <= value <= 10 and value % 2


# value = int(input("Enter int number-> "))
# print(event_and_match_interval_m10_10(value))


# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** (4 * (0.5 + 0.25))


# value = float(input("Enter float number-> "))
# print(reverse_operations(value))


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    return value | 1 << n


# value = int(input("Enter int number-> "))
# n = int(input("Enter int number-> "))
# print(bin(value))
# print(bin(set_nth_bit(value, n)))


# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    return value ^ 1 << n


# value = int(input("Enter int number-> "))
# n = int(input("Enter int number-> "))
# print(bin(value))
# print(bin(switch_nth_bit(value, n)))


# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return (x + 3) ** 3


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
    sign = 0 if value >= 0 else 1
    value = abs(value)

    if value > 1 << 128:
        value = 1 << 128

    i = 0
    while value >= 1 << i:
        i += 1

    exp = 127 + i - 1 if value >= 1 else 0
    man = int((1 << 23) * ((value - (1 << (i - 1))) / ((1 << i) - (1 << (i - 1))))) if value >= 1 else 0

    my_value = sign << 31 | exp << 23 | man
    my_bytes = struct.pack("L", my_value)
    return struct.unpack("f", my_bytes)[0]


x = int(input("Enter int number-> "))
print(int_to_float(x))


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    return ((first - last) >> 32) * (last - first) + last

# first = int(input("Enter int number-> "))
# last = int(input("Enter int number-> "))
# print(min_raw(first, last))
