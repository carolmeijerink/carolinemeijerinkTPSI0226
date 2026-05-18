import json
import os #interação com o sistema operativo

from reserva import Reserva


nome_ficheiro = "reservas.json"

def guardar_reservas(lista_reservas):
    try:
        dados_para_guardar = [vars(r) for r in lista_reservas]

        with open(nome_ficheiro, 'w', encoding='utf-8') as f:
            json.dump(dados_para_guardar, f, indent=4, ensure_ascii=False)
            print("Reservas guardadas com sucesso.")

    except Exception as e:
        print(f"Erro ao guardar as reservas: {e}")

def carregar_reservas():
    if not os.path.exists(nome_ficheiro):
        print("Nenhum ficheiro de reservas encontrado. Iniciando com uma lista vazia.")
        Reserva.contador_id = 1
        return []
    
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            lista_objetos = []
            max_id = 0

            for d in dados:
                res = Reserva(d['nome_completo'], d['nif'], d['email'], d['data_checkin'], d['data_checkout'])
                res.id = d['id']
                lista_objetos.append(res)

                if d['id'] > max_id:
                    max_id = d['id']

            Reserva.contador_id = max_id + 1
            return lista_objetos
        
    except Exception as e:
        print(f"Erro ao carregar as reservas: {e}")
        return []