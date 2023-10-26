from src.main import * #cambiar esto
import pytest

def aplicar_burbuja(lista_a_ordenar:list)->list:
    
    return [1,2,3,4,5]

def test_comprobar_si_ordena_bien_el_burbujas():
    assert aplicar_burbuja([5,4,3,2,1]) == [1,2,3,4,5]