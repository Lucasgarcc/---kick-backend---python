
# 1 - contador 

#for x in range(10,0,-1, ):
#    print("Fim!" , x )

# 2 numeros pares
'''
for x in range(1,200 ):
    if x % 2 == 0:
        print("pares:", x)
'''
# 4 numeros impares
'''
num = (int(input(" digite numero: ")))
for x in range(1,num ):
    num 
    if num and x % 2 != 0:
        print("pares:", x)
'''
# 5  media de notas


for x in range(3):
    nota1 = int(input("nota1: " ))
    nota2 = int(input("nota2: "))
    nota3 =int(input("nota3: " ))
    media = (nota1 + nota2 + nota3 )/3 
    if  nota1 and nota2 and nota3 >= 6: 
        print(" Parabêns você foi aprovado! ", media)
        print(" * Continue assim! *") 
    else:
        print(" Que pena você foi reprovaodo!" , media)
        print(" * Você precisa estudar mais  um pouco! *")