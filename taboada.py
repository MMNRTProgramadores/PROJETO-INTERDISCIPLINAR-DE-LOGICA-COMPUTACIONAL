from time import sleep
#~~~~~~~~~~~~~
print('\033[1;mFeito por: Rafael\033[m')
sleep(1.5)
print('\x1b[2J\x1b[1;1H')
#~~~~~~~~~~~~~
while True:
    n=int(input('\033[1;36mQual taboada voce deseja consultar? \033[m'))
    c=0
    c1=0
    c2=0
    c3=0
    print('\033[1;32m_____ADIÇÃO_______\033[m')
    for c in range(0,10):
        c=c+1
        m=c+n
        print(f'\033[1;33m{c} + {n} = {m}\033[m')
        sleep(0.10)
    print('\033[1;32m_____SUBTRAÇÃO_______\033[m')

    for c1 in range(0,10):
        c1=c1+1
        m1=c1-n
        print(f'\033[1;33m{c1} - {n} = {m1}\033[m')
        sleep(0.10)
    print('\033[1;32m______MULTIPLICAÇÃO_______\033[m')

    for c2 in range(0,10):
        c2=c2+1
        m2=c2*n
        print(f'\033[1;33m{c2} * {n} = {m2}\033[m')
        sleep(0.10)
    print('\033[1;32m_____DIVISÃO_______\033[m')

    for c3 in range(0,10):
        c3=c3+1
        m3=c3/n
        print(f'\033[1;33m{c3} / {n} = {m3:.2f}\033[m')
        sleep(0.10)
    exit=str(input('\033[1;34mDeseja sair(S/N)? \033[m'))
    if exit=='S'or exit=='s':
        break
print('\033[4;32m-----------FIM--------------\033[m')
