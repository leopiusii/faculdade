n1 = float (input("Digite a nota da sua prova 1: "))
n2 = float (input("Digite a nota da sua prova 2: "))
n3 = float (input("DIgite a nota da sua prova 3: "))
m = (float(n1 + n2 + n3) /3)
f = float (input("Você teve 10 aulas, em quantas compareceu? "))
f = float(f*10)
print ("Sua frequência é: " + str (f))
if m >= 7.0 and f>=70:
    print ("Você está aprovado, sua média é: " + str(m), "e sua frequência é: " + str (f))
else:
    print ("Você está reprovado, sua média é: " + str(m), "e sua frequência é: " + str (f))
notas = [n1, n2, n3]
oi = max(notas)
print ("A sua maior nota foi: " + str (oi))
a = input ("Deseja fechar o programa? Digite sim por favor, não sei mais o que por nesse programa ")
if a == 'sim':
    exit()
else:
    print ("Mandei digitar sim amigo")
    exit()
    


    
