
texto = input('Digite a mensagem a ser encriptada ou decifrada: ') # Solicitando o texto a ser encriptado ou decriptado:
chave = int(input('Entre com o valor da chave (deslocamento): ')) # Chave a ser utilizada
modo = input('Escolha C para cifrar ou D para decifrar o texto: ') # Determinar modo de operação (E = encriptar; D = decriptar)
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Conjunto de caracteres válidos no algoritmo
convertido = '' # Variável para armazenar o texto criptografado (ou decifrado)
texto = texto.upper() # Converter todo o texto em maiúsculas:
modo = modo.upper() # Converter todo o modo em maiúsculas:

def encrypt(message):
    m =''
    for c in message:
        if c in alfabeto:
            c_index=alfabeto.index(c)
            m += alfabeto[(c_index + chave) % len(alfabeto)]
        else:
            m += c
    return m
    
def decrypt(message):
    m =''
    for c in message:
        if c in alfabeto:
            c_index=alfabeto.index(c)
            m += alfabeto[(c_index - chave) % len(alfabeto)]
        else:
            m += c
    return m

if modo == 'C':
    print (encrypt(texto))
elif modo == 'D':
    print (decrypt (texto))
else:
    print ('Não conheço esse comando')