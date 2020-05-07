# cores no terminal
"""sempre que quiser representar uma cor em python você começa com \033[style;text;background m"""
#\033[0;33;44m
#style 0 (none) 1 (bold) 4 (underline) 7 (negative)
#text 30 (white) 31 (red) 32 (green) 33(yellow) 34(blue) 35 (purple) 36 (ciano) 37(gray)
#back 40 (white) 41 (red) 42 (green) 43(yellow) 44(blue) 45 (purple) 46 (ciano) 47(gray)
print("\033[1;30;41mTeste!\033[m")
a = 3
b = 5
print('Os valores são \033[1;30;41m{}\033[m e \033[1;30;41m{}\033[m!!!!'.format(a , b))
print('Os valores são {}{}{} e {}{}{}!!!!!'.format('\033[1;30;41m', a , '\033[m', '\033[1;30;41m', b , '\033[m'))
cores = {'limpa': '\033[m',
         'azul':"\033[34m",
         "amarelo":'\033[33m'}
print("Os valores são {}{}{} e {}{}{}".format(cores["amarelo"],a,b, cores['limpa']))
