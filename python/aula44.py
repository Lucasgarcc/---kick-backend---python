#Esturuta de condição

idade = ((int(input("Digite seu idade: "))))

if (idade < 20):
    print("jovem")
elif idade >= 20 and idade < 65:
    print("adulto")
else:
    print("idoso!")

login = input("Login: ")
senha = input("senha: ")

if senha == "true" or senha == "v":
    print("login executado")
elif senha != "true" or "v" :
    print("senha incorreta")


ano = (int(input("Digite sua data de nascimento: ")))

votar = 2005

if ano > votar :
    input("você está abto a votar!")
else : 
    input("você está novo ainda!")


total = 0
valorMaca = 0

quantidade = int(input("difite a quantidade de maça: "))

if quantidade < 12:
    valorMaca = 0.3
    total = float(valorMaca * quantidade)
    print("valor da maça: " , valorMaca, "R$")
    print("valor da total: " , total, "R$")
elif quantidade >= 12:
    valorMaca = 0.25
    total = float(valorMaca * quantidade)
    print("valor da maça: " , valorMaca, "R$")
    print("valor da total: " , total, "R$")    