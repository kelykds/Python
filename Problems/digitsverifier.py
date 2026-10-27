k = int(input("Digite o CPF (apenas números): "))
digits = []
def numseparator(k):
    while (k > 10):
        dig = k - (k % 10)
        digits.append(dig)
        k = (k - dig) / 10

def verificador(k):
    #tem 11 digitos? (não quero ter solicitar todo separado)
    numseparator(k)
    qtdedig = len(digits)
    if qtdedig != 11:
        print("Número inválido: deve conter 11 dígitos.")
        return 1
    else: #tem todos os dígitos iguais?
        if digits[0] == digits[1] and digits[0] == digits[2] and digits[0] == digits[3] and digits[0] == digits[4] and digits[0] == digits[5] and digits[0] == digits[6] and digits[0] == digits[7] and digits[0] == digits[8]:
            return 2
        else:
            c1 = (digits[10] * 10) + (digits[9] * 9) + (digits[8] * 8) + (digits[7] * 7) + (digits[6] * 6) + (digits[5] * 5) + (digits[4] * 4) + (digits[3] * 3) + (digits[2] * 2)
            c2 = (digits[10] * 11) + (digits[9] * 10) + (digits[8] * 9) + (digits[7] * 8) + (digits[6] * 7) + (digits[5] * 6) + (digits[4] * 5) + (digits[3] * 4) + (digits[2] * 3) + (digits[1] * 2)

            q1 = c1 % 11
            q2 = c2 % 11
            if q1 < 2 and digits[1] == 0:
                if (q2 < 2 and digits[0] == 0) or (q2 >= 2 and digits[0] == 11-q2):
                    return True
                else: 
                    return False
            elif digits[1] == 11-q1:
                if (q2 < 2 and digits[0] == 0) or (q2 >= 2 and digits[0] == 11-q2):
                    return True
                else: 
                    return False


if verificador(k) == True:
    print("O CPF é válido. A pessoa física é de: ")
    if digits[2] == 0:
        print("RS\n")
    elif digits[2] == 1:
        print("DF, GO, MS, MT ou TO\n")
    elif digits[2] == 2:
        print("AC, AM, AP, PA, RO ou RR\n")
    elif digits[2] == 3:
            print("CE, MA ou PI\n")
    elif digits[2] == 4:
        print("AL, PB, PE ou RN\n")
    elif digits[2] == 5:
        print("BA ou SE\n")
    elif digits[2] == 6:
        print("MG\n")
    elif digits[2] == 7:
        print("ES ou RJ\n")
    elif digits[2] == 8:
        print("SP\n")
    elif digits[2] == 9:
        print("PR ou SC\n")
else:
    print("O CPF digitado é invalido.")