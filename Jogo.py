from random import randint
cartas=[{'nome':'mago','atk':5000,'dfs':3000},{'nome':'feiticeira','atk':4000,'dfs':3500},{'nome':'lanceiro','atk':5000,'dfs':1000},{'nome':'conselheiro','atk':0,'dfs':5000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':5000,'dfs':4500},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':5000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':0},{'nome':'lenhador','atk':4000,'dfs':4000},{'nome':'rei','atk':2500,'dfs':4000}]
porçao=[{'atk+':500,'qua':3},{'dfs+':500,'qua':3},{'imunidade':0,'qua':3},{'atk2':2,'qua':3},{'dfs2':2,'qua':3}]
pc=[]
usu=[]
crt=rod=vusu=vpc=0
#print(len(cartas))

#Distribuição de cartas#
for i in range(0,6):
    carta=cartas[randint(0,len(cartas)-1)]
    pos=(cartas.index(carta))
    pc.append(carta)
    cartas.pop(pos)
    carta=cartas[randint(0,len(cartas)-1)]
    pos=(cartas.index(carta))
    usu.append(carta)
    cartas.pop(pos)

                                                #jogo#
while True:
    print(f'{"=+"*15}')
    print(f'\033[033m{"Placar":^30}\033[m')
    print(f'\033[036mUsuario={vusu}, pc={vpc}\033[m')
    print(f'\033[036mCartas usuario: {len(usu)}\nCartas Pc: {len(pc)}\033[m')
    if len(usu)==0 or len(pc)==0:
        if len(usu)==0:
            vencedor='Pc'
        else:
            vencedor='Usuario'
        print(f'Fim do jogo o {vencedor} Venceu')
        break
    print(f'{"=+"*15}')
                                           #escolha da carta vez do usuario#
    print(f'{"=+"*15}')
    print(f'\033[034m{"Suas  cartas são":^30}\033[m')
    print(f'{"=+"*15}')
    if rod%2==0 and len(usu)>0:
        for i in usu:
            crt=crt+1
            print(f'{crt}°-\033[036m{i["nome"]}\033[m')
            print(f'\033[031mAtaque={i["atk"]}\033[m')
            print(f'\033[032mDefesa={i["dfs"]}\033[m')
            print('\n',end='')
        c=int(input(f'Qual carta deseja usar? 1/{len(usu)}: '))
        if c<=len(usu) and c!=0:
            carusu=usu[c-1]
            print(f'A carta escolhida foi:\n\033[036m{carusu["nome"]}\033[m\n\033[031mAtaque={carusu["atk"]}\033[m\n\033[032mDefesa={carusu["dfs"]}\033[m')
                                                #escolha da ação vez do usuario#
            while True:
                acaousu=input('Qual ação deseja efetuar? A/D/R').upper().strip()[0]
                if acaousu in 'AD':
                    numpc=randint(0,len(pc)-1)
                    carpc=pc[numpc]
                    if acaousu=='A':
                        #O usuario vai atacar logo o pc defende
                        dano=carusu['atk']-carpc['dfs']
                        if dano>0:
                            print('usuario ganhou')
                            pc.pop(numpc)
                            carusu['atk']=dano                   
                            vusu=vusu+1
                            print(f'resta:{dano} ataque')
                        elif dano==0:
                            print('empate')
                            carusu['atk']=carpc['dfs']=0
                        else:
                            print('Pc ganhou')
                            usu.pop(c-1)
                            carpc['dfs']=dano*-1
                            vpc=vpc+1
                        rod=rod+1
                        crt=0
                        break
                        
                    if acaousu=='D':
                        #O usuario defende logo o pc ataca
                        dano=carusu['dfs']-carpc['atk']
                        if dano>0:
                            print('Usuario ganhou')
                            pc.pop(numpc)
                            carusu['dfs']=dano
                            vusu=vusu+1
                            print(f'Resta:{dano} de defesa')
                        elif dano==0:
                            print('Empatou')
                            carusu['dfs']=carpc['atk']=0
                        else:
                            print('Pc ganhou')
                            usu.pop(c-1)
                            carpc['atk']=dano*-1
                            vpc=vpc+1
                        rod=rod+1
                        break
                    
                if acaousu=='R':
                    opc=input('O que deseja recarregar? A/D').strip().upper()[0]
                    if opc in 'AD':
                        if opc=='A':
                            carusu['atk']=carusu['atk']+500
                            print('A carta recebeu 500 de ataque')
                       
                        if opc=='D':
                            carusu['dfs']=carusu['dfs']+500
                            print('A carta recebeu 500 de defesa')
                          
                        rod=rod+1
                    break
        elif c>len(usu) or c==0:
            print('\033[031mNão existe essa carta escolha uma válida\033[m')
        crt=0
                                #vez do pc
    if rod%2==1 and len(pc)>0:
        print(f'{"=+"*15}')
        print(f'{"vez do pc":^30}')
        print(f'{"=+"*15}')
        acoes='A','D','R'
        numpc=randint(0,len(pc)-1)
        carpc=pc[numpc]
        acaopc=acoes[randint(0,2)]
        if acaopc in 'AD':
            if acaopc=='A':
                print('Defenda-se')
                at=carpc['atk']
            if acaopc=='D':
                print('Ataque-me')
                df=carpc['dfs']
            while True:
                for i in usu:
                    crt=crt+1
                    print(f'{crt}°\033[036m{i["nome"]}\033[m')
                    print(f'\033[031mAtaque: {i["atk"]}\033[m')
                    print(f'\033[032mDefesa: {i["dfs"]}\033[m')
                    print('\n',end='')
                c=int(input(f'Escolha a sua carta 1/{len(usu)}'))
                if c>len(usu) or c==0:
                    print('\033[031mnão existe essa carta escolha uma válida\033[m')
                else:
                    carusu=usu[c-1]
                    print(f'A carta escolhida foi:\n\033[036m{carusu["nome"]}\033[m\n\033[031mAtaque={carusu["atk"]}\033[m\n\033[032mDefesa={carusu["dfs"]}\033[m')
                    print(carpc)
                    if acaopc=='A':         
                        dano=carpc['atk']-carusu['dfs']
                        print(dano)
                        if dano>0:
                            print('Pc venceu')
                            vpc=vpc+1
                            usu.pop(c-1)
                            carpc['atk']=dano
                        if dano==0:
                            print('Empatou')
                            carpc['atk']=carusu['def']=0
                        if dano<0:
                            print('Usuario venceu')
                            vusu=vusu+1
                            pc.pop(numpc)
                            carusu['dfs']=dano*-1
                    if acaopc == 'D':
                        dano=carpc['dfs']-carusu['atk']
                        print(dano)
                        if dano<0:
                            print('usuario vence')
                            carusu['atk']=dano*-1
                            vusu=vusu+1
                            pc.pop(numpc)
                        elif dano==0:
                            print('empate')
                            carusu['atk']=carpc['dfs']=0
                        else: 
                            print('Pc venceu')
                            vpc=vpc+1
                            carpc['dfs']=dano
                            usu.pop(c-1)
                    print(f'A carta escolhida foi:\n\033[036m{carusu["nome"]}\033[m\n\033[031mAtaque={carusu["atk"]}\033[m\n\033[032mDefesa={carusu["dfs"]}\033[m')
                    print(carpc)
                    break

        if acaopc=='R':
            acaopc=acoes[randint(0,1)]
            if acaopc==0:
                print('O pc recarregou o ataque ')
                carpc['atk']=carpc['atk']+500
            else:
                print('O pc recarregou a defesa')
                carpc['dfs']=carpc['dfs']+500  
        crt=0
        rod=rod+1
