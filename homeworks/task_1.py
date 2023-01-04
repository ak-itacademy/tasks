'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple


# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return first + second, first - second, first * second


# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return first / second, first // second, first % second


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> int:
    first = first ^ second
    second = first ^ second
    first = second ^ first
    return first, second


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float:
    if first < second:
        return first
    return second


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value << 1, value << 3, value << 5


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    return (divident % divider) ** power


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    if value & (1 << 31):
        return -1
    return 0


# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    return ~value + 1


# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    for i in range(0, 32, 2):
        if value & (1 << i) >= 1:
            return True
    return False


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    count = 0
    for i in range(32):
        if value & (1 << i) == 0:
            count += 1
    return count


# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    return (second & 0x0f) << 4 | (first & 0x0f)


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(value: int) -> int:
    first = value & 0x0f
    second = (value >> 4) & 0x0f
    return first, second


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
def clamp(value: float, low: float, high: float) -> float:
    if low <= value <= high:
        return value
    elif value < low:
        return low
    return high

# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    if low <= value <= high or high <= value <= low:
        return value
    elif value > low > high or value < low < high:
        return low
    elif value > high > low:
        return high


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    return -10 <= value < 10 and value % 2 == 1


# Определить порядок выполнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** (4 * (0.5 + 0.25))


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    value = value | (1 << n)
    return value


# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
    value = value ^ (1 << n)
    return value


# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return (x + 3) ** 3


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
    return last + ((first - last) & ((first - last) >> 31))