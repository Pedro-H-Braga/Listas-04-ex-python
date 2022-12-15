'''
ASSUNTO DE STRINGS:

resolução:
- fazer a string ocorrer um 'split' que separe as palavras e seja possível contar as vogais
- fazer laço que identifique as vogais nas strings 
- fazer um contador para contar as aparições no laço

ANDAR PELA STRING:
var = '0123456789'
x = var[0:3:2]
RESPOSTA: X=012

Fazer um laço que ande do inicio ao fim da
'''
# teste string
entrada = 'opa digai meu bom, quão á de ser'
letra = ''
# contador de vogais
contador = 0
vogais = 'aeiouáéíóúãõâêîôû'
# transformar as entradas em minusculo para não ter divergencia na contagem
entrada = entrada.lower()

#while letra in entrada:
if letra in vogais:
        contador += 1

print(f"A palavra '{entrada}' tem {contador} vogais.".format(entrada, contador))


