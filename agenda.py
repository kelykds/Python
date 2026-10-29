agenda = {}

conf = input("Olá! Deseja guardar contatos? (y/n) ")
if conf == 'y':
    num = input("Há um número específico de contatos? (y/n) ")
    if num == 'y':
        qtdec = input("Quantos contatos deseja guardar? ")
        i = 0
        while i < qtdec:
                    nome = input("Nome: ")
                    telefone = input("Telefone: ")
                    agenda[nome] = telefone
                    i = i + 1

    elif num == 'n':
        while True:
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda[nome] = telefone
            cont = input("Deseja continuar?(y/n) ")
            if cont == 'n':
                 break
            elif cont == 'y':
                 continue
    else:
        print("Opção não encontrada.")