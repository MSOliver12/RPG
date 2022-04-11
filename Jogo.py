from random import randint

cartas=[{'nome':'mago','atk':5000,'def':3000},{'nome':'feiticeira','atk':4000,'dfs':3500},{'nome':'lanceiro','atk':5000,'dfs':1000},{'nome':'conselheiro','atk':0,'dfs':5000},{'nome':'guardas','atk':500,'dfs':5000},{'nome':'Caçador','atk':5000,'dfs':3000},{'nome':'cavaleiro','atk':5000,'dfs':4500},{'nome':'princesa','atk':3000,'dfs':2000},{'nome':'dragão','atk':5000,'dfs':1000},{'nome':'flecheiro','atk':3500,'dfs':0},{'nome':'lenhador','atk':4000,'dfs':4000},{'nome':'rei','atk':2500,'dfs':4000}]
porçao=[{'atk+':500},{'dfs+':500},{'imunidade':0},{'atk2':2},{'dfs2':2}]
print(len(cartas))
for i in range(0,3):
    print(cartas[randint(0,len(cartas)-1)])
