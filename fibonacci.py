print('')
msg=str('SEQUÊNCIA DE FIBONACCI!').center(45)
l='*'*len(msg)
print(f'\033[1m{l}\033[m')
print(f'\033[1;34m{msg}\033[m')
print(f'\033[1m{l}\033[m')
#~~~~~~~~~~~~
while True:
    print('')
    pros=input('\033[1;36mDeseja Continuar(S/N)?  \033[m')
    if pros.upper=='S' or pros=='s':
        print('')
        n = int(input('\033[1;35mQuantos termos você quer mostrar? \033[m'))
        t1=0
        t2=1
        print('')
        print(f'\033[1m{t1}\033[m\033[1;32m ->\033[m \033[1m{t2}\033[m', end='')   
        cont=3
        while cont<=n:
            t3 = t1+t2
            print(f'\033[1;32m->\033[m \033[1m{t3}\033[m',end='')
            t1 = t2
            t2 = t3
            cont += 1
        print('')
        print('\033[1;33m...FIM!\033[m')
    else:
        print('')
        print('\033[1;31mPrograma encerrado!\033[m')
        break
