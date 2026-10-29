agenda = {}

def guardarctt():
     nome = input("Nome: ")
     contato = input("Telefone/Email: ")
     agenda[nome] = contato

conf = input("Olá! Deseja guardar contatos? (y/n) ")
if conf == 'y':
    num = input("Há um número específico de contatos? (y/n) ")
    if num == 'y':
        qtdec = int(input("Quantos contatos deseja guardar? "))
        i = 0
        while i < qtdec:
                    guardarctt()
                    i = i + 1

    elif num == 'n':
        while True:
            guardarctt()
            cont = input("Deseja continuar?(y/n) ")
            if cont == 'n':
                 break
            
    else:
        print("Opção não encontrada.")