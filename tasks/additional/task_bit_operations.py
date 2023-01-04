'''
Дополнительное задание.
Битовые операции.
'''

from typing import Sequence

import colorama

colorama.init()

BASE_COLOR: str = colorama.Fore.GREEN
DIFF_COLOR: str = colorama.Fore.LIGHTYELLOW_EX
ERASE_COLOR: str = colorama.Fore.LIGHTRED_EX


# Вспомогательный метод. Форматирует число в битовом представлении.
def binary(value: int, number_of_bits: int = 8) -> str:
    return format((((1 << number_of_bits) - 1) & value), 'b').zfill(number_of_bits)


# Вспомогательный метод. Подсвечивает разницу значений.
def print_values(values: Sequence[int], result: int, number_of_bits: int = 8):
    for index, value in enumerate(values):
        print(f'{colorize_diff([binary(value), *list(map(binary, [*values, result]))])} (value {index + 1})')
    print(f'{colorize_diff([binary(result), *list(map(binary, values))])} (result of operation)')


def print_shifted_values(value1: int, value2: int, result: int, shift: str = 'left'):
    value1 = binary(value1)
    result = binary(result)
    if shift == 'left':
        print(f'{ERASE_COLOR}{value1[:value2]}{BASE_COLOR}{value1[value2:]}{colorama.Style.RESET_ALL} << {value2}')
        print(f'{BASE_COLOR}{result[:len(result) - value2]}{DIFF_COLOR}{result[len(result) - value2:]}'
              f'{colorama.Style.RESET_ALL} (result)')
    else:
        print(f'{BASE_COLOR}{value1[:len(value1) - value2]}{ERASE_COLOR}{value1[len(value1) - value2:]}'
              f'{colorama.Style.RESET_ALL} >> {value2}')
        print(f'{BASE_COLOR}{result[:value2]}{DIFF_COLOR}{result[value2:]}{colorama.Style.RESET_ALL} (result)')


def print_masked_values(value1: int, value2: int, result: int):
    def colorize_using_mask(value: str, mask: str):
        return ''.join(f'{BASE_COLOR if m == "0" else DIFF_COLOR}{v}' for v, m in zip(value, mask)) + f'{colorama.Style.RESET_ALL}'

    value1 = binary(value1)
    value2 = binary(value2)
    result = binary(result)
    print(colorize_using_mask(value1, value2) + ' (value)')
    print(colorize_using_mask(value2, value2) + ' (mask)')
    print(colorize_using_mask(result, value2) + ' (result)')


def colorize_diff(values: Sequence[str], base_color: str = BASE_COLOR, diff_color: str = DIFF_COLOR) -> str:
    marks = list(map(lambda x: len(set(x)) == 2, zip(*values)))
    return ''.join(map(lambda marked: f'{diff_color if marked[1] else base_color}{marked[0]}{colorama.Style.RESET_ALL}',
                       zip(values[0], marks)))


