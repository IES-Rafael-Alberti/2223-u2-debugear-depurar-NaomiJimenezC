import pytest

def aplicar_burbuja(lista_a_ordenar:list)->list:
    
    return [1,2,3,4,5]

def test_comprobar_si_ordena_bien_el_burbujas():
    assert aplicar_burbuja([5,4,3,2,1]) == [1,2,3,4,5]
    

a = [5,4,3,2,1]
#analizalo luego
for iteracion_padre in range(len(a)-1):
    for iteracion_hijo in range(len(a)-1-iteracion_padre):
        if a[iteracion_hijo] > a[iteracion_hijo+1]:
            a[iteracion_hijo] , a[iteracion_hijo+1] = a[iteracion_hijo+1] , a[iteracion_hijo]
print(a)