"""
hacer el algoritmo burbuja
"""

#entrada

def ingresar_valores() -> str:
    lista_valor = [ ]
    valor = input("Ingrese un valor (Ingrese un input vacío cuando quieras parar): ")
    while valor != "":
        lista_valor.append(valor)
        valor = input("Ingrese un valor (Ingrese un input vacío cuando quieras parar): ")
    if comprobar_si_todos_los_elementos_son_del_mismo_tipo(lista_valor):
        return lista_valor    
        



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


def aplicar_burbuja(lista_a_ordenar:list):
    for iteracion_padre in range(len(lista_a_ordenar)-1):
        for iteracion_hijo in range(len(lista_a_ordenar)-1-iteracion_padre):
            if lista_a_ordenar[iteracion_hijo] > lista_a_ordenar[iteracion_hijo+1]:
                lista_a_ordenar[iteracion_hijo] , lista_a_ordenar[iteracion_hijo+1] = lista_a_ordenar[iteracion_hijo+1] , lista_a_ordenar[iteracion_hijo]
    return lista_a_ordenar

#salida

def mostrar_lista_ordenada(lista_ordenada:list)->str:
    return f"La lista de elementos ordenadas queda así: {lista_ordenada}"

if __name__ == "__main__":
    lista_valores = ingresar_valores()
    lista_ordenada = aplicar_burbuja(lista_valores)
    resultado = mostrar_lista_ordenada(lista_ordenada)
    
    print(resultado)