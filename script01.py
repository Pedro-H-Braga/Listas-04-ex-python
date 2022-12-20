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




LÓGICA 2 COM WHILE:
- pegar o tamanho da palavra com len() e 
- fazer while que seja verdadeiro até contador_string (que vai percorrer a string até ser menor que o tamanho da palavra)
- condição para percorrer a string 0 -> tamanho final, e ao percorrer, se achar uma vogal contador_vogais recebe +1 
'''

# string para teste
entrada = 'opa digai meu bom, quão á de ser'
# contador vogal 
contador_vogais = 0
vogais = 'a'
# contador string)
contador_string = 0
percorre_string = ''
tamanho_string = len(entrada)
# transformar as entradas em minusculo para não ter divergencia na contagem
entrada = entrada.lower()

# while que vai varrer a string até o tamanho maxímo dela
while contador_string < tamanho_string:
    
    percorre_string = entrada[contador_string:tamanho_string]
    if vogais in percorre_string:
        contador_vogais += 1
        contador_string += 1
    else:
        contador_string += 1

print(f"Tem {contador_vogais} vogais na palavra: {entrada}")
#print(f"A palavra '{entrada}' tem {contador} vogais.")