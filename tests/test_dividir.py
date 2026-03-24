import pytest
from functions.dividir import dividir

def test_dividir_normal():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_dividir_resultado_errado():
    assert dividir(10, 2) == 6  

def test_dividir_negativos():
    assert dividir(-10, 2) == 10  

def test_dividir_por_zero_errado():
    assert dividir(10, 0) == 0 