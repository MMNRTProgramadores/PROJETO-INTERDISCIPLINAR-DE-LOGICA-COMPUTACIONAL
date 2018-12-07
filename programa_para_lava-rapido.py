#DSENVOLVEDORES: RAFAEL ANJOS & NATAM.
#ANALISTAS: TIAGO SERAFIM, MIGUEL E MARIA LUIZA.
#projeto interdisciplinar dirigido por Wagner lops águiar(vulgo "Ninja")
#PYTHON_3
print('\033[1;33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
from time import sleep
#biblioteca de tempo
print("""
	█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
	█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
	█░░║║║╠─║─║─║║║║║╠─░░█
	█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
	█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
#foi ultilizado 3 aspas duplas pois elas pegam o texto mesmo dando quebra de linha
manual=input("""\033[1;32mDeseja abrir o manual de instrução
(S/N)? \033[m""")
if manual.upper()=='S':
	#upper deixa tudo que o usuário digitar, maiúsculo.
	print("""\033[1;33m<<<MANUAL DE INSTRUÇÕES>>>
Caso você digite 1, você será direcionado para o programa de cálculo de gasto de água por mês, no qual você irá digitar quantos litros de água você gasta para lavar um carro e em seguida quantos carros você lava em média por dia.
------------------------------------------
Caso você digite 2, você será direcionado para o programa de pacote de serviços do lava-rápido, no qual haverá as opções bronze, prata e ouro, todas com suas especificações e lreços mostradas na tabela. Você terá de selecionar digitando o nome do pacote, ex: ouro.
-----------------------------------------
Caso você digite 3, você será direcionado para o controle de fila, no qual aparrcerá se você quer continuar, caso diga sim, o programa pedirá para você pressionar enter para tirar a sua senha, e em seguida perguntará se você quer continuar, e assim sucessivamente.
------------------------------------------
Caso você digite 4, você será direcionado para o programa de entrega em domicílio, no qual você informará quantas vezes deseja ultilizar o programa e em seguida você preencherá as informações requeridas que por sua vez irão aparecer todas juntas na tela.
-------------------------------------------
Caso você digite 5, você será direcionado para o programa de compra de produtos e brindes do lava-rápido,no qual terá alguns produtos e brindes listados por números, e você poderá escolher  um produto de cada vez apenas digitando o número do produto que se encontrará antes do nome do dele, e caso queira escolher mais basta dizer sim após escolher um produto.
-----------------------------------------
Caso queira sair do programa digite 0 e em seguida pressione enter.
\033[m""")
while True:
	print("""\033[1;35mQual dos programas abaixo você deseja ultilizar?
[0]- Para sair do programa.
[1]- Cálculo de Litros de água gastos por mês.
[2]- Pacotes de serviços.
[3]- Controle de fila.
[4]- Entregas em domicílio.
[5]- Opção para compra de produtos.
-=-=-=-=--=-=-=-=-\033[m""")
	try:
	#try é o inicio de uma excessão que ocorrerá. Ex: caso o usuário digitar algo que não seja número(int)
		select=int(input('\033[1;35mQual sua escolha:  \033[m'))	
		if select==1:
		#if é o mesmo que "se"
			print('\033[1;33m○~~~~~~《INICIO》~~~~~~○\033[m')
			litros=float(input("""\033[1;36mQuantos litros de água são gastos para
lavar um carro?\033[m """))
			#a declaração da variavel como float, significa que ela permite numeros quebrados. Ex: 2.5
			print('\033[1;36.....\033[m')
			carros=int(input("""\033[1;36mQuantos carros são lavados em média
por dia?\033[m """))
			media=int(litros*carros*30)
			print('\033[1;36.....\033[m')
			print('\033[1;36mVocê gasta em média {} litros por mês.'.format(media))
			print('\033[1;33m○~~~~~~~~{FIM}~~~~~~~~○\033[m')
		elif select==2:
			print('\033[1;34m☆~~~~~~[INICIO]~~~~~~☆ \033[m')
			print('\033[1;33mESCOLHA UM DOS PACOTES ABAIXO:\033[m ')
			print("""\033[1;36m
      <<<!PACOTES!>>>\033[m 	
\033[7;36m_____________________________________ 
|\033[1;36m   CONTÉM:      |BRONZE|PRATA |OURO |
|lavagem normal  |•sim• |•sim• |•sim•|
|brilho no pneu  |•não• |•sim• |•sim•|
|limpeza do motor|•não• |•não• |•sim•|
|Lavagem em casa |•não• |•não• |•sim•|\033[m""")
			print('\033[1;36mVALORES:         |R$ 15 |R$ 30 |R$ 50|\033[m')
			pacote=str(input("""\033[1;33mEscolha seu pacote
(bronze,prata,ouro): """))
			if pacote.upper()=='BRONZE':
				print('')
				#print sem nada dentro além de aspas serve para deixar espaço entre as linhas
				print('Você escolheu o pacote BRONZE🌟, Parabéns!') 
				print('-=-' *20)
			elif pacote.upper()=='PRATA':
				print('') 
				print('Você escolheu o pacote PRATA🔱, Parabéns!')
				print('-=-' *20) 
			elif pacote.upper()=='OURO':
				print('')
				print('Você escolheu o pacote OURO👑, Parabéns!\033[m')
				print('-=-' *20)
			else:
				print('')
				print('\033[1;31mOPCÃO INVALIDA.\033[m')
				print('')
				print('\033[1;34m<~~~~~~~~[FIM]~~~~~~~~~>\033[m')
		elif select==3:
			print('\033[1;33m~~~~~~~{inicio}~~~~~~~\033[m')
			senha=1
			while True:
				pross=input('\033[1;32mDeseja continuar(S/N)? \033[m')
				if pross.upper()=='S':
					enter=input('\033[1;34mPressione enter e retire sua senha>>\033[m')
					print('\033[1;36mloading...\033[m')
					senha=senha+1
					print('\033[1;36mSua senha é \033[m' '\033[7m{}\033[m' '\033[1;36m .Aguarde um instante.\033[m'.format(senha))
					print('\033[1;36m...\033[m')
				else:
					break
				print('=' *20)
		elif select==4:
			print('\033[1;34m<<~~~~~~{INICIO}~~~~~~>>\033[m')
			n=int(input("""\033[1;33mQuantas vezes você deseja ultilizar o
programa? """))
			print('....\033[m')
			cont=0
			while cont<n:
				cont=cont+1
				print("""\033[1;33mPreencha as informações do local onde
  será feito a entrega: """)
				print('')
				nome=input('Nome do cliente: ')
				rua=input('Rua: ')
				ap=input('Apartamento/prédio: ')
				bloco=input('Bloco: ')
				print('°•°•°•\033[m')
				print("""\033[7;36mDADOS DE ENTREGA:     \033[m
\033[7;36mNome do cliente: {}\033[m
\033[7;36mRua:             {}\033[m
\033[7;36mApartamento:     {}\033[m
\033[7;36mBloco:        {}\033[m""".format(nome, rua, ap, bloco))
#aqui eu ultilizei os codigos de cores fechando cada linha para a cor não preencher horizontalmente a linha sem fim
				print('\033[1;33m<<~~~~~~~~[FIM]~~~~~~~~~>>')
		elif select==5:
			while True:
					print('\033[1;33m~~~~~~~~{INÍCIO}~~~~~~~~~\033[m')
					print("""\033[4;34m       PRODUTOS:         | VALOR:\033[m""")
					print("""\033[1;36m                         |
<1> Pretinho stock car.  | R$ 15.0
<2> Aromatizante.        | R$ 10.0
<3> repelente de água.   | R$ 20.0
<4> Chaveiros            | R$ 35.0
<5> Óleo de motor.       | R$ 40.0
<6> Adesivos.            | R$ 5.0\033[m""")
#os preços foram retirados da internet, juntamente com os produtos
					prod=int(input('\033[1;34mEscolha uma das opções para o respectivo item: \033[m '))
					print('\033[1;32mCARREGANDO...\033[m')
					sleep(0.75)
					#esse sleep é o tempo que o programa levará para processar somente nessa parte
					if prod==1:
						print('\033[1;36m===Você escolheu Pretinho Stock Car.===\033[m')
					elif prod==2:
						print('\033[1;36m===Você escolheu Aromatizante.===\033[m')
					elif prod==3:
						print('\033[1;36m===Você escolheu Repelente de água.===\033[m')
					elif prod==4:
						print('\033[1;36m===Você escolheu Chaveiros.===\033[m')
					elif prod==5:
						print('\033[1;36m===Você escolheu Óleo de motor.===\033[m')
					elif prod==6:
						print('\033[1;36m===Você escolheu Adesivos.===\033[m')
					else:
						print('\033[1;31mESSA OPÇÃO NÃO EXISTE.\033[m')
					mas=input('\033[1;33mDeseja escolher mais produtos(S/N)?  \033[m')
					if mas.upper()=='N':
						print('\033[1:33mFim!\033[m')
						break
		elif select==0:
				print('')
				print('\033[1;33mObrigado por ultilizar nosso programa!\033[m')
				print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
#é possivel adicionar artes com textos ultilizando 3 aspas duplas
				break
				#break para o código
	except:
		#esse bloco fecha a excessão
				print(' ')
				print('\033[1;31mOpção inválida.\033[m')
				print('<<>>'*14) 
				#um texto vezes um numero serve para aumentar o numero de caracteres desse texto sem precisar ficar digitando a mesma coisa