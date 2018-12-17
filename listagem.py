li=str('LISTAGEM DE PRODUTOS!').center(30)
linha='-'*len(li)
l=( 'lapis',0.75,
    'borracha',1.75,
    'caneta',1.25,
    'caderno',10.25,
    'estojo',5.0,
    'mochila',115.00,
    'branquinho',3.50,
    'regua',2.0,
    'marca-texto',2.50,
    'apontador',1.80,
    'lapis de cor',6.0)

print(f'\033[1;33m{linha}\033[m')
print(f'\033[1;32m{li}\033[m')
print(f'\033[1;33m{linha}\033[m')
for pos in range(0,len(l)):
    if pos % 2 == 0:
        print(f'\033[1m{l[pos]:.<30}',end='')
    else:
        print(f'R${l[pos]:.>7}\033[m')
