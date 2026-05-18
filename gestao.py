

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


def eliminar_reserva(lista, id_procurado):
    for res in lista:
        if res.id == id_procurado:
            print(f"Reserva encontrada: ID {res.id} | Nome: {res.nome_completo}")
            confirmacao = input("Tem certeza que deseja eliminar esta reserva? (S/N): ").upper()
            if confirmacao == 'S':
                lista.remove(res)
                print("Reserva eliminada com sucesso.")
                return True
            else:
                print("Eliminação cancelada pelo utilizador.")
                return False
    print("A reserva com o ID especificado não foi encontrada.")

def editar_reserva(lista, id_procurado, func_validar_nif, func_validar_email):
    for res in lista:
        if res.id == id_procurado:
            print("\n--- DADOS ATUAIS DA RESERVA ---")
            print(f"1. Nome: {res.nome_completo}")
            print(f"2. NIF: {res.nif}")
            print(f"3. E-mail: {res.email}")
            print(f"4. Cancelar edição")

            opcao = input("\nO que deseja alterar? (1-4): ")

            if opcao == "1":
                novo_nome = input("Novo Nome Completo: ")
                if novo_nome.strip():
                    res.nome_completo = novo_nome
                    print("Nome atualizado com sucesso!")
                    return True
            
            elif opcao == "2":
                while True:
                    novo_nif = input("Novo NIF: ")
                    if func_validar_nif(novo_nif):
                        res.nif = novo_nif
                        print("NIF atualizado com sucesso!")
                        return True
                        
            
            elif opcao == "3":
                while True:
                    novo_email = input("Novo E-mail: ")
                    if func_validar_email(novo_email):
                        res.email = novo_email
                        print("E-mail atualizado com sucesso!")
                        return True
                        
            
            elif opcao == "4":
                print("Edição cancelada.")
                return False
            else:
                print("Opção inválida.")
            return False
    
    print("Reserva não encontrada.")
    return False



