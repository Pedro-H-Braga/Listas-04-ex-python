'''
Faça um programa que solicite ao usuário uma frase e substitua todos os espaços por _ 
(underline/sublinhado). O programa deverá exibir a frase original e a frase após as substituições.

- pegar entrada
- ver seu tamanho
- variaveis: entrada, contador, percorre_string, tamanho_string

varre a string. ao varrer:
condição que se 'espaço em branco' em string substitua por '_'
'''
entrada = input("informe algo: ")

string_nova = entrada.replace(' ', '_')
print('antiga entrada: ' + entrada+', nova entrada: '+string_nova)