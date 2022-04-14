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
crt=rod=vusu=vpc=0

################ distribuição de cartas #######################
p=i=0
print(len(cartas))
for c in range(0,12):
    carta=cartas[randint(0,len(cartas)-1)]
    pos=cartas.index(carta)
    carta['nome']=carta['nome'].upper()
    if c%2==0:
        usu.append(carta)
    else:
        pc.append(carta)
    cartas.pop(pos)

for i in range(0,8):
    porçao=porçoes[randint(0,len(porçoes)-1)]
    pos=porçoes.index(porçao)
    porçao['qua']=porçao['qua']-1
    if i%2==0:
        usupor.append(porçao)
    else:
        pcpor.append(porçao)
    if porçao['qua']==0:
        porçoes.pop(pos)

for i in usupor:
    i['qua']=0
    i['nome']=i['nome'].upper()
for i in pcpor:
    i['qua']=0
    i['nome']=i['nome'].upper()

################# Fim da distribuição ########################


############### Porção de ataque pro pc ######################
usapor=randint(0,1)
if len(defpc)>0:
    qualpor=randint(0,len(defpc)-1)
    pcesc=defpc[qualpor]
if usapor==0 or len(defpc)==0:
    print('\033[031mO pc não usou porção de defesa\033[m')
else:
    print('\033[032mO pc usou uma porção de defesa\033[m ')
    ação=(pcesc['ação'])
    if '+' in ação:
        carpc['dfs']=carpc['dfs']+int(ação)
    if '*' in ação:
        ação=ação.replace('*','')
        carpc['dfs']=carpc['dfs']*int(ação)
    if ação==0:
        combate=0
    defpc.pop(defpc.index(pcesc))
    pcpor.pop(pcpor.index(pcesc))