"""
hacer el algoritmo burbuja
"""

#entrada

#procesado
def comprobar_si_todos_los_elementos_son_del_mismo_tipo(lista_a_comprobar:list)->bool:
    """comprobar si todos los elementos son del mismo tipo

    Args:
        lista_a_comprobar (list): recibe una lista que será la que haya que comprobar

    Raises:
        ValueError: Si todos los elementos no son iguales saltará un ValueError

    Returns:
        bool: Si todos los elementos son iguales devolverá true, como confirmación de que todo está bien
    """
    
    tipo_elemento_lista = type(lista_a_comprobar[0])
    if all(isinstance(elemento, tipo_elemento_lista) for elemento in lista_a_comprobar):
        return True
    else:
        raise ValueError("No todos los elementos son del mismo tipo:")



#salida

if __name__ == "__main__":
    print()