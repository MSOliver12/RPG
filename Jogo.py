from dataclasses import replace
from random import randint
cartas=[{'nome':'mago','atk':3500,'dfs':3000},{'nome':'feiticeira','atk':3000,'dfs':3500},{'nome':'lanceiro','atk':4500,'dfs':2000},{'nome':'conselheiro','atk':3500,'dfs':4000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':4000,'dfs':4000},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':4000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':3500},{'nome':'lenhador','atk':4000,'dfs':3000},{'nome':'rei','atk':2500,'dfs':5000}]
porçoes=[{'nome':'atk','ação':'+500','qua':3},{'nome':'dfs','ação':'+500','qua':3},{'nome':'imunidade','ação':'0','qua':3},{'nome':'atk','ação':'*2','qua':3},{'nome':'dfs','ação':'*2','qua':3}]
####pc###
pc=[]
pcpor=[]
####usuario####
usu=[]
usupor=[]
#####jogo#####
crt=rod=vusu=vpc=0

#print(len(cartas))


#Distribuição de cartas#
#personagens
for i in range(0,12):
    personagem=cartas[randint(0,len(cartas)-1)]
    pos=cartas.index(personagem)
    if i%2==0:
        usu.append(personagem)
    else:
        pc.append(personagem)
    cartas.pop(pos)


#porções
for i in range(0,8):
    porçao=porçoes[randint(0,len(porçoes)-1)]
    pos=porçoes.index(porçao)
    #######porção pro pc##########
    if i%2==0:
        pcpor.append(porçao)
    #######porção do usuario######
    if i%2==1:
        usupor.append(porçao)

    if porçao['qua']==0:
        porçoes.pop(pos)
###################Fuções############

def cabeçalho (texto):
    print('=+'*25)
    print(f'\033[033m{texto:^50}\033[m')
    print('=+'*25)

def jogo(jogador):
    pcação=usuação='nada'
    
    
    carpc=pc[randint(0,len(pc)-1)]
    if jogador=='pc':
        while True:
            açao=('a','d','r')
            ação=açao[randint(0,len(açao)-1)]
            if ação=='r':
                print('\033[036mO pc recarregou\033[m')
                ação=açao[randint(0,1)]
                if ação=='a':
                    carpc['atk']=carpc['atk']+500
                else:
                    carpc['dfs']=carpc['dfs']+500
            else:
                if ação=='a':
                    usuação='dfs'
                    pcação='atk'
                    print('\033[031mO pc está atacando\033[m')
                else:
                    usuação='atk'
                    pcação='dfs'
                    print('\033[032mO pc está se defendendo\033[m')
            break

    crt=0
    for i in usu:
        crt=crt+1
        print(f'{crt}°- \033[036m{i["nome"].upper():^12}\033[m',end=' ')
        print(f'\033[031mAtaque: {i["atk"]:^4}\033[m',end=' ')
        print(f'\033[032mDefesa: {i["dfs"]:^4}\033[m')

    while True:
        escolhausu=input(f'Qual carta deseja escolher? 1/{len(usu)} ')
        if escolhausu.isnumeric()==True:
            escolhausu=int(escolhausu)
            if escolhausu==0 or escolhausu>len(usu):
                print('\033[031mCarta inválida\033[m')
            else:
                carusu=usu[escolhausu-1]
                cabeçalho('Carta escolhida')
                print(f'{escolhausu}° \033[036m{carusu["nome"]}\033[m')
                print(f'\033[031mAtaque: {carusu["atk"]}\033[m')
                print(f'\033[032mDefesa: {carusu["dfs"]}\033[m')
                break
        else:
            print('\033[031mCarta inválida\033[m')
    if jogador=='usuario':
        while True:
            ação=input('Deseja \033[031m[A]\033[mtacar \033[032m[D]\033[mefender ou \033[036m[R]\033[mecarregar? ').upper().strip()[0]
            if ação in 'ADR':
                if ação in 'AD':
                    crt=0
                    atqusu=[]
                    defusu=[]
                    if ação=='A':
                        usuação='atk'
                        pcação='dfs'
                        cabeçalho('Porção de Ataque')
                        for i in usupor:
                            if i['nome']=='atk':
                                atqusu.append(i)
                                crt=crt+1
                                print(f'{crt}°- \033[036m{i["nome"].upper():^10}\033[m',end=' ')
                                print(f'\033[035mAção={i["ação"]}\033[m')
                        if crt==0:
                            print('\033[031mVocê não possui porção de Ataque\033[m') 

                    else:
                        usuação='dfs'
                        pcação='atk'
                        cabeçalho('Porção de Defesa')
                        for i in usupor:
                            if i['nome']=='dfs':
                                defusu.append(i)
                                crt=crt+1
                                print(f'{crt}°- \033[036m{i["nome"].upper():^10}\033[m',end=' ')
                                print(f'\033[035mAção={i["ação"]}\033[m')  
                        if crt==0:
                            print('\033[031mVocê não possui porção de Defesa\033[m')         
                    if crt>0:
                        while True:            
                            usaporção=input('Deseja usar uma porção? S/N ').upper().strip()[0]
                            if usaporção in 'SN':
                                if usaporção=='S':
                                    while True:
                                        if crt>1:
                                            qualpor=input(f'Qual Porção deseja usar 1/{crt}? ')
                                        else:
                                            qualpor='1'
                                        if qualpor.isnumeric()==True:
                                            qualpor=int(qualpor)
                                            if qualpor>0 and qualpor<=crt:
                                                if usuação=='atk':
                                                    porção=atqusu[qualpor-1]
                                                if usuação=='dfs':
                                                    porção=defusu[qualpor-1]
                                                ação=(porção['ação'])
                                                if '*' in ação:
                                                    ação=ação.replace('*','') 
                                                    carusu[usuação]=carusu[usuação]*int(ação)                                                                             
                                                else:
                                                    (carusu[usuação])=carusu[usuação]+int(ação)
                                                    
                                                usupor.pop(usupor.index(porção))
                                                break
                                            else:
                                                print('\033[031mPorção inválida\033[m')
                                        else:
                                            print('\033[031mPorção inválida\033[m')

                                if usaporção=='N':
                                    print('\033[031mPorção não utilizada\033[m')
                                break
                            else:
                                print('\033[031mOpção inválida\033[m')
                else:
                    while True:
                        ação=input('Deseja recarregar \033[031m[A]\033[mtaque ou \033[032m[D]\033[mefesa? ').upper().strip()[0]
                        if ação in 'AD':
                            if ação=='A':
                                carusu['atk']=carusu['atk']+500
                            else:
                                carusu['dfs']=carusu['dfs']+500
                            print(f'{escolhausu}° \033[036m{carusu["nome"]}\033[m')
                            print(f'\033[031mAtaque: {carusu["atk"]}\033[m')
                            print(f'\033[032mDefesa: {carusu["dfs"]}\033[m')
                            break
                        else:
                            print('\033[031mopção inválida\033[m')
                break
            else:
                print('\033[031mAção inválida\033[m')
    ########combate######
    '''print(carusu)
    print(carpc)'''
    if pcação!='nada' or usuação!='nada':
        dano=carpc[pcação]-carusu[usuação]
        print(dano)
        if dano>0:
            print('\033[031mVocê perdeu\033[m')
            carpc[pcação]=carpc[pcação]-dano
            usu.pop(usu.index(carusu))
        elif dano==0:
            print('\033[033mEmpate\033[m')
            carpc[pcação]=carusu[usuação]=0
        else:
            print('\033[032mVocê ganhou\033[m')
            carusu[usuação]=dano*-1
            pc.pop(pc.index(carpc))
        '''print(len(usu))
        print(len(pc))
        print(carusu)
        print(carpc)'''




#####################JOGO########################
cabeçalho('CARTAS')
crt=0
for i in usu:
    crt=crt+1
    print(f'{crt}°- \033[036m{i["nome"].upper():^12}\033[m',end=' ')
    print(f'\033[031mAtaque: {i["atk"]:^4}\033[m',end=' ')
    print(f'\033[032mDefesa: {i["dfs"]:^4}\033[m')
cabeçalho("Porções")
crt=0
for i in usupor:
    crt=crt+1
    print(f'{crt}°- \033[036m{i["nome"].upper():^10}\033[m',end=' ')
    print(f'\033[035mAção={i["ação"]}\033[m')

while True:
    if rod%2==0:
        jogada='usuario'
        cabeçalho('Usuario')
    if rod%2==1:
        jogada='pc'
        cabeçalho('Computador')
    if rod==20:
        cabeçalho('Fim')
        break
    jogo(jogada)
    rod=rod+1
