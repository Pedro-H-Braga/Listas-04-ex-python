'''
ASSUNTO DE STRINGS:

resolução:
- fazer a string ocorrer um 'split' que separe as palavras e seja possível contar as vogais
- fazer laço que identifique as vogais nas strings 
- fazer um contador para contar as aparições no laço

ANDAR PELA STRING:
var = '0123456789'
x = var[0:3:2] 0 a 3 pulando de dois em dois
RESPOSTA: X=012

Fazer um laço que ande do inicio ao fim da

pegar o tamanho da palavra com len() e 
fazer while que seja verdadeiro até contador (que vai percorrer a string até ser menor que o tamanho da palavra)

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

print(f"A palavra '{entrada}' tem {contador} vogais.")


