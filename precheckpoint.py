#1
C = int(input("Infome os graus em Celsius:"))
K = C + 273
print(K, "K")

#2
peso= float(input ("Insira seu peso em kg:"))
altura= float(input ("Insira sua altura em metros:"))
IMC = (peso / altura **2)
print ("seU IMC é", IMC)

#3
velocidade= int(input("Infome a velocidade em km/h:"))
if velocidade <= 80 :
    print("velocidade dentro do limite")
else:
    excesso = velocidade - 80
    multa = excesso * 5
    print("O valor da multa é de :", multa , "reais")

#4
Nota1 = int(input("Infome a Nota 1:"))
Nota2 = int(input("Infome a Nota 2:"))
Nota3 = int(input("Infome a Nota 3:"))

ME= (Nota1 + Nota2 + Nota3) / 3
MA=  (Nota1 + Nota2 * 2 + Nota3 * 3)/ 7
print(MA)

#5
salario= float(input("Informe seu salario"))
print("seu novo salario será-")
print( "Gerente:", (salario * 0.1)+ salario)
print("Engenheiro:" , (salario * 0.2)+salario)
print("Tecnico:", (salario * 0.3)+salario)
print("Se seu cargo não stiver na tabela seu novo salario será", (salario * 0.4)+salario)

#6
pessoas=int(input("informe quantas pessoas moram na residencia:"))
minutos=int(input("Qual a media de minutos que demoram no banho"))
potChuveiroWats= 2400
kwh= 0.40


consumoBanho = ((potChuveiroWats / 1000) * minutos) / 60 # energia em kwh
consumoMes = consumoBanho * pessoas * 30
valor = consumoMes * kwh
print (consumoMes, "Kwh")
print(valor, "reais")

#7
produtos = {
    1001: {"preco_unitario": 5.32, "imposto": 0.18},
    1324: {"preco_unitario": 6.45, "imposto": 0.18},
    6548: {"preco_unitario": 2.37, "imposto": 0.06},
    987:  {"preco_unitario": 5.32, "imposto": 0.06},
    7623: {"preco_unitario": 6.45, "imposto": 0.12}
}

codigo_produto = int(input("Digite o código do produto(1001, 1324, 6548, 987, 7623): "))
quantidade = int(input("Digite a quantidade comprada: "))


if codigo_produto in produtos:
    preco_unitario = produtos[codigo_produto]["preco_unitario"]
    imposto_percentual = produtos[codigo_produto]["imposto"]
    
    valor_produto = preco_unitario * quantidade
    
    valor_imposto = valor_produto * imposto_percentual
 
    valor_total = valor_produto + valor_imposto
    
  
    print(f"Valor do produto: R${valor_produto:.2f}")
    print(f"Valor do imposto: R${valor_imposto:.2f}")
    print(f"Valor total a pagar: R${valor_total:.2f}")
else:
    print("Código de produto inválido.")

