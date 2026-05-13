
from reserva import Reserva
from validacoes import validar_email, validar_data, validar_nif
from datetime import datetime
from persistencia import guardar_reservas, carregar_reservas
import gestao

def menu ():
    base_de_dados_reservas = carregar_reservas()
    while True:
        print("\n--- MENU ---")
        print("1. Nova reserva")
        print("2. Listar reservas")
        print("3. Pesquisar reserva por nome")
        print("4. Pesquisar reserva por ID")
        print("5. Ordenar por ID")
        print("6. Estatísticas de reservas")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            

            print ("\nBem-vindo ao Hotel XPTO!")

            while True:   
                print ("\nPor favor, preencha seus dados para realizar a reserva:\n")
                nome_completo = input("Nome completo: ")
                
                while True:
                    nif = input("NIF: ")
                    if validar_nif(nif):
                        break
                
                
                while True:
                    email = input("E-mail: ")
                    if validar_email(email):
                        break
                
                
                while True:
                    data_checkin = input("Data de checkin (dd/mm/aaaa): ")
                    if validar_data(data_checkin):
                        break
                
                
                while True:
                    data_checkout = input("Data de checkout (dd/mm/aaaa): ")
                    if validar_data(data_checkout):
                        d1 = datetime.strptime(data_checkin, "%d/%m/%Y")
                        d2 = datetime.strptime(data_checkout, "%d/%m/%Y")

                        if d2 > d1:
                            break

                        else:
                            print("Erro: A data de checkout deve ser posterior à data de checkin.")

            
                
                try:
                    nova_reserva = Reserva(nome_completo, nif, email, data_checkin, data_checkout)
                    base_de_dados_reservas.append(nova_reserva)
                    nova_reserva.exibir_detalhes()
                    print("\nReserva registada com sucesso!")

                except Exception as e:
                    print(f"Lamentamos, ocorreu um erro ao criar reserva: {e}. Por favor, tente novamente.")
                
                print("\nDeseja realizar outra reserva? (S/N)")

                resposta = input().upper()
                if resposta != "S":
                    break


            # for res in base_de_dados_reservas:
            #     res.exibir_detalhes()

            print("\nDeseja guardar as reservas em um ficheiro antes de sair? (S/N)")
            if(input().upper() == "S"):
                guardar_reservas(base_de_dados_reservas)

            
        

        elif escolha == "2":
            gestao.listar_reservas(base_de_dados_reservas)
        
        elif escolha == "3":
            nome_procurado = input("Digite o nome para pesquisa: ")
            resultados = gestao.pesquisa_linear_nome(base_de_dados_reservas, nome_procurado)
            gestao.listar_reservas(resultados)
       
        elif escolha == "4":
            try:
                id_procurado = int(input("Digite o ID para pesquisa: "))
                resultado = gestao.pesquisa_binaria_id(base_de_dados_reservas, id_procurado)
                if resultado:
                    resultado.exibir_detalhes()
                else:
                    print("Reserva não encontrada.")
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")
        
        elif escolha == "5":
            base_de_dados_reservas = gestao.ordenar_por_id_bubble(base_de_dados_reservas)
            print("\nReservas ordenadas por ID com sucesso!")
            gestao.listar_reservas(base_de_dados_reservas)
        
        elif escolha == "6":
            gestao.calcular_estatisticas(base_de_dados_reservas)

        elif escolha == "7":
            print("\nObrigado por usar o Hotel XPTO! Até breve!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__": #lembrar: este if garante que o menu só será executado se este arquivo for o principal, e não se ele importado para outro sem eu querer
    menu()