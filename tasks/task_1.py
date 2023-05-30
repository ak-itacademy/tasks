# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Задание 1.
# Базовые математические операции, приоритеты выполнения, условные операторы, циклы.

from typing import Tuple

# Реализовать функции сложения, вычитания и умножения двух чисел.
# def add_mul(first: float, second: float) -> Tuple[float, float, float]:
#    return ..., ..., ...

def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    # Compute the sum of the two numbers.
    sum = first + second

    # Compute the product of the two numbers.
    product = first * second

    # Compute the difference between the two numbers.
    difference = first - second

    # Return a tuple containing the sum, product, and difference.
    return sum, product, difference

# Реализовать функции деления, деления нацело и нахождения остатка от деления.
#def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
#    return ..., ..., ...

def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    # Compute the quotient of dividing the first number by the second number.
    quotient = first / second

    # Compute the integer quotient of dividing the first number by the second number.
    integer_quotient = first // second

    # Compute the remainder of dividing the first number by the second number.
    remainder = first % second

    # Return a tuple containing the quotient, integer quotient, and remainder.
    return quotient, integer_quotient, remainder


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
#def xor_swap(first: int, second: int) -> int:
#    return ...

def xor_swap(first: int, second: int) -> Tuple[int, int]:
    first = first ^ second
    second = first ^ second
    first = first ^ second
    return (first, second)

# Вернуть наименьшее число, используя условный оператор.
#def min_conditional(first: float, second: float) -> float:
#   return ...

def min_conditional(first: float, second: float) -> float:
    return first if first < second else second

# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
#def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
#    return ..., ..., ...

def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return (value << 1, value << 3, value << 5)

# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
#def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
#    return ..., ..., ...

def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return (value >> 1, value >> 3, value >> 5)

# Реализовать операцию возведения в степень остатка от деления.
#def exponentiation(divident: float, divider: float, power: float) -> float:
#    return ...

def exponentiation(divident: float, divider: float, power: float) -> float:
    remainder = divident % divider
    return remainder ** power

# Определить знак 32-битного числа с помощью операции &.
#def sign(value: int) -> int:
#    return ...

def sign(value: int) -> str:
    sign_bit = (value >> 31) & 1
    if sign_bit == 0:
        return "positive"
    else:
        return "negative"

# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
#def change_sign(value: int) -> int:
#    return ...

def change_sign(value: int) -> int:
    return (~value + 1)

# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
#def check_32_even_bit_set(value: int) -> bool:
#    return ...

def check_32_even_bit_set(value: int) -> bool:
    even_bits_mask = 0b01010101010101010101010101010101  # 32-битная маска четных битов
    # Когда мы выполняем операцию битового "&" между 32-битным числом и этой маской,
    # мы получаем только те биты, которые находятся на четных позициях в двоичном представлении числа.
    # Если хотя бы один из этих битов установлен в 1, значит, в числе есть хотя бы один четный бит, и функция возвращает True,
    # иначе функция вернет False.
    return bool(value & even_bits_mask)

# Посчитать количество бит в 32-х битном числе, установленных в ноль.
#def calculate_32_zero_bits(value: int) -> int:
#    return ...

def calculate_32_zero_bits(value: int) -> int:
    # Считаем количество нулевых битов с помощью функции bin(),
    # которая возвращает строку с двоичным представлением числа
    return bin(value).count('0')  # вычитаем 1, так как самый левый бит всегда равен 0

# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
# def pack_4_4(first: int, second: int) -> int:
#    return ...

def pack_4_4(first: int, second: int) -> int:
    # Проверяем, что оба числа помещаются в 4 бита
    if first > 0b1111 or second > 0b1111:
        raise ValueError("Both values should fit into 4 bits")
    # Сдвигаем второе число на 4 бита влево и складываем с первым
    return (second << 4) | first

# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
# def unpack_4_4(first: int, second: int) -> int:
# Я НЕ ПОНИМАЮ ЗАДАЧУ, НАВЕРНОЕ ТУТ НЕВЕРНО ПОСТАВЛЕННАЯ ЗАДАЧА, ИМЕЛО БЫ СМЫСЛ ИЗ ОДНОГО ЧИСЛА НАДО СДЕЛАТЬ 2, поэтому я решаю переформулированную задачу
# def unpack_4_4(num: int) -> Tuple[int, int]:
#    return ...

def unpack_4_4(num: int) -> Tuple[int, int]:
    first = num & 0b00001111  # Mask to extract the 4 least significant bits
    second = (num & 0b11110000) >> 4  # Mask to extract the 4 most significant bits and shift them to the right
    return first, second

# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
# т.е. вывести значение нижней границы, если число меньше или вывести значение верхней границы, если число больше
# def clamp(value: float, low: float, high: float) -> float:
#    return ...

def clamp(value: float, low: float, high: float) -> float:
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
#def clamp_any(value: float, low: float, high: float) -> float:
#    return ...

def clamp_any(value: float, low: float, high: float) -> float:
    if low > high:
        print("Lower bound cannot be greater than upper bound")
        return None
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
# def event_and_match_interval_m10_10(value: int) -> bool:
#     return ...

def event_and_match_interval_m10_10(value: int) -> bool:
    if value % 2 != 0 and -10 <= value <= 10:
        return True
    else:
        return False

# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
# def reverse_operations(value: float):
#     return value ** 4 * 0.5 + 0.25
# 1. value ** 4 - возведение в 4ую степень
# 2. умножение на 0.5
# 3. сложение с 0.25

def reverse_operations(value: float):
    # выполняем операции в порядке 3 -> 2 -> 1, а т.е.:
    return ((value + 0.25) * 0.5) ** 0.25

