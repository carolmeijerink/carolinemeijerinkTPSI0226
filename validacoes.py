# validar e-mail, data e nif inseridos


import re #biblioteca Regular Expressions, contém expressões regulares para validar o formato do e-mail e da data
from datetime import datetime #para fazer todas as validações necessárias relativamente à data


def validar_nif(nif):
    if nif.isdigit() and len(nif) == 9:
        return True
    else:
        print("Erro: O NIF deve conter exatamente 9 dígitos, apenas numéricos. Por favor, insira um NIF válido, como no exemplo: 123456789")
        return False

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    
    else:
        print("Erro: O formato do e-mail inserido é inválido. Por favor, insira um e-mail válido, como no exemplo: nome@dominio.com")
        return False

def validar_data(data_texto):
    padrao = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(padrao, data_texto):
        print("Erro: O formato da data inserida é inválido. Por favor, insira a data no formato DD/MM/AAAA, como no exemplo: 25/12/2024")
        return False
    
    try:

        data_objeto = datetime.strptime(data_texto, "%d/%m/%Y")
        hoje = datetime.now()
        if data_objeto < hoje:
            print("Erro: A data inserida é anterior à data atual. Por favor, insira uma data futura.")
            return False
        else:
            return True
        
    except ValueError:
        print("Erro: A data inserida não existe. Por favor, insira uma data válida, como no exemplo: 25/12/2024")
        return False


  






