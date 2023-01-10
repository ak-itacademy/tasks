'''
Задание 3.
Классы. Наследование, волшебные методы.
'''

from typing import Union

# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.

# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.

# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.

# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.

# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.

# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.

# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.

# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    UNIT_NAME: str = "Length Units"
    CONVERSION_RATE: float = 0.0

    def __init__(self, value: Union[float, "LengthUnits"]):
        self.__value = float(value) * self.CONVERSION_RATE if type(value) in (int, float) else value.value

    def __eq__(self, another: "LengthUnits"):
        return self.value == another.value

    def __lt__(self, another: "LengthUnits"):
        return self.value < another.value

    def __add__(self, another: Union[float, "LengthUnits"]):
        result = self.__value + another * self.CONVERSION_RATE if type(another) in (int, float) \
            else self.__value + another.value
        return globals().get(type(self).__name__, None)(result / self.CONVERSION_RATE)

    def __iadd__(self, another: Union[float, "LengthUnits"]):
        self.__value += another * self.CONVERSION_RATE if type(another) in (int, float) else another.value
        return self

    def __sub__(self, another: Union[float, "LengthUnits"]):
        result = self.__value - another * self.CONVERSION_RATE if type(another) in (int, float) \
            else self.__value - another.value
        return globals().get(type(self).__name__, None)(result / self.CONVERSION_RATE)

    def __isub__(self, another: Union[float, "LengthUnits"]):
        self.__value -= another * self.CONVERSION_RATE if type(another) in (int, float) else another.value
        return self

    def __mul__(self, value: float):
        result = self.__value * value
        return globals().get(type(self).__name__, None)(result / self.CONVERSION_RATE)

    def __imul__(self, value: float):
        self.__value *= value
        return self

    def __truediv__(self, another: Union[float, "LengthUnits"]):
        result = self.__value / another if type(another) in (int, float) else self.__value / another.value
        return globals().get(type(self).__name__, None)(result / self.CONVERSION_RATE) \
            if type(another) in (int, float) else result

    def __idiv__(self, another: Union[float, "LengthUnits"]):
        self.__value /= another if type(another) in (int, float) else another.value
        return self if type(another) in (int, float) else self.value

    def __str__(self):
        return f"{self.value / self.CONVERSION_RATE} {self.UNIT_NAME}"

    @property
    def value(self):
        return self.__value


class Millimeters(LengthUnits):
    UNIT_NAME: str = "mm"
    CONVERSION_RATE: float = 1

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Centimeters(LengthUnits):
    UNIT_NAME: str = "cm"
    CONVERSION_RATE: float = 10

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Meters(LengthUnits):
    UNIT_NAME: str = "m"
    CONVERSION_RATE: float = 1000

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Kilometers(LengthUnits):
    UNIT_NAME: str = "km"
    CONVERSION_RATE: float = 1000_000

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Inches(LengthUnits):
    UNIT_NAME: str = "in"
    CONVERSION_RATE: float = 25.4

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Feets(LengthUnits):
    UNIT_NAME: str = "ft"
    CONVERSION_RATE: float = 304.8

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Yards(LengthUnits):
    UNIT_NAME: str = "yd"
    CONVERSION_RATE: float = 914.4

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Miles(LengthUnits):
    UNIT_NAME: str = "mi"
    CONVERSION_RATE: float = 1_609_344

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Fen(LengthUnits):
    UNIT_NAME: str = "fen"
    CONVERSION_RATE: float = 3.33

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class Chi(LengthUnits):
    UNIT_NAME: str = "chi"
    CONVERSION_RATE: float = 333

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)


class In(LengthUnits):
    UNIT_NAME: str = "in"
    CONVERSION_RATE: float = 33_300

    def __init__(self, value: Union[float, "LengthUnits"]):
        super().__init__(value)