# Установить n-ый бит числа в единицу.
# def set_nth_bit(value: int, n: int) -> int:
#   return ...

def set_nth_bit(value: int, n: int) -> int:
    mask = 1 << n
    return value | mask

# Переключить n-ый бит числа.
# def switch_nth_bit(value: int, n: int) -> int:
#    return ...

def switch_nth_bit(value: int, n: int) -> int:
    mask = 1 << n
    return value ^ mask

# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
# def change_priorities(x: float) -> float:
#    return x + 3 ** 3

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
# def int_to_float(value: int) -> float:
#    return ...


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
# def min_raw(first: int, last: int) -> int:
#    return ...

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("# home task 1: add_mul(10.0, 5.0)")
    result = add_mul(10.0, 5.0)
    print(result)

    print("# home task 2: div_int_rem(10.0, 5.0)")
    result = div_int_rem(10.0, 5.0)
    print(result)

    print("# home task 3: xor_swap(10, 5)")
    result = xor_swap(10, 5)
    print(result)

    print("# home task 4: min_conditional(10, 5)")
    result = min_conditional(10, 5)
    print(result)

    print("# home task 5: x = 10")
    x = 10
    print(f"{x} * 2 = {mul_shift_2_8_32(x)[0]}")
    print(f"{x} * 8 = {mul_shift_2_8_32(x)[1]}")
    print(f"{x} * 32 = {mul_shift_2_8_32(x)[2]}")

    print("# home task 6: x = 320")
    x = 320
    print(f"{x} / 2 = {div_shift_2_8_32(x)[0]}")
    print(f"{x} / 8 = {div_shift_2_8_32(x)[1]}")
    print(f"{x} / 32 = {div_shift_2_8_32(x)[2]}")

    print("# home task 7: exponentiation(10, 3, 2)")
    result = exponentiation(10, 3, 2)
    print(result)

    print("# home task 8: sign(-10)")
    result = sign(-10)
    print(result)

    print("# home task 9: change_sign(-10)")
    result = change_sign(-10)
    print(result)

    print("# home task 10:")
    num1 = 0b00000010  # all even bits are 0, so the result should be false
    num2 = 0b00000011  # one even bit is 1, so the result should be true
    num3 = 0b00000101  # two even bits are 1, so the result should be true
    print("check_32_even_bit_set(0b00000010) is " + str(check_32_even_bit_set(num1)))  # False
    print("check_32_even_bit_set(0b00000011) is " + str(check_32_even_bit_set(num2)))  # True
    print("check_32_even_bit_set(0b00000101) is " + str(check_32_even_bit_set(num3)))  # True

    print("# home task 11:")
    print("calculate_32_zero_bits(0b01010101010101010101010101010101) is " + str(calculate_32_zero_bits(0b01010101010101010101010101010101))) # 16
    print("calculate_32_zero_bits(0b101010101010101) is " + str(calculate_32_zero_bits(0b0101010101010101))) # 8

    print("# home task 12:")
    print("pack_4_4(1, 2) is " + str(pack_4_4(1, 2)))

    print("# home task 13:")
    print("0b1100 is " + str(0b1100))
    print("0b1101 is " + str(0b1101))
    print("unpack_4_4(0b11001101) is " + str(unpack_4_4(0b11001101)))

    print("# home task 14:")
    print("1 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp(1, 5, 10)))
    print("5 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp(5, 5, 10)))
    print("7 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp(7, 5, 10)))
    print("10 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp(10, 5, 10)))
    print("15 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp(15, 5, 10)))
    print("5 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp(15, 5, 10)))
    print("10 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp(15, 5, 10)))
    print("15 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp(15, 5, 10)))
    print("15 is the number, 15 is low threshold and 10 is high threshold, so the result is " + str(clamp(15, 15, 10)))

    print("# home task 15:")
    print("1 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(1, 5, 10)))
    print("5 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(5, 5, 10)))
    print("7 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(7, 5, 10)))
    print("10 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(10, 5, 10)))
    print("15 is the number, 5 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(15, 5, 10)))
    print("5 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(15, 5, 10)))
    print("10 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(15, 5, 10)))
    print("15 is the number, 10 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(15, 5, 10)))
    print("15 is the number, 15 is low threshold and 10 is high threshold, so the result is " + str(clamp_any(15, 15, 10)))

    print("# home task 16:")
    print("event_and_match_interval_m10_10(-55), so the result is " + str(event_and_match_interval_m10_10(-55)))
    print("event_and_match_interval_m10_10(5), so the result is " + str(event_and_match_interval_m10_10(5)))
    print("event_and_match_interval_m10_10(55), so the result is " + str(event_and_match_interval_m10_10(55)))

    print("# home task 17:")
    print("reverse_operations(31.75), so the result is " + str(reverse_operations(31.75)))

    print("# home task 18:")
    print("#set_nth_bit(0b0001, 2), so the result should be 0b0101, i.e. " + str(set_nth_bit(0b0001, 2)))
    print("#set_nth_bit(0b0001, 3), so the result should be 0b1001, i.e. " + str(set_nth_bit(0b0001, 3)))

    print("# home task 19:")
    print("#switch_nth_bit(0b1111, 1), so the result should be 0b1101, i.e. " + str(switch_nth_bit(0b1111, 1)))
    print("#switch_nth_bit(0b1111, 3), so the result should be 0b0111, i.e. " + str(switch_nth_bit(0b1111, 3)))

    print("# home task 20:")
    print("change_priorities(0) calculates (x + 3) ** 3, so the result is  " + str(change_priorities(0)))
    print("change_priorities(1) calculates (x + 3) ** 3, so the result is  " + str(change_priorities(1)))
    print("change_priorities(2) calculates (x + 3) ** 3, so the result is  " + str(change_priorities(2)))

