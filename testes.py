from random import randint
cartas=[{'nome':'mago','atk':3500,'dfs':3000},{'nome':'feiticeira','atk':3000,'dfs':3500},{'nome':'lanceiro','atk':4500,'dfs':2000},{'nome':'conselheiro','atk':3500,'dfs':4000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':4000,'dfs':4000},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':4000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':3500},{'nome':'lenhador','atk':4000,'dfs':3000},{'nome':'rei','atk':2500,'dfs':5000}]
porçoes=[{'nome':'atk','ação':'+500','qua':3},{'nome':'dfs','ação':'+500','qua':3},{'nome':'imunidade','ação':'0','qua':3},{'nome':'atk','ação':'*2','qua':3},{'nome':'dfs','ação':'*2','qua':3}]
######usuario#######
cartasusu=[]
porçoesusu=[]
#######pc########
cartaspc=[]
porçoespc=[]
########Distribuição das cartas###############
for i in range (0,12):
    escolha=randint(0,len(cartas)-1)
    if i%2==0:
        cartaspc.append(cartas[escolha])
    else:
        cartasusu.append(cartas[escolha])
    cartas.pop(escolha)

for i in range(0,8):
    escolha=randint(0,len(porçoes)-1)
    porção=porçoes[escolha]
    porção['qua']=porção['qua']-1
    if i%2==0:
        porçoespc.append(porção)
    else:
        porçoesusu.append(porção)
    if porção['qua']==0:
        porçoes.pop(escolha)

for i in porçoesusu:
    i['qua']=0
for i in porçoespc:
    i['qua']=0

print(porçoes)
print('+='*30)
print(porçoespc)
print('=+'*30)
print(porçoesusu)
print('=+'*30)