
class Reserva:
    
    contador_id = 1
    
    def __init__ (self, nome_completo, nif, email, data_checkin, data_checkout):
        self.id = Reserva.contador_id
        Reserva.contador_id += 1
        
        self.nome_completo = nome_completo
        self.nif = nif
        self.email = email
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        
    def exibir_detalhes(self):
        print(f"\nID da Reserva: {self.id}")
        print(f"Nome do hóspede: {self.nome_completo}")
        print(f"NIF: {self.nif}")
        print(f"E-mail: {self.email}")
        print(f"Data de checkin: {self.data_checkin}")
        print(f"Data de checkout: {self.data_checkout}")
        
        print("-" * 20)

base_de_dados_reservas = []
print ("\nBem-vindo ao Hotel XPTO!")

while 1==1:   
    print ("\nPor favor, preencha seus dados para realizar a reserva:\n")
    nome_completo = input("Nome completo: ")
    nif = input("NIF: ")
    email = input("E-mail: ")
    data_checkin = input("Data de checkin (dd/mm/aaaa): ")
    data_checkout = input("Data de checkout (dd/mm/aaaa): ")

    nova_reserva = Reserva(nome_completo, nif, email, data_checkin, data_checkout)
    base_de_dados_reservas.append(nova_reserva)
    nova_reserva.exibir_detalhes()
    print("\nReserva registada com sucesso!")

    print("\nDeseja realizar outra reserva? (S/N)")

    resposta = input().upper()
    if resposta != "S":
        break


# for res in base_de_dados_reservas:
#     res.exibir_detalhes()
        
        