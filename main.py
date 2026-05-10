
from reserva import Reserva
from validacoes import validar_email, validar_data, validar_nif
from datetime import datetime

base_de_dados_reservas = []
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
        
        