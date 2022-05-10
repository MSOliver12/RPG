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
    combate=1
    pcrec=0       
    carpc=pc[randint(0,len(pc)-1)]
    if jogador=='pc':
        while True:
            açao=('a','d','r')
            ação=açao[randint(0,len(açao)-1)]
            if ação=='r':
                pcrec=1
                pcação='rec'
                usuação='rec'
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
                    usuopcpor='dfs imunidade'
                    pcopcpor='atk'
                    print('\033[031mO pc está atacando\033[m')
                else:
                    usuação='atk'
                    pcação='dfs'
                    usuopcpor='atk'
                    pcopcpor='dfsimunidade'
                    print('\033[032mO pc está se defendendo\033[m')
            break
    if pcrec==0:
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
        pcrec=0
        while True:
            ação=input('Deseja \033[031m[A]\033[mtacar \033[032m[D]\033[mefender ou \033[036m[R]\033[mecarregar? ').upper().strip()[0]
            if ação in 'ADR':
                if ação in 'AD':
                    crt=0
                    if ação=='A':
                        usuação='atk'
                        pcação='dfs'
                        pcopcpor='dfs imunidade'
                        usuopcpor='atk'
                        cabeçalho('Porção de Ataque')
                        
                    else:
                        usuação='dfs'
                        pcação='atk'
                        pcopcpor='atk'
                        usuopcpor='dfsimunidade'
                        cabeçalho('Porção de Defesa')
                else:
                    while True:
                        usução='rec'
                        pcação='rec'
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
############Escolha de porção#################
    if pcação=='rec' or usuação=='rec':
        print('\033[036mRecarga efetuada\033[m')

#####################PORÇÕES##################
###################Porção usu#################
    else:
        pcusapor=randint(0,1)
        porçõespc=[]
        porçoesusu=[]
        for i in usupor:
            if i['nome'] in usuopcpor:
                porçoesusu.append(i)
        if len(porçoesusu)>0:
            crt=0
            for i in porçoesusu:
                crt=crt+1
                print(f'{crt}°- \033[036m{i["nome"].upper():^10}\033[m',end=' ')
                print(f'\033[035mAção= {i["ação"]}\033[m')
            while True:    
                usarpor=input('Deseja usar alguma porção S/N: ').upper().strip()[0]
                if usarpor in 'SN':
                    if usarpor=='S':
                        if len(porçoesusu)>1:
                            while True:
                                qualporusu=input(f'Qual porção 1/{len(porçoesusu)}: ')
                                if qualporusu.isnumeric()==True:
                                    qualpor=int(qualporusu)
                                    if qualpor!=0 and qualpor<=len(porçoesusu):
                                        qualpor=qualpor-1
                                        break
                                else:
                                    print('\033[031mPorção Inválida\033[m')
                        elif len(porçoesusu)==1:
                            qualpor=0
                        porção=(porçoesusu[qualpor])
                        ação=porção['ação']
                        if '*' in ação:
                            ação=int(ação.replace('*',''))
                            carusu[usuação]=carusu[usuação]*ação
                        elif ação=='0':
                            combate=0
                            carpc[pcação]=0
                        else:
                            carusu[usuação]=carusu[usuação]+int(ação)

                        usupor.pop(usupor.index(porção))
                        print('\033[032mUsu usou Porção\033[m')
                    else:
                        print('\033[031musu não usou porção\033[m')
                    break
                else:
                    print('\033[031mOpção inválida\033[m')    
        else:
            print('\033[031mVocê não possui porções disponiveis\033[m')
   ################pcporção#############
        for i in pcpor:
            if i['nome'] in pcopcpor:
                porçõespc.append(i)
        if len(porçõespc)>0 and pcusapor==1:
            print('\033[032mO pc usou uma  porção\033[m')
            qualporpc=porçõespc[randint(0,len(porçõespc)-1)]
            ação=qualporpc['ação']
            if '*' in ação:
                ação=ação.replace('*','')
                if ação!='0':
                    carpc[pcação]=carpc[pcação]*int(ação)
            elif ação=='0':
                combate=0
                carusu[usuação]=carusu[usuação]*int(ação)
            else:
                carpc[pcação]=carpc[pcação]+int(ação)
            pcpor.pop(pcpor.index(qualporpc))
        else:
            print('\033[031mO pc não usou porção\033[m')

######################COMBATE##################

        if combate==1:
            dano=carpc[pcação]-carusu[usuação]
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
        elif combate==0:
            print('\033[033mPorção de Imunidade\033[m')

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
    print(f'\033[035mAção= {i["ação"]}\033[m')

while True:
    if rod%2==0 and len(usu)>0 and len(pc)>0:
        cabeçalho('Placar')
        print(f'Pc= {6-len(usu)}')
        print(f'Usu= {6-len(pc)}')
        jogada='usuario'
        cabeçalho('Usuario')
    if rod%2==1 and len(pc)>0 and len(usu)>0:
        cabeçalho('Placar')
        print(f'Pc= {6-len(usu)}')
        print(f'Usu= {6-len(pc)}')
        jogada='pc'
        cabeçalho('Computador')
    if len(pc)==0 or len(usu)==0:
        cabeçalho('Fim')
        cabeçalho('Placar')
        print(f'Pc= {6-len(usu)}')
        print(f'Usu= {6-len(pc)}')
        break
    jogo(jogada)
    rod=rod+1
