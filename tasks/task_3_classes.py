
#Задание 3.
#Классы. Наследование, волшебные методы.


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
    ratio = 1.0
    label = ""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} {self.label}"

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            return self.value == other.to_base_unit().value
        return self.value == other * self.ratio

    def __lt__(self, other):
        if isinstance(other, LengthUnits):
            return self.value < other.to_base_unit().value
        return self.value < other * self.ratio

    def __add__(self, other):
        if isinstance(other, LengthUnits):
            return self.__class__(self.value + other.to_base_unit().value / self.ratio)
        return self.__class__(self.value + other)

    def __iadd__(self, other):
        if isinstance(other, LengthUnits):
            self.value += other.to_base_unit().value / self.ratio
        else:
            self.value += other
        return self

    def __sub__(self, other):
        if isinstance(other, LengthUnits):
            return self.__class__(self.value - other.to_base_unit().value / self.ratio)
        return self.__class__(self.value - other)

    def __isub__(self, other):
        if isinstance(other, LengthUnits):
            self.value -= other.to_base_unit().value / self.ratio
        else:
            self.value -= other
        return self

    def __mul__(self, other):
        return self.__class__(self.value * other)

    def __imul__(self, other):
        self.value *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, LengthUnits):
            return self.value / other.to_base_unit().value * other.ratio / self.ratio
        return self.__class__(self.value / other)

    def itruediv(self, other):
        if isinstance(other, LengthUnits):
            self.value /= other.to_base_unit().value / self.ratio
        else:
            self.value /= other
        return self

    def to_base_unit(self):
        return self.__class__(self.value * self.ratio)


class Millimeters:
    ratio = 1.0
    label = "мм"


class Centimeters:
    ratio = 10.0
    label = "см"


class Meters:
    ratio = 1000.0
    label = "м"


class Kilometers:
    ratio = 1000000.0
    label = "км"


class Inches:
    ratio = 25.4
    label = "дюйм"


class Feets:
    ratio = 304.8
    label = "фут"


class Yards:
    ratio = 914.4
    label = "ярд"


class Miles:
    ratio = 1609343.9
    label = "миля"


class Fen:
    ratio = 3.33333
    label = "фэнь"


class Chi:
    ratio = 33.3333
    label = "чи"


class In:
    ratio = 333.333
    label = "инь"
