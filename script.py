import random

size = int(input('tamanho da senha:'))
lowchar_ok = str(input('letras minusculas [s]im, [n]ão: '))
upchar_ok = str(input('letras maiusculas [s]im, [n]ão: '))
num_ok = str(input('numero [s]im, [n]ão: '))
jokeychar_ok = str(input('caracteres especiais [s]im, [n]ão: '))

upchar = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowchar = str('abcdefghijklmnopqrstuvwxyz')
num = str('1234567890')
jokeychar = str('!@#$%¨&*()')

def senha():
    if (size <= 0 or lowchar_ok =='n' and num_ok == "n" and upchar_ok == "n" and jokeychar_ok == "n"):
        return "ERRO... Sua senha deve conter ao menos um caracter valido."

    elif (lowchar_ok =='s' and upchar_ok == "n" and num_ok == "n" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar)
    elif (lowchar_ok =='n' and upchar_ok == "s" and num_ok == "n" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(upchar)
    elif (lowchar_ok =='n' and upchar_ok == "n" and num_ok == "s" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(num)
    elif (lowchar_ok =='n' and upchar_ok == "n" and num_ok == "n" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(jokeychar)
    elif (lowchar_ok =='s' and upchar_ok == "s" and num_ok == "n" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar + upchar)
    elif (lowchar_ok =='s' and upchar_ok == "s" and num_ok == "s" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar + upchar + num)
    elif (lowchar_ok =='s' and upchar_ok == "s" and num_ok == "s" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar + upchar + num + jokeychar)
    elif (lowchar_ok =='n' and upchar_ok == "s" and num_ok == "s" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(upchar + num + jokeychar) 
    elif (lowchar_ok =='n' and upchar_ok == "n" and num_ok == "s" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(num + jokeychar)
    elif (lowchar_ok =='s' and upchar_ok == "n" and num_ok == "n" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar + jokeychar) 
    elif (lowchar_ok =='n' and upchar_ok == "s" and num_ok == "n" and jokeychar_ok == "s"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(upchar + jokeychar)
    elif (lowchar_ok =='s' and upchar_ok == "n" and num_ok == "s" and jokeychar_ok == "n"):
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(lowchar + num)
    else:
        senha = ""
        while len(senha) != size:
            senha = senha + random.choice(upchar + num)
    if len(senha) == size:
        return "Password: %s" % senha
print(senha())
