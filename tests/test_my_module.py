import pytest
from functions.my_module import calcular_media, obter_elemento


def test_media_normal():
    assert calcular_media([2, 4, 6]) == 4


def test_media_lista_vazia():
    assert calcular_media([]) == 0


def test_obter_elemento_valido():
    assert obter_elemento([10, 20, 30], 1) == 20


def test_obter_elemento_invalido():
    with pytest.raises(IndexError):
        obter_elemento([1, 2, 3], 5)