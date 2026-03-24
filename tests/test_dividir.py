import pytest
from functions.dividir import dividir

def test_dividir_normal():
    assert dividir(10, 2) == 5
