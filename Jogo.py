from os import remove
from random import randint
cartas=[{'nome':'mago','atk':3500,'dfs':3000},{'nome':'feiticeira','atk':3000,'dfs':3500},{'nome':'lanceiro','atk':4500,'dfs':2000},{'nome':'conselheiro','atk':3500,'dfs':4000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':4000,'dfs':4000},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':4000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':3500},{'nome':'lenhador','atk':4000,'dfs':3000},{'nome':'rei','atk':2500,'dfs':5000}]
porçoes=[{'nome':'atk','ação':'+500','qua':3},{'nome':'dfs','ação':'+500','qua':3},{'nome':'imunidade','ação':'0','qua':3},{'nome':'atk','ação':'*2','qua':3},{'nome':'dfs','ação':'*2','qua':3}]
pc=[]
pcpor=[]
usu=[]
usupor=[]
atqusu=[]
defusu=[]
imunusu=[]
crt=rod=vusu=vpc=0
#print(len(cartas))


#Distribuição de cartas#
#porções
for i in range(0,4):
    porçao=porçoes[randint(0,len(porçoes)-1)]
    #print(porçao)
    pos=porçoes.index(porçao)
    pcpor.append(porçao)
    porçao['qua']=porçao['qua']-1
    if porçao['qua']==0:
        porçoes.pop(pos)

    porçao=porçoes[randint(0,len(porçoes)-1)]
    #print(porçao)
    pos=porçoes.index(porçao)
    usupor.append(porçao)
    porçao['qua']=porçao['qua']-1
    if porçao['qua']==0:
        porçoes.pop(pos)
    
for i in pcpor:
    i['qua']=1
for i in usupor:
    i['qua']=1
    if i['nome']=='atk':
        atqusu.append(i)
    elif i['nome']=='dfs':
        defusu.append(i)
    else:
        imunusu.append(i)
#personagens
for i in range(len(usu),len(usu)+6):
    carta=cartas[randint(0,len(cartas)-1)]
    pos=cartas.index(carta)
    pc.append(carta)
    cartas.pop(pos)
    carta=cartas[randint(0,len(cartas)-1)]
    pos=(cartas.index(carta))
    usu.append(carta)
    cartas.pop(pos)
print('=+'*30)
print(f'\033[034mCartas do pc{pc}\033[m')
print(f'\033[035mPorções do Pc{pcpor}\033[m')
print('=+'*30)
print(f'\033[035mCartas do usuario {usu}\033[m')
print(f'\033[034mPorções do usuario{usupor}\033[m')
print('=+'*25) 

                                                ###jogo###
                                            
while True:
                        #######Cartas usuario########
    crt=0
    print('=+'*25)
    print(f'\033[033m{"Suas cartas são":^50}\033[m ')
    print('=+'*25)
    for i in usu:
        crt=crt+1
        print(f'\033[034m{crt:>2}°- \033[036m{i["nome"]:<13}\033[m',end='  ')
        print(f'\033[031mAtaque: {i["atk"]:>4}\033[m',end='  ')
        print(f'\033[032mDefesa: {i["dfs"]:>4}\033[m')
    
                            ######Vez do usuario####
    while True:
        c=input(f'Qual carta deseja escolher: 1/{len(usu)} ')
        if c.isnumeric()==True:
            c=int(c)
            if 0!=c<=len(usu):
                carusu=usu[c-1]
                print('=+'*25)
                print(f'\033[033m{"A carta escolhida foi":^50}\033[m')
                print('=+'*25)
                print(f'\033[036m{carusu["nome"]}\033[m')
                print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                print('=+'*25)
                while True:
                    acaousu=input('Qual ação deseja efetuar? A,D,R: ').upper().strip()[0]
                    if acaousu in 'ADR':
                                    ####Ataque ou defesa####
                        if acaousu in 'AD':
                            crt=0
                            if acaousu=='A':
                                if len(atqusu)>0:
                                    print('=+'*25)
                                    print(f'\033[033m{"porções de ataque":^50}\033[m')
                                    print('=+'*25)
                                    for i in atqusu:
                                        crt=crt+1
                                        print(f'{crt}°- {i["nome"]}',end=' ')
                                        print(i['ação'])
                                    print('=+'*25)
                                    while True:
                                        escpor=input('Deseja usar alguma S/N ').upper().strip()[0]
                                        if escpor in 'SN':
                                            if escpor=='S':
                                                escpor=input(f'Qual porção? 1/{len(atqusu)}')
                                                if escpor.isnumeric()==True:
                                                    poresc=atqusu[int(escpor)-1]
                                                    ação=poresc['ação']
                                                    if '+' in ação:
                                                        carusu['atk']=int(carusu['atk'])+int(ação)
                                                        print('\033[032mporção usada com sucesso!033[m')
                                                        print(carusu)

                                                    if '*' in ação:
                                                        ação=ação.replace('*','')
                                                        carusu['atk']=int(carusu['atk'])*int(ação)
                                                        print('\033[032mPorção usada com sucesso!\033[m')
                                                        print(carusu)
                                                    atqusu.pop(atqusu.index(poresc))
                                                    print(f'\033[032m{atqusu}\033[m')
            
                                                else:
                                                    print('\033[031mOpção inválida\033[m')
                                            else:
                                                print('não usar')
                                                break
                                        else:
                                            print('\033[031mOpção inválida\033[m')
                                else:
                                    print('Você não possui porções de Ataque')






                                    #######RECARGA########
                        if acaousu =='R':
                            acaousu=input('Deseja recarregar a defesa ou o ataque D/A').upper().strip()[0]
                            if acaousu=='A':
                                carusu['atk']=carusu['atk']+500
                                print('Recarga no ataque')
                                break
                            if acaousu=='D':
                                carusu['dfs']=carusu['dfs']+500
                                print('Recarga na defesa')
                                break
                    else:
                        print('\033[031mAção Inválido\033[m')
                break
            else: 
                print('\033[031mCarta Inválida!\033[m')
        else:
            print('\033[031mCarta Inválida\033[m')
    '''crt=0
    for i in usupor:
        crt=crt+1
        print(f'\033[034m{crt:>2}°- \033[036m{i["nome"]:<13}\033[m',end=' ')
        print(f'\033[033{i["ação"]}\033[m')
    a=(input('digite um valor para jogo 0 encerra:'))'''
    break
print('Fim')
    

