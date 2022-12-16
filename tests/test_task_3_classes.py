from tasks.task_3_classes import (
    Millimeters,
    Centimeters,
    Meters,
    Kilometers,
    Inches,
    Feets,
    Yards,
    Miles,
    Fen,
    Chi,
    In
)


def test_equality():
    assert Millimeters(1000000.0) == Centimeters(100000.0) == Meters(1000.0) == Kilometers(1.0)
    assert Inches(63360.0) == Feets(5280.0) == Yards(1760.0) == Miles(1.0)
    assert Fen(1.0) == Chi(100.0) == In(10000.0)
    assert Inches(1.0) == Millimeters(25.4)
    assert Fen(1.0) == Millimeters(10.0 / 3.0)


def test_string_representation():
    assert str(Millimeters(10.0)) == '10.0 mm'
    assert str(Centimeters(15.1)) == '15.1 cm'
    assert str(Meters(20.2)) == '20.2 m'
    assert str(Kilometers(25.3)) == '25.3 km'
    assert str(Inches(1.51)) == '1.51 in'
    assert str(Feets(2.635)) == '2.635 ft'
    assert str(Yards(3.58)) == '3.58 yd'
    assert str(Miles(2.1)) == '2.1 mi'
    assert str(Fen(4.55)) == '4.55 fen'
    assert str(Chi(2.155)) == '2.155 chi'
    assert str(In(8.7)) == '8.7 in'


def test_compare():
    assert Millimeters(10.0) < Centimeters(2.0) < Meters(0.03) < Kilometers(0.01)
    assert Inches(10.0) < Feets(1.0) < Yards(0.5) < Miles(0.01)
    assert Fen(100.0) < Chi(2.0) < In(0.5)
    assert Millimeters(10.0) < Inches(1.0) < Fen(10.0)


def test_sum():
    assert Millimeters(1.0) + Centimeters(1.0) + Meters(1.0) + Kilometers(1.0) == Millimeters(1001011.0)
    assert Inches(1.0) + Feets(1.0) + Yards(1.0) + Miles(1.0) == Inches(63409.0)
    assert Fen(1.0) + Chi(1.0) + In(1.0) == Fen(10101.0)
    assert Millimeters(1.0) + 1.0 == Millimeters(2.0)
    assert Inches(10.0) + 5.0 == Inches(15.0)
    assert Fen(100.0) + 1.5 == Fen(101.5)


def test_sub():
    assert Kilometers(1.0) - Meters(1.0) - Centimeters(1.0) - Millimeters(1.0) == Millimeters(998989.0)
    assert Miles(1.0) - Yards(1.0) - Feets(1.0) - Inches(1.0) == Inches(63311.0)
    assert In(1.0) - Chi(1.0) - Fen(1.0) == Fen(9899.0)
    assert Millimeters(1.0) - 1.0 == Millimeters(0.0)
    assert Inches(10.0) - 5.0 == Inches(5.0)
    assert Fen(100.0) - 1.5 == Fen(98.5)


def test_mul():
    assert Millimeters(10.0) * 2 == Millimeters(20.0)
    assert Centimeters(10.0) * 2 == Centimeters(20.0)
    assert Meters(10.0) * 2 == Meters(20.0)
    assert Kilometers(10.0) * 2 == Kilometers(20.0)
    assert Inches(10.0) * 2 == Inches(20.0)
    assert Feets(10.0) * 2 == Feets(20.0)
    assert Yards(10.0) * 2 == Yards(20.0)
    assert Miles(10.0) * 2 == Miles(20.0)
    assert Fen(10.0) * 2 == Fen(20.0)
    assert Chi(10.0) * 2 == Chi(20.0)
    assert In(10.0) * 2 == In(20.0)


def test_div():
    assert Millimeters(10.0) / 2 == Millimeters(5.0)
    assert Centimeters(10.0) / 2 == Centimeters(5.0)
    assert Meters(10.0) / 2 == Meters(5.0)
    assert Kilometers(10.0) / 2 == Kilometers(5.0)
    assert Inches(10.0) / 2 == Inches(5.0)
    assert Feets(10.0) / 2 == Feets(5.0)
    assert Yards(10.0) / 2 == Yards(5.0)
    assert Miles(10.0) / 2 == Miles(5.0)
    assert Fen(10.0) / 2 == Fen(5.0)
    assert Chi(10.0) / 2 == Chi(5.0)
    assert In(10.0) / 2 == In(5.0)

    assert Kilometers(1.0) / Millimeters(1.0) == 1000000.0
    assert Miles(1.0) / Inches(1.0) == 63360.0
    assert In(1.0) / Fen(1.0) == 10000.0


def test_conversion():
    assert Millimeters(Meters(1.5)) == Millimeters(1500.0)
    assert Millimeters(Inches(1.0)) == Millimeters(25.4)
    assert Kilometers(Miles(1.0)) == Kilometers(1.609344)
    assert Meters(In(1.0)) == Meters(100.0 / 3.0)
