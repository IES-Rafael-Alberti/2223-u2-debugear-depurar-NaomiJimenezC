from src.main import * #cambia esto luego
import pytest




def test_saber_si_los_elementos_de_una_lista_son_enteros():
    assert comprobar_si_todos_los_elementos_son_del_mismo_tipo([1,2,3,4,5]) == True

def test_saber_si_los_elementos_de_una_lista_son_string():
    assert comprobar_si_todos_los_elementos_son_del_mismo_tipo(["a","b","c"]) == True

def test_saber_si_los_elementos_de_una_lista_no_son_del_mismo_tipo():
    with pytest.raises(ValueError):
     comprobar_si_todos_los_elementos_son_del_mismo_tipo(["a","b",2])
