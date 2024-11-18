import pytest
from main import sumar, masgrande

def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(-1, -1) == -2

def test_masgrande():
    assert masgrande(2, 1) == True
    assert masgrande(1, 2) == False
    assert masgrande(2, 2) == False
    assert masgrande(-1, -2) == True