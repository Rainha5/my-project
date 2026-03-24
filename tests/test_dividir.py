import pytest
from functions.dividir import dividir

def test_dividir_normal():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)