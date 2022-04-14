from random import randint
cartas=[{'nome':'mago','atk':3500,'dfs':3000},{'nome':'feiticeira','atk':3000,'dfs':3500},{'nome':'lanceiro','atk':4500,'dfs':2000},{'nome':'conselheiro','atk':3500,'dfs':4000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':4000,'dfs':4000},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':4000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':3500},{'nome':'lenhador','atk':4000,'dfs':3000},{'nome':'rei','atk':2500,'dfs':5000}]
porçoes=[{'nome':'atk','ação':'+500','qua':3},{'nome':'dfs','ação':'+500','qua':3},{'nome':'imunidade','ação':'0','qua':3},{'nome':'atk','ação':'*2','qua':3},{'nome':'dfs','ação':'*2','qua':3}]
####pc###
pc=[]
pcpor=[]
atqpc=[]
defpc=[]
####usuario####
usu=[]
usupor=[]
atqusu=[]
defusu=[]
#####jogo#####
crt=vusu=vpc=0
rod=1
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
#########porçoes do pc###########    
for i in pcpor:
    i['qua']=1
    if i['nome']=='atk':
        atqpc.append(i)
    else:
        defpc.append(i)

#########porçoes do usuario#######
for i in usupor:
    i['qua']=1
    if i['nome']=='atk':
        atqusu.append(i)
    else:
        defusu.append(i)
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


                                                ###jogo###                                            
while True:
                #######placar#########
    print('=+'*25)
    print(f'\033[033m{"Placar":^50}\033[m')
    print('=+'*25)
    print(f'\033[034mPc={vpc:2}\033[m')
    print(f'\033[035mUsuario={vusu:^2}\033[m')
    print('=+'*25)

    if rod==0:
        ################## Cartas do Usúario ##############
        crt=0
        print('=+'*25)
        print(f'\033[033m{"Suas cartas são":^50}\033[m ')
        print('=+'*25)
        for i in usu:
            crt=crt+1
            print(f'\033[034m{crt:>2}°- \033[036m{i["nome"].upper():<13}\033[m',end='  ')
            print(f'\033[031mAtaque: {i["atk"]:>4}\033[m',end='  ')
            print(f'\033[032mDefesa: {i["dfs"]:>4}\033[m')
        print(f'\033[033m{"porções":^50}\033[m')
        for i in usupor:
            print(f'\033[034m{i["nome"].upper()}\033[m',end=' ')
            print(f'\033[036m{i["ação"]}\033[m')


                                        ######Vez do usuario####
    
    if rod%2==0:
        crt=0
        print('=+'*25)
        print(f'\033[033m{"Personagem":^50}\033[m ')
        print('=+'*25)
        for i in usu:
            crt=crt+1
            print(f'\033[034m{crt:>2}°- \033[036m{i["nome"].upper():<13}\033[m',end='  ')
            print(f'\033[031mAtaque: {i["atk"]:>4}\033[m',end='  ')
            print(f'\033[032mDefesa: {i["dfs"]:>4}\033[m')
        print('=+'*25)

        while True:
            if len(usu)>=2:
                c=input(f'\033[035mQual carta deseja escolher:\033[m 1/{len(usu)} ')
            else:
                c='1'
            if c.isnumeric()==True:
                c=int(c)
                if 0!=c<=len(usu):
                    carusu=usu[c-1]
                    print('=+'*25)
                    print(f'\033[033m{"A carta escolhida foi":^50}\033[m')
                    print('=+'*25)
                    print(f'\033[036m{carusu["nome"].upper()}\033[m')
                    print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                    print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                    print('=+'*25)
                    while True:
                        acaousu=input('Deseja \033[031m[A]\033[mtacar \033[032m[D]\033[mefender ou \033[036m[R]\033[mecarregar: ').upper().strip()[0]
                        if acaousu in 'ADR':
                                        ####Ataque ou defesa####
                            if acaousu in 'AD':
                                        ###escolha da carta do pc###
                                escpc=randint(0,len(pc)-1)
                                carpc=pc[escpc]
                                usapor=randint(0,1)
                                combate=1

                                #print(carpc)
                                crt=0
                                              #####Ataque#### 
                                if acaousu=='A':
                                          #########Porção do pc###########
                                    if usapor==0 or len(defpc)==0:
                                        print('\033[031mO pc não usou porção de defesa\033[m')
                                    else:
                                        qualpor=randint(0,len(defpc)-1)
                                        pcesc=defpc[qualpor]
                                        qualpor=randint(0,len(defpc)-1)
                                        pcesc=defpc[qualpor]
                                        print('\033[032mO pc usou uma porção de defesa\033[m ')
                                        ação=(pcesc['ação'])
                                        if '+' in ação:
                                            carpc['dfs']=carpc['dfs']+int(ação)
                                        if '*' in ação:
                                            ação=ação.replace('*','')
                                            carpc['dfs']=carpc['dfs']*int(ação)
                                        if ação=='0':
                                            combate=0
                                        defpc.pop(defpc.index(pcesc))
                                        pcpor.pop(pcpor.index(pcesc))
                                    ###########Jogada do usuario##############
                                    if len(atqusu)>0:
                                        print('=+'*25)
                                        print(f'\033[033m{"porções de ataque":^50}\033[m')
                                        print('=+'*25)
                                        for i in atqusu:
                                            crt=crt+1
                                            print(f'{crt}°- {i["nome"].upper()}',end=' ')
                                            print(i['ação'])
                                        print('=+'*25)
                                        while True:
                                            escpor=input('Deseja usar alguma S/N ').upper().strip()[0]
                                            if escpor in 'SN':
                                                if escpor=='S':
                                                    while True:
                                                        if len(atqusu)>=2:
                                                            escpor=input(f'Qual porção? 1/{len(atqusu)}: ')
                                                        else:
                                                            escpor='1'
                                                        if escpor.isnumeric()==True:
                                                            if int(escpor)==0 or int(escpor)>len(atqusu):
                                                                print('\033[031mPorção Inexistente\033[m')
                                                            else:
                                                                poresc=atqusu[int(escpor)-1]
                                                                ação=poresc['ação']
                                                                if '+' in ação:
                                                                    carusu['atk']=int(carusu['atk'])+int(ação)
                                                                    print('\033[032mporção usada com sucesso!\033[m')
                                                                elif '*' in ação:
                                                                    ação=ação.replace('*','')
                                                                    carusu['atk']=int(carusu['atk'])*int(ação)
                                                                    print('\033[032mPorção usada com sucesso!\033[m')                                                                                             
                                                                atqusu.pop(atqusu.index(poresc))
                                                                usupor.pop(usupor.index(poresc))
                                                                break                
                                            
                                                        else:
                                                            print('\033[031mOpção inválida\033[m')
                                                    break
                                                else:
                                                    print('\033[031mVocê Não usou nenhuma porção\033[m')
                                                    break
                                            else:
                                                print('\033[031mOpção inválida\033[m')
                                    else:
                                        print('\033[031mVocê não possui porções de Ataque\033[m')
                                        break
                                    

                                    #####combate#####
                                    if combate==0:
                                        print('\033[m033mporção de imunidade usada pelo Pc\033[m')
                                    else:
                                        dano=carpc['dfs']-carusu['atk']
                                        if dano>0:
                                            print(f'\033[031mVocê Perdeu\033[m')
                                            print(f'sua carta \033[036m{carusu["nome"].upper()}\033[m foi elimininada')
                                            carpc['dfs']=carpc['dfs']-dano
                                            usu.pop(usu.index(carusu))
                                            vpc=vpc+1
                                        elif dano==0:
                                            print(f'\033[033mEmpate\033[m')
                                            carpc['dfs']=carusu['atk']=0
                                            print(f'\033[036m{carusu["nome"].upper()}\033[m')
                                            print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                                            print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                                        else:
                                            print(f'\033[032mVocê Ganhou\033[m')
                                            carusu['atk']=dano*-1
                                            print(f'\033[036m{carusu["nome"].upper()}\033[m')
                                            print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                                            print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                                            pc.pop(pc.index(carpc))
                                            vusu=vusu+1
                                    break
                                        ###defesa###
                                if acaousu=='D':
                                    ###########Escolha da porção do pc########
                                    if usapor==0 or len(atqpc)==0:
                                        print('\033[031mO pc não usou porção de Ataque\033[m')
                                    else:
                                        qualpor=randint(0,len(atqpc)-1)
                                        pcesc=atqpc[qualpor]
                                        print('\033[032mO pc usou uma porção de Ataque\033[m ')
                                        ação=(pcesc['ação'])
                                        if '+' in ação:
                                            carpc['atk']=carpc['atk']+int(ação)
                                        if '*' in ação:
                                            ação=ação.replace('*','')
                                            carpc['atk']=carpc['atk']*int(ação)
                                        if ação==0:
                                            combate=0
                                        atqpc.pop(atqpc.index(pcesc))
                                        pcpor.pop(pcpor.index(pcesc))
                                   ##############Jogada do ususario#################
                                    if len(defusu)>0:
                                        print('=+'*25)
                                        print(f'\033[033m{"porções de Defesa":^50}\033[m')
                                        print('=+'*25)
                                        for i in defusu:
                                            crt=crt+1
                                            print(f'{crt}°- {i["nome"]}',end=' ')
                                            print(i['ação'])
                                        print('=+'*25)
                                        while True:
                                            escpor=input('Deseja usar alguma S/N ').upper().strip()[0]
                                            if escpor in 'SN':
                                                if escpor=='S':
                                                    while True:
                                                        if len(defusu)>=2:
                                                            escpor=input(f'Qual porção? 1/{len(defusu)}: ')
                                                        else:
                                                            escpor='1'
                                                        if escpor.isnumeric()==True:
                                                            if int(escpor)==0 or int(escpor)>len(defusu):
                                                                print('\033[031mPorção Inválida\033[m')
                                                            else:
                                                                poresc=defusu[int(escpor)-1]
                                                                ação=poresc['ação']
                                                                if '+' in ação:
                                                                    carusu['dfs']=int(carusu['dfs'])+int(ação)
                                                                    print('\033[032mporção usada com sucesso!\033[m')
                                                                if '*' in ação:
                                                                    ação=ação.replace('*','')
                                                                    carusu['dfs']=int(carusu['dfs'])*int(ação)
                                                                    print('\033[032mPorção usada com sucesso!\033[m')
                                                                if ação=='0':
                                                                    combate=0
                                                                defusu.pop(defusu.index(poresc))
                                                                usupor.pop(usupor.index(poresc))
                                                                break               
                                                        else:
                                                            print('\033[031mOpção inválida\033[m')
                                                    break        
                                                else:
                                                    print('\033[031mVocê não usou nenhuma porção\033[m')
                                                    break
                                            else:
                                                print('\033[031mOpção inválida\033[m')
                                    else:
                                        print('\033[031mVocê não possui porções de Defesa\033[m')
                                        ########combate#########
                                    if combate==0:
                                        print('\033[033mPorção de imunidade usada\033[m')
                                    if combate==1:
                                        dano=carpc['atk']-carusu['dfs']
                                        if dano>0:
                                            print(f'\033[031mVocê Perdeu\033[m')
                                            print(f'Sua carta \033[035m{carusu["nome"].upper()}\033[m foi eliminada')
                                            carpc['atk']=carpc['atk']-dano
                                            usu.pop(usu.index(carusu))
                                            vpc=vpc+1
                                        elif dano==0:
                                            print(f'\033[033mEmpatou\033[m')
                                            carpc['atk']=carusu['dfs']=0
                                            print(f'\033[036m{carusu["nome"].upper()}\033[m')
                                            print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                                            print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                                        else:
                                            print(f'\033[032mVocê Ganhou\033[m')
                                            carusu['dfs']=(dano*-1)
                                            print(f'\033[036m{carusu["nome"].upper()}\033[m')
                                            print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                                            print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                                            pc.pop(pc.index(carpc))
                                            vusu=vusu+1
                                    break
                                        #######RECARGA########
                            if acaousu =='R':
                                nome=carusu['nome'].upper()
                                while True:
                                    acaousu=input('\033[032m[D]\033[mefesa ou \033[031m[A]\033[mtaque: ').upper().strip()[0]
                                    if acaousu in 'AD':
                                        if acaousu=='A':
                                            carusu['atk']=carusu['atk']+500
                                            print(f'\033[031mVocê recarregou o ataque da carta {nome}\033[m')
                                        if acaousu=='D':
                                            carusu['dfs']=carusu['dfs']+500
                                            print(f'\033[032mVocê recarregou a defesa da carta {nome}\033[m')
                                        print(f'\033[036m{carusu["nome"].upper()}\033[m')
                                        print(f'\033[031mAtaque: {carusu["atk"]:>4}\033[m')
                                        print(f'\033[032mDefesa: {carusu["dfs"]:>4}\033[m')
                                        break
                                    else:
                                        print('\033[031mAção inválida\033[m')
                                break
                        else:
                            print('\033[031mAção Inválido\033[m')
                    break
                else: 
                    print('\033[031mCarta Inválida!\033[m')
            else:
                print('\033[031mCarta Inválida\033[m')

        rod=rod+1
        crt=0

                              ###########Jogada do pc#########
    if rod%2==1:
        açoespc=('A','D','R')
        escpc=randint(0,len(pc)-1)
        print('=+'*25)
        print(f'\033[033m{"Placar":^50}\033[m')
        print('=+'*25)
        print(f'\033[034mPc={vpc:2}\033[m')
        print(f'\033[035mUsuario={vusu:^2}\033[m')
        print('=+'*25)
        print('=+'*25)
        print(f'\033[036m{"vez do pc":^50}\033[m')
        print('=+'*25)
        ##############Pc escolhe a carta###########
        carpc=pc[escpc]
        print(carpc)
        usapor=randint(0,1)
        açãopc=açoespc[randint(0,2)]
        print(açãopc)
        combate=1
        if açãopc in'AD':
            if açãopc=='A':
                print('\033[031mO pc está atacando\033[m')
                if usapor==0 or len(atqpc)==0:
                    print('\033[031mO pc não usou porção de Ataque\033[m')
                else:
                    qualpor=randint(0,len(atqpc)-1)
                    pcesc=atqpc[qualpor]
                    print('\033[032mO pc usou uma porção de Ataque\033[m ')
                    ação=(pcesc['ação'])
                    if '+' in ação:
                        carpc['atk']=carpc['atk']+int(ação)
                    if '*' in ação:
                        ação=ação.replace('*','')
                        carpc['atk']=carpc['atk']*int(ação)
                    if ação==0:
                        combate=0
                    atqpc.pop(atqpc.index(pcesc))
                    pcpor.pop(pcpor.index(pcesc))
                
            else:
                print('\033[032mO pc está atacando\033[m')
                if usapor==0 or len(defpc)==0:
                    print('\033[031mO pc não usou porção de defesa\033[m')
                else:
                    qualpor=randint(0,len(defpc)-1)
                    pcesc=defpc[qualpor]
                    qualpor=randint(0,len(defpc)-1)
                    pcesc=defpc[qualpor]
                    print('\033[032mO pc usou uma porção de defesa\033[m ')
                    ação=(pcesc['ação'])
                    if '+' in ação:
                        carpc['dfs']=carpc['dfs']+int(ação)
                    if '*' in ação:
                        ação=ação.replace('*','')
                        carpc['dfs']=carpc['dfs']*int(ação)
                    if ação=='0':
                        combate=0
                    defpc.pop(defpc.index(pcesc))
                    pcpor.pop(pcpor.index(pcesc))

        else:
            açãopc=açoespc[randint(0,1)]
            if açãopc=='A':
                print('\033[031mO pc Recarregou o Ataque\033[m')
                carpc['atk']=carpc['atk']+500
            else:
                print('\033[032mO pc recarregou a defesa\033[m ')
                carpc['dfs']=carpc['dfs']+500

    crt=0
    rod=rod+1
    if len(pc)==0 or len(usu)==0:
        break
print('Fim do jogo')
    

