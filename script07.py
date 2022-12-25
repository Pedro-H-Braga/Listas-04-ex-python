'''
entrada = input('informe uma palavra: ')
contador = 0
guarda_palavra_anterior = ''
tamanho_entrada = len(entrada) 
entrada = entrada[::-1]

contador = tamanho_entrada
while contador >= 0:
    percorre_entrada = entrada[contador:tamanho_entrada]
    print(percorre_entrada[::-1])
    contador -= 1

'''
variavel         = '1234567890'
tamanho_variavel = len(variavel)
contador = 1
contador_invertido = tamanho_variavel
while contador_invertido >= 0:
        print(variavel[0:contador_invertido])
        contador_invertido -= 1
        
        if contador_invertido == 0:
            print(percorre_variavel[::-1])
            contador_invertido += 1