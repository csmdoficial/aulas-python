'''MANIPULANDO CADEIAS DE TEXTO
Para o python toda cadeia de texto simples está entre aspas
frase = "curso em video python"
o python vai colocar esses dados na memoria do computador, ele vai separar a frase por cada letra
incluindo espaços em branco
OPERAÇÕES
-FATIAMENTO:
frase[9] = vai mostrar a casa 9 que seria o V
frase[9:14] = vai pegar a parte video da frase
frase[9:21] = Video python
frase[9:21:2] = V D O P T O
frase[:5] = começa do caractere 0 'Curso em Vídeo'
frase[15:] = começa no caractere 15 'python'
frase[9::3] = começa no 9 e pula de 3 em 3 'VePh'
-ANALISAR
len(frase) = comprimento da frase , len = lense que é comprimento em ingles
frase.count('o') = contar quantas vezes aparece a letra o minuscula
frase.count('o',0,13) = vai contar quantos o tem até a caractere 12
frase.find('deo') = vai contar quantas vezes ele encontrou a frase deo dizendo a posição que começou
frase.find('Android') = vai retornar o valor -1 pq nao esta na frase
'curso' in frase = existe a palavra curso na frase? se tiver vai retornar true
-TRANSFORMAÇÃO
frase.replace('Python','Android') = ele vai procurar a frase python e vai substituir por android
frase.upper() = vai colocar a frase em maiuscula
frase.lower() = vai colocar a frase em minusculas
frase.capitalize() = vai jogar todos os caracteres pra minusculos, mas so o primeiro caractere
vai ser maiusculo
frase.title() = vai analisar quantas palavras tem e colocar letra maiuscula em toda letra inicial
de frase
frase.strip() = vai remover todos os espaços inuteis no inicio e no final da string
(necessario para cadastro de dados quando alguem coloca espaço antes de um nome
frase.rstrip() = vai remover todos os espaços inuteis na direita
frase.lstrip() = vai remover todos os espaços inuteis na esquerda
-DIVISÃO
frase.split() vai ocorrer um divisão onde tiver espaços na sua frase e entao cada uma dessas
palavras vai ser colocada em um outra lista
- JUNÇÃO'-'.join(frase) = juntar todos os elementos de frase e colocar 0 _ nos espaços
'''
frase = "Curso em video Python"
print(frase)
print(frase[3])
print(frase[:13])
print(frase[0:14])
print(frase[::2])
print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), 
lower(), capitalize(), title(), strip(), junção com join().""")
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase)
'''para substituir para sempre'''
frase = frase.replace('Python' , 'Android')
print(frase)
print(frase.lower().find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])


