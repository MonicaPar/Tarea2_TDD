from src.calculadora import string_calculator

def test_empty_string_returns_zero():
    assert string_calculator("") == 0
