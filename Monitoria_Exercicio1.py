# Enunciado
# Em cybersegurança a criação de senhas tem um código chamado hash, este hash pode ser quebrado caso sua senha seja fraca, por isso em muitos casos é preciso mascarar o Hesh , que seria mudando alguns
# fatores dele e acrescentando outros sabendo disso. Elabore um programa em python que permita o usuário criar um usuário e uma senha está senha deve ter mais de 8 caracteres e um " "(espaço), caso contrário o usuário deverá
# digitar a senha novamente, e para confirmar que sua senha é a que voce quer mesmo,pede-se para voce digita-la novamente caso esteja diferente da primeira será preciso escrever desde a primeira, após isso
# o site deverá informar para você por meio de um PROCEDIMENTO se sua senha é:
# Muito Fraca (menos de 10 pontos ) 
# Fraca ( menos de 12 pontos )
# Regular ( de 12 á 18 pontos )
# Forte ( 19 á 25 pontos )
# Muito Forte (26 ou mais pontos) 
# baseada na Função CalcularPontuação :
# Para cada letra minuscula : 0.5 ponto
# Para cada letra maiuscula : 2 pontos
# Para cada numero : 3 pontos pontos
# Para cada caracter especial(demais que nao sejam letras e numeros): 4 pontos
# após isso deverá ser perguntado para o usuário se ele deseja imprementar um Hash á sua senha, caso a resposta seja não deverá ser exibida uma mensagem que ele será hackeado facilmente
# , caso a resposta seja sim, você como um programador deverá chamar a 
# Procedimento Criptografia 
# epegar metade dos caracter pro final da senha e mudar para 3 letras acima CASO A LETRA SEJA MINUSCULA (Lembre-se de que ao soma 3 em x deve retornanr "A", y deve retornanr "B" e z deve retornar "C".
# após isso deve-se acrescentar no final da senha um numero aleátorio de 0 á 100,um espaço e uma letra Grande Aleátoria. Feito isso deve-se chamar novamente a função CalcularPontuação e falar se a senha será
# 2
# bem como informando a quantidade de pontos anterior e a nova.
# Dica : para usar numeros aleatorios import "from random import randint" randint( intervalo 1,intervalo 2)


#importação Dos Módulos
from random import randint
#Definição Das Funções/Procedimentoss:
def CalcularPontuação(senha):
    pontuação = 0
    for c in senha:
        if ord(c) >= 97 and ord(c) <= 122:
            pontuação += 0.5
        elif ord(c) >= 65 and ord(c) <= 90:
            pontuação += 2
        elif ord(c) >= 48 and ord(c) <= 57:
            pontuação += 3
        else:
            pontuação += 4
    return pontuação

def Tabela(pontuação):
    if pontuação < 10:
        print("sua senha é muito fraca ")
    elif pontuação <= 11:
        print("sua senha é fraca ")
    elif  12 <= pontuação <= 18:
        print("sua senha é regular ")
    elif 19 <= pontuação <= 25:
        print("sua senha é forte ")
    else:
        print("sua senha é muito forte ")
        
def Criptografia(senha):
    SenhaNova = ""
    for c in senha:
        if ord(c) >= 97 and ord(c) <= 122:
            if c == "x":
                c = "A"
            elif c == "y":
                c = "B"
            elif c == "z":
                c = "C"     
            else:
                c = chr(ord(c)-29)
            SenhaNova += c
    LetraAleatória = randint(65,90)
    LetraAleatória = chr(LetraAleatória)
    NumeroAletório = randint(0,100)
    NumeroAletório = str(NumeroAletório)
    SenhaNova += LetraAleatória+" "+NumeroAletório
    print("o hesh gerado será %s"%SenhaNova)
    PontosNovos = CalcularPontuação(SenhaNova)
    print("A sua nova pontuação é %.2f"%PontosNovos)
    Tabela(PontosNovos)
    
#Programa Principal
print("Bem vindo ao site da mauá. Crie seu usuário agora: ")
nome = input("Digite o nome do seu usuário: ")
senha = " "
senha2 = ""
tamanho = len(senha)
f = -1

while tamanho < 8 and (senha2 != senha ) or f == -1:
    senha = input("Digite sua senha[ >= 8 caracteres com " "]: ")
    tamanho = len(senha)
    f = senha.find(" ")
    if tamanho >= 8 and f != -1:
        senha2 = input("Confirme sua senha: ")
        if senha != senha2:
            tamanho = 0
    else:
        senha2 = ""
        tamanho = 0   
       
Pontos = CalcularPontuação(senha)
print("sua pontuação é %i "%Pontos)
Tabela(Pontos)
resp = input("deseja implementar um hash á sua senha?[sim/nao] ").lower()
if resp == "sim" :
    SenhaNova = Criptografia(senha)
else:
    print("Você será hackeado facilmente ")