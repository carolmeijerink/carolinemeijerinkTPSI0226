

def listar_reservas(lista):
    if not lista:
        print("Nenhuma reserva encontrada.")
        return
    else:
        print("\n--- LISTA DE RESERVAS ---")

    for res in lista:
        print(f"ID: {res.id} | Nome: {res.nome_completo} | NIF: {res.nif} | Email: {res.email} | Check-in: {res.data_checkin} | Check-out: {res.data_checkout}")


def pesquisa_linear_nome(lista, nome_procurado):
    resultados = []
    for r in lista:        
        if nome_procurado.lower() in r.nome_completo.lower():
            resultados.append(r)
    return resultados


def ordenar_por_id_bubble(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j].id > lista[j+1].id:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def pesquisa_binaria_id(lista, id_procurado):
    lista_ordenada = ordenar_por_id_bubble(lista)
    inicio = 0
    fim = len(lista_ordenada) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista_ordenada[meio].id == id_procurado:
            return lista_ordenada[meio]
        elif lista_ordenada[meio].id < id_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1  
    return None

def calcular_estatisticas(lista):
    if not lista:
        return
    
    total_reservas = len(lista)
    print(f"\nTotal de reservas: {total_reservas}")