#Enunciado
# Um amigo gamer(Pessoa que gosta de jogar video game) seu gosta de comprar jogos frequentemente, e em todo final de ano tem muitos lançamentos de jogos novos.
# O seu amigo por saber que você sabe programar, pediu a você que elaborasse um programa que permitisse ele digitar a quantidade de jogos que ele estaria interessado a comprar e armezar em uma lista os correspondentes jogos.
# Após isso ele precisa inserir o nome do jogo que esta verificando o preço nas lojas, se o jogo que ele digitar nao estiver armazenado na lista pergunte ao usuário se deseja inserir o novo jogo a lista ou não
# (caso tenha sido algum erro de digitação), e então ficar inserindo o nome da loja e o respectivo preço naquela loja por meio de dicionáro até o usuário dizer que nao deseja consultar mais lojas e nem jogos.
# Ao final do programa voce deve informar para o usuário o melhor lugar e preço para comprar cada jogo e informando tambem o total que será gasto com 2 casas decimais.

import subprocess
n = int(input("Digite a quantidade de jogos que deseja comprar este mes: "))
l = []
for i in range(n):
    jogo = input("Digite o nome do jogo: ").upper()
    l.append(jogo)
d = {}
resp = "S"
while resp == "S" :
    jogo = input("Qual jogo deseja consultar o preço? ").upper()
    if jogo not in l:
        acrescentar = input("jogo não encontrado, deseja acrescentar ele em sua lista? ").upper()
        if acrescentar == "S":
            l.append(jogo)  
    op = "S"
    l2 = []
    while op == "S" and jogo in l and jogo not in l2:    
        loja = input("Digite o nome do loja: ")
        preco = float(input("Digite o preço do jogo %s na loja %s "%(jogo,loja)))
        l2.append([loja,preco])
        op = input("Deseja inserir outra loja? ").upper()
    if op != "s":
        d[jogo] = l2   
    resp = input("Deseja inserir outro jogo? ").upper()
    subprocess.call("cls", shell=True)

total = 0 

for jogoo in d:
    AuxPreco = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    AuxLoja = ""
    for lista in d[jogoo]:       
        if lista[1] < AuxPreco:
            AuxLoja = lista[0]    
            AuxPreco = lista[1]
    print("O melhor lugar para você comprar o jogo %s é na loja %s com o preço de: R$%.2f Reais"%(jogoo,AuxLoja,AuxPreco))          
    total += AuxPreco
print("e o total que voce vai gastar com jogos esse mes é: %.2f"%total)
