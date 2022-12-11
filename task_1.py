'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple


# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return first+second, first-second, first * second
print(add_mul(2.5, 4.8))

# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return first / second, first // second, first % second
print(div_int_rem(5, 8))


# Обменять два целочисленных значение с помощью битового xor не используя промежуточные переменные.
def xor_swap(a: int, b: int) -> int:
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return a, b
print(xor_swap(2, 3))


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(a: float, b: float) -> float:
    if a < b:
        return a
    elif a == b:
        return 'числа равны'
    else:
        return b
print(min_conditional(5, 7))


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value << 1, value << 3, value << 5
print(mul_shift_2_8_32(1))


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5
print(div_shift_2_8_32(32))


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    try:
        return (divident % divider) ** power
    except ZeroDivisionError:
        return 'divider не должен быть равен нулю'
print(exponentiation(27, 12, 5))


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    return 'знак +' if ~value & (1 << 32) else 'знак -'
print(sign(2845645471))


# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    return ~value + 1
print(change_sign(255))


# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    counter = 0
    for i in range(0, 32, 2):
        if value & (1 << i):
            counter +=1
    return True if counter > 0 else False
print(check_32_even_bit_set(4294967294))


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    count = 0
    for i in range(32):
        if value & (1 << i) == 0:
            count += 1
    return count
print(calculate_32_zero_bits(4294967294))


# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    return ((first & 0b11110000) >> 4) | (second & 0b11110000)
print(pack_4_4(170, 142))


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(value: int):
    first = (value & 0b00001111) << 4
    second = (value & 0b11110000)
    return first, second
print(unpack_4_4(138))


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
def clamp(value: float, low: float, high: float) -> float:
    if low <= value <= high:
        return value
    elif value < low:
        return low
    else:
        return high
print(clamp(12, 12, 55))


# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    if low <= high:
        if low <= value <= high:
            return value
        elif value < low:
            return low
        else:
            return high
    else:
        if high <= value <= low:
            return value
        elif value < high:
            return high
        else:
            return low
print(clamp_any(98, 45, 89))


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    return True if -10 <= value <= 10 and value % 2 else False
print(event_and_match_interval_m10_10(7))


# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** (4 * (0.5 + 0.25))


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    return value | (1 << n)
print(set_nth_bit(32, 2))


# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    return value ^ (1 << n)
print(switch_nth_bit(38, 1))


# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return (x + 3) ** 3
print(change_priorities(2))

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


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    return last + ((first - last) & ((first-last) >> 31))
print(min_raw(145, 254))
