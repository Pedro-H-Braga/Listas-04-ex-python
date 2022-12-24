'''
Faça um programa que receba uma palavras e imprima essa palavra na vertical (em escada).
Exemplo: Ao ser informada a palavra NATAL, o programa imprime conforme poder ser visto abaixo:
N
NA
NAT
NATA
NATAL

fazer laço que exibe posição por posição até chegar na posição final
'''
entrada = 'natal'
contador = 0
tamanho_entrada = len(entrada) 
while contador < tamanho_entrada:
    contador += 1
    percorre_entrada = entrada[contador::tamanho_entrada]
    print(percorre_entrada)
