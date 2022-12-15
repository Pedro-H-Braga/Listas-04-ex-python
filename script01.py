'''
ASSUNTO DE STRINGS:

resolução:
- fazer a string ocorrer um 'split' que separe as palavras e seja possível contar as vogais
- fazer laço que identifique as vogais nas strings 
- fazer um contador para contar as aparições no laço
'''
# teste string
entrada = 'opa digai meu bom, quão á de ser'
# contador de vogais
contador = 0
vogais = 'aeiouáéíóúãõâêîôû'
# transformar as entradas em minusculo para não ter divergencia na contagem
entrada = entrada.lower()

if vogais in entrada:
    contador += 1
    print(vogais)

print(contador)


