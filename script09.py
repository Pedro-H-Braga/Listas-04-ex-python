'''
Faça um programa que emule o jogo da forca. O programa terá uma constante chamada
PALAVRA_CHAVE que armazenara a palavra a ser descoberta. O programa deverá solicitar ao usuário
as letras e à medida que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou
não. O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de
ser enforcado

VARIAVEIS:
palavra_chave
tamanho_palavra
acertos
erros
falta_quanto

LÓGICA:
fazer laço que pegue entradas até completar a palavra e que se diferente da letra da palavra pegue o contador e some mais um
até completar 6, se chegar em 6 saia do laço. 
Quando pegar as entradas, varrer a string palavra_chave verificando se tem alguma letra informado que tem na palavra_chave,
se sim, conte mais um para acertos e mostre quantas letras faltam para completar a palavra, 
se não conte mais um para erros e mostre quantos erros já tem.
Deixar todas as letras minuscula depois da entrada


'''
