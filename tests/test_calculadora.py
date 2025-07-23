from src.calculadora import string_calculator

def test_empty_string_returns_zero():
    assert string_calculator("") == 0

def cadena_unica():
    assert string_calculator("2") == "2"

def varios_valores():
    assert string_calculator("2,1") == 3