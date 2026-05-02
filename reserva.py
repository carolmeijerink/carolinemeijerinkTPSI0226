
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