def main():
    # Битовое НЕ. Рассмотрите реализацию операции "битовое НЕ". Раскомментируйте нижеприведенный код,
    # поэкспериментируйте со следующими значениями и отметьте, что все биты изменяются на противоположные:
    # - установите значение value в 0x00;
    # - установите значение value в 0x01;
    # - установите значение value в 0x02;
    # - установите значение value в 0x10;
    # - установите значение value в 0xff;
    # - установите значение value в 0x55.
    # value = 0x00
    # result = ~value
    # print_values([value], result)

    # Битовое И. Рассмотрите реализацию операции "битовое И". Раскомментируйте нижеприведенный код,
    # поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0x01 и value2 в 0xff;
    # - установите значение value1 в 0x81 и value2 в 0x00;
    # - установите значение value1 в 0x81 и value2 в 0xff;
    # - установите значение value1 в 0x55 и value2 в 0x00;
    # - установите значение value1 в 0x55 и value2 в 0xff;
    # - установите значение value1 в 0xff и value2 в 0x0f;
    # - установите значение value1 в 0xff и value2 в 0xf0.
    # Отметьте, что в результате выполнения оператора "битовое И" выставляются только те биты,
    # которым соответствуют единичные биты в обоих исходных значениях.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 & value2
    # print_values([value1, value2], result)

    # Битовое ИЛИ. Рассмотрите реализацию операции "битовое ИЛИ". Раскомментируйте нижеприведенный код,
    # поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00 и value2 в 0xff;
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0x81 и value2 в 0x00;
    # - установите значение value1 в 0x55 и value2 в 0x00;
    # - установите значение value1 в 0x55 и value2 в 0xaa.
    # Отметьте, что в результате выполнения оператора "битовое ИЛИ" выставляются те биты,
    # которым соответствует хотя бы один единичный бит в любом из исходных значений.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 | value2
    # print_values([value1, value2], result)

    # Исключающее ИЛИ (сложение по модулю 2). Рассмотрите реализацию операции "исключающее ИЛИ".
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00 и value2 в 0x00;
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0xff и value2 в 0x00;
    # - установите значение value1 в 0x00 и value2 в 0xff;
    # - установите значение value1 в 0x55 и value2 в 0x00;
    # - установите значение value1 в 0x55 и value2 в 0xff;
    # - установите значение value1 в 0x55 и value2 в 0xaa.
    # Отметьте, что в результате выполнения оператора "исключающее ИЛИ" выставляются только те биты,
    # которым соответствуют различные биты в исходных значениях, то есть 1 и 0 дают 1, а 0 и 0 или 1 и 1
    # дают 0.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 ^ value2
    # print_values([value1, value2], result)

    # Сдвиг влево. Рассмотрите реализацию операции "сдвиг влево".
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0x01 и value2 в 0x01;
    # - установите значение value1 в 0x03 и value2 в 0x02;
    # - установите значение value1 в 0x70 и value2 в 0x01;
    # - установите значение value1 в 0x70 и value2 в 0x02;
    # - установите значение value1 в 0xff и value2 в 0x04.
    # Отметьте, что в результате выполнения оператора "сдвиг влево" исходное значение в двоичном представлении
    # просто сдвигается на заданное количество бит. Сдвиг влево на 1 бит соответствует умножению на 2.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 << value2
    # print_shifted_values(value1, value2, result)

    # Сдвиг вправо. Рассмотрите реализацию операции "сдвиг вправо".
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0x01 и value2 в 0x01;
    # - установите значение value1 в 0x03 и value2 в 0x01;
    # - установите значение value1 в 0x70 и value2 в 0x01;
    # - установите значение value1 в 0x70 и value2 в 0x02;
    # - установите значение value1 в 0xff и value2 в 0x04;
    # - установите значение value1 в -1 и value2 в 0x04.
    # Отметьте, что в результате выполнения оператора "сдвиг вправо" исходное значение в двоичном представлении
    # просто сдвигается на заданное количество бит. Если число отрицательное, то результат дополняется единицами.
    # Если число неотрицательное, то результат дополняется нулями. По сути знаком числа.
    # Сдвиг вправо на 1 бит соответствует делению на 2.
    # value1 = -1
    # value2 = 0x02
    # result = value1 >> value2
    # print_shifted_values(value1, value2, result, shift='right')

    # Формирование единичной битовой маски.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value в 0x00;
    # - установите значение value в 0x01;
    # - установите значение value в 0x04;
    # - установите значение value в 0x07.
    # Отметьте, что для формирования единичной маски используется сдвиг единицы влево на заданное число позиций.
    # value = 0x00
    # result = 1 << value
    # print(f'{binary(result)}')

    # Формирование битовой маски.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00 и value2 в 0x02;
    # - установите значение value1 в 0x00 и value2 в 0x07;
    # - установите значение value1 в 0x02 и value2 в 0x06;
    # - установите значение value1 в 0x01 и value2 в 0x07.
    # Обратите внимание на алгоритм формирования маски и попытайтесь в нем разобраться.
    # def mask(start: int, end: int) -> int:
    #     return ((1 << (end - start + 1)) - 1) << start
    #
    # value1 = 0x00
    # value2 = 0x00
    # result = mask(value1, value2)
    # print(f'{binary(result)}')

    # Проверка битов.
    # Для проверки (тестирования) установленных (единичных) битов используется маска и операция битовое И.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0xff и value2 в 0x01;
    # - установите значение value1 в 0xff и value2 в 0x02;
    # - установите значение value1 в 0xff и value2 в 0x04;
    # - установите значение value1 в 0x00 и value2 в 0xff;
    # - установите значение value1 в 0xff и value2 в 0x0f;
    # - установите значение value1 в 0xff и value2 в 0xf0;
    # - установите значение value1 в 0x55 и value2 в 0x0f;
    # - установите значение value1 в 0xc3 и value2 в 0x3c;
    # - установите значение value1 в 0xc4 и value2 в 0x3c.
    # Обратите внимание на то, что по сути проверка битов с помощью маски вырезает из исходного значения биты,
    # соответствующие маске. Далее это значение может быть преобразовано к булевому типу и если хотя бы один бит
    # установлен в единицу, то результат будет равен True.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 & value2
    # print_masked_values(value1, value2, result)
    # print(bool(result))

    # Установка битов.
    # Для установки битов используется маска и операция битовое ИЛИ.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00 и value2 в 0x01;
    # - установите значение value1 в 0x00 и value2 в 0x32;
    # - установите значение value1 в 0xff и value2 в 0x55;
    # - установите значение value1 в 0x00 и value2 в 0xa5;
    # - установите значение value1 в 0x55 и value2 в 0x0f;
    # - установите значение value1 в 0x0f и value2 в 0xf0;
    # - установите значение value1 в 0x55 и value2 в 0x0f.
    # Обратите внимание на то, что независимо от исходного значения биты, соответствующие маске, устанавливаются
    # в единичное значение.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 | value2
    # print_masked_values(value1, value2, result)

    # Инверсия битов.
    # Для инверсии битов используется маска и операция исключающее ИЛИ.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00 и value2 в 0x01;
    # - установите значение value1 в 0x01 и value2 в 0x00;
    # - установите значение value1 в 0x31 и value2 в 0x30;
    # - установите значение value1 в 0xff и value2 в 0x55;
    # - установите значение value1 в 0xaa и value2 в 0xff;
    # - установите значение value1 в 0x5a и value2 в 0xa5;
    # - установите значение value1 в 0x55 и value2 в 0x0f;
    # - установите значение value1 в 0xff и value2 в 0xf0;
    # - установите значение value1 в 0xff и value2 в 0xff.
    # Обратите внимание на то, что инвертируются все биты, соответствующие маске.
    # value1 = 0x00
    # value2 = 0x00
    # result = value1 ^ value2
    # print_masked_values(value1, value2, result)

    # Битовые поля.
    # Для доступа к битовым полям используются маски и операции сдвига.
    # В качестве примера будет использоваться 16-битное значение с полями длиной 4, 3 и 9 бит.
    # Раскомментируйте нижеприведенный код, поэкспериментируйте со следующими значениями и оцените результат:
    # - установите значение value1 в 0x00, value2 в 0x00 и value3 в 0x00;
    # - установите значение value1 в 0x01, value2 в 0x02 и value3 в 0x03;
    # - установите значение value1 в 0x1ff, value2 в 0x07 и value3 в 0x03.
    # Обратите внимание, что битовые представления отдельных полей (помеченных различными цветами) совпадают
    # с битовыми представлениями отдельных чисел.
    # red: str = colorama.Fore.LIGHTRED_EX
    # blue: str = colorama.Fore.LIGHTBLUE_EX
    # magenta: str = colorama.Fore.LIGHTMAGENTA_EX
    # value1 = 0x1ff
    # value2 = 0x06
    # value3 = 0x03
    # result = (value1 & 0b0000000111111111) | ((value2 & 0b00001111) << 9) | ((value3 & 0b00000111) << 13)
    # value1 = binary(value1, 9)
    # value2 = binary(value2, 4)
    # value3 = binary(value3, 3)
    # result = binary(result, 16)
    # print(f'{red}{value1}{colorama.Style.RESET_ALL} (1st value - [0:8] bits)')
    # print(f'{blue}{value2}{colorama.Style.RESET_ALL} (2nd value - [9:12] bits)')
    # print(f'{magenta}{value3}{colorama.Style.RESET_ALL} (3rd value - [13:15] bits)')
    # print(f'{magenta}{result[:3]}{blue}{result[3:7]}{red}{result[7:]}{colorama.Style.RESET_ALL} (result)')

    ...


main()
