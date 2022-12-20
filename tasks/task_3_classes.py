'''
Задание 3.
Классы. Наследование, волшебные методы.
'''

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

    def __init__(self, value: float or "LengthUnits", conversion_rate: float):
        self.__conversion_rate = float(conversion_rate)
        self.__value = float(value if isinstance(value, float) or isinstance(value, int) else
                             value.value() * value.conversion_rate() / self.conversion_rate())

    def __eq__(self, another: "LengthUnits"):
        return self.value() * self.conversion_rate() == another.conversion_to_base_unit()

    def __lt__(self, another: "LengthUnits"):
        return self.value() * self.conversion_rate() < another.conversion_to_base_unit()

    def __add__(self, another):
        self.__value += (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self

    def __iadd__(self, another):
        self.__value += (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self

    def __sub__(self, another):
        self.__value -= (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self

    def __isub__(self, another):
        self.__value -= (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self

    def __mul__(self, value):
        self.__value *= value
        return self

    def __imul__(self, value):
        self.__value *= value
        return self

    def __truediv__(self, another):
        self.__value /= (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self if another is isinstance(another, float) or isinstance(another, int) else self.value()

    def __idiv__(self, another):
        self.__value /= (another if isinstance(another, float) or isinstance(another, int) else
                         another.conversion_to_base_unit() / self.conversion_rate())
        return self if another is isinstance(another, float) or isinstance(another, int) else self.value()

    def value(self) -> float:
        return self.__value

    def set_value(self, value: float):
        self.__value = float(value)

    def conversion_rate(self) -> float:
        return self.__conversion_rate

    def conversion_to_base_unit(self):
        return self.value() * self.conversion_rate()


class Millimeters(LengthUnits):
    UNIT_NAME: str = "Millimeters"

    def __init__(self, value: float or "LengthUnits", conversion_rate=1):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} mm"


class Centimeters(LengthUnits):
    UNIT_NAME: str = "Centimeters"

    def __init__(self, value: float or "LengthUnits", conversion_rate=10):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} cm"


class Meters(LengthUnits):
    UNIT_NAME: str = "Meters"

    def __init__(self, value: float or "LengthUnits", conversion_rate=1000):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} m"


class Kilometers(LengthUnits):
    UNIT_NAME: str = "Kilometers"

    def __init__(self, value: float or "LengthUnits", conversion_rate=1000000):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} km"


class Inches(LengthUnits):
    UNIT_NAME: str = "Inches"

    def __init__(self, value: float or "LengthUnits", conversion_rate=25.4):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f'{value} in'


class Feets(LengthUnits):
    UNIT_NAME: str = "Feets"

    def __init__(self, value: float or "LengthUnits", conversion_rate=304.8):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} ft"


class Yards(LengthUnits):
    UNIT_NAME: str = "Yards"

    def __init__(self, value: float or "LengthUnits", conversion_rate=914.4):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} yd"


class Miles(LengthUnits):
    UNIT_NAME: str = "Miles"

    def __init__(self, value: float or "LengthUnits", conversion_rate=1_609_344):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} mi"


class Fen(LengthUnits):
    UNIT_NAME: str = "Fen"

    def __init__(self, value: float or "LengthUnits", conversion_rate=3.33):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} fen"


class Chi(LengthUnits):
    UNIT_NAME: str = "Chi"

    def __init__(self, value: float or "LengthUnits", conversion_rate=333):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} chi"


class In(LengthUnits):
    UNIT_NAME: str = "In"

    def __init__(self, value: float or "LengthUnits", conversion_rate=33_300):
        super().__init__(value, conversion_rate)

    def __str__(self):
        value = self.value()
        return f"{value} in"
