k_str = input("Digite o CPF (apenas números): ")
digits = []

def numseparator(k):
    for char in k:
        digits.append(int(char))

def verificador(k):
    #tem 11 digitos? (não quero ter solicitar todo separado)
    numseparator(k)
    qtdedig = len(digits)
    if len(k) != 11:
        print("Número inválido: deve conter 11 dígitos.")
        return False

    numseparator(k)

    if digits[0] == digits[1] and digits[0] == digits[2] and digits[0] == digits[3] and digits[0] == digits[4] and digits[0] == digits[5] and digits[0] == digits[6] and digits[0] == digits[7] and digits[0] == digits[8] and digits[0] == digits[9] and digits[0] == digits[10]:
        return False
    else:
        c1 = (digits[0] * 10) + (digits[1] * 9) + (digits[2] * 8) + (digits[3] * 7) + (digits[4] * 6) + (digits[5] * 5) + (digits[6] * 4) + (digits[7] * 3) + (digits[8] * 2)
        q1 = c1 % 11
        
        if q1 < 2:
            digito1_calculado = 0
        else:
            digito1_calculado = 11 - q1
        
        c2 = (digits[0] * 11) + (digits[1] * 10) + (digits[2] * 9) + (digits[3] * 8) + (digits[4] * 7) + (digits[5] * 6) + (digits[6] * 5) + (digits[7] * 4) + (digits[8] * 3) + (digits[9] * 2)
        q2 = c2 % 11
        
        if q2 < 2:
            digito2_calculado = 0
        else:
            digito2_calculado = 11 - q2

        if digits[9] == digito1_calculado and digits[10] == digito2_calculado:
            return True
        else:
            return False


if verificador(k_str) == True:
    print("O CPF é válido. A pessoa física é de: ")
    regiao = digits[8]
    if regiao == 0:
        print("RS\n")
    elif regiao == 1:
        print("DF, GO, MS, MT ou TO\n")
    elif regiao == 2:
        print("AC, AM, AP, PA, RO ou RR\n")
    elif regiao == 3:
            print("CE, MA ou PI\n")
    elif regiao == 4:
        print("AL, PB, PE ou RN\n")
    elif regiao == 5:
        print("BA ou SE\n")
    elif regiao == 6:
        print("MG\n")
    elif regiao == 7:
        print("ES ou RJ\n")
    elif regiao == 8:
        print("SP\n")
    elif regiao == 9:
        print("PR ou SC\n")
else:
    print("O CPF digitado é invalido.")