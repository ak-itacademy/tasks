'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple


# Задача 1
# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> tuple[float, float, float]:
    return first + second, first - second, first * second


print(add_mul(11.3, 6.3))


# Задача 2
# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> tuple[float, float, float]:
    return first / second, first // second, first % second


print(div_int_rem(11.3, 6.3))


# Задача 3
# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> int:
    return (first ^ second) ^ first, (second ^ first) ^ second


print(xor_swap(5, 19))

# Задача 4
# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float | str:
    if first < second:
        return first
    elif first == second:
        return 'numbers equal'
    else:
        return second


print(min_conditional(5, 5))

# Задача 5
# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.

def mul_shift_2_8_32(value: int) -> tuple[int, int, int]:
    return value << 1, value << 3, value << 5


print(mul_shift_2_8_32(5))

# Задача 6
# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.

def div_shift_2_8_32(value: int) -> tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5


print(div_shift_2_8_32(321))

# Задача 7
# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    return (divident % divider) ** power


print(exponentiation(9, 5, 2))

# Задача 8
# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    mask = 1 if value < 0 else 0
    return mask & (value >> 31)


print(sign(-1256398989))


# Задача 9
# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    var = ~ value + 1
    return var


print(change_sign(-1256398989))

# Задача 10
# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    a = bool(0)
    for i in range(2, 32, 2):
        if (value & (1 << i)) != 0:
            a = bool(1)
            break
    return a


print(check_32_even_bit_set(7))

# Задача 11
# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    counter = 0
    for i in range(32):
        if (value & (1 << i)) == 0:
            counter += 1
    return counter


print(calculate_32_zero_bits(11))

# Задача 12
# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    value = first | second << 4
    return value


print(pack_4_4(4, 10))

# Еще вариант, заморочилась начиталась, использовала функцию упаковки, но тут не в 8 бит.
import struct

def pack_4_4(first: int, second: int) -> bytes:
    pack = struct.pack("<ii", first, second)
    return int.from_bytes(pack, byteorder='big')


print(pack_4_4(2, 8))


# Задача 13
# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(value: int) -> tuple[int, int]:
    second = value >> 4
    value1 = value & ~ (1 << 4)
    value2 = value1 & ~ (1 << 5)
    value3 = value2 & ~ (1 << 6)
    first = value3 & ~ (1 << 7)
    return first, second


print(unpack_4_4(164))

# Еще вариант, но тут не в 8 бит.
import struct

def unpack_4_4(value: int) -> tuple[int, int]:
    unpack = struct.unpack("<ii", struct.pack(">q", value))
    return unpack


print(unpack_4_4(144115188210073600))

# Задача 14
# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(value, high))


print(clamp(10, 7, 9))

# Задача 15
# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    if low < high:
        return max(low, min(value, high))
    else:
        return max(high, min(value, low))


print(clamp_any(7, 9, 4))

# Задача 16
# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    if (-10 <= value <= 10) & value % 2 == 1:
        return bool(1)
    else:
        return bool(0)


print(event_and_match_interval_m10_10(67))

# Задача 17
# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    # value ** 4 * 0.5 + 0.25 - исходное выражение
    # ** = 1
    # * = 2
    # + = 3
    return ((0.5 + 0.25) * value) ** 4


print(reverse_operations(2))

# Задача 18
# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    value2 = value | (1 << n)
    return value2

# Задача 19
# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    value2 = value ^ (1 << n)
    return value2


print(switch_nth_bit(10, 1))

# Задача 20
# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    # x + 3 ** 3 - исходное выражение
    return (x + 3) ** 3


print(change_priorities(2))


'''
Задачи повышенной сложности.
'''

# Задача 2*
# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    a = (last - (((first - last) >> 31) * (first - last)))
    return a


print(min_raw(-15, - 14))
