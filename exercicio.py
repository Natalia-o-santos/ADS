# exercicio 1
print ("Olá Mundo")
 
# exercicio 2
numero= int (input ("Insira um numero:"))
print ("O numero informado foi", numero)
 
#exercicio 3
a= int (input ("Insira um numero:"))
b= int(input ("Insira um numero:"))
print ( a+b)
 
#exercicio 4
nota1 =int (input ("Insira a nota do 1°bimestre:"))
nota2 =int (input ("Insira a nota do 2°bimestre:"))
nota3 =int (input ("Insira a nota do 3°bimestre:"))
nota4 =int (input ("Insira a nota do 4°bimestre:"))
media = (nota1 + nota2 + nota3 + nota4)/ 4
print (media)
 
#exercicio 5
a = int (input ("Insira um valor em metros:"))
print (a * 100, "cm")
 
#exercicio 6
raio= int(input("Informe o raio do circulo"))
area= print(raio ** 2 * 3.14)
 
#exercicio 7
lado = int(input("Informe o lado do quadrado"))
area = lado ** 2
print ( " Area do quadrado:", area)
 
#exercicio 8
valorHora = int(input("Informe quanto você ganha por hora:"))
horasMes = int(input("Informe quantas horas você trabalhou"))
salario = (valorHora * horasMes)
print (" Salario : R$", salario)
 
#exercicio 9
F = int(input("Informe os graus em Fahrenheit:"))
C =5 * ((F - 32)/ 9)
print ("Graus Celsius :", C)
 
#exercicio 10
C = int(input("Informe os graus em Celsius:"))
F= (C * 1.8) + 32
print ("Graus fahrenheit :", F)
 
#exercicio 11
numero1 = int (input ("Insira um numero inteiro:"))
numero2 = int (input ("Insira um numero inteiro:"))
numero3 = float (input ("Insira um numero real:"))
 
resultado1 = (numero1 * 2) * (numero2 / 2)
print (resultado1 )
 
resultado2 = (3 * numero1 ) + numero3
print (resultado2)
 
resultado3 = numero3 ** 3
print (resultado3)
 
#exercicio 12
altura= float(input ("Insira sua altura em metros:"))
pesoIdeal = (72.7 * altura) - 58
print ("o peso ideal é :", pesoIdeal ,"kg")
 
#exercicio 13
 
altura= float(input ("Insira sua altura em metros:"))
pesoIdealHomem = (72.7*altura) - 58
pesoIdealMulher = (62.1*altura) - 44.7
 
print("seu peso ideal sendo homem é: ", pesoIdealHomem, "Kg , e sendo mulher é de: ", pesoIdealMulher, "kg")

#exercicio 14
kilosPeixe = int(input("kilos de peixe:"))
if kilosPeixe <= 50:
    print("você não exedeu o limite de peso") 
else:
    excesso = kilosPeixe -50
    multa= excesso * 4
    print("a multa a ser paga é de R$  ", multa )

#exercicio 15 
salario = int(input('quanto você ganha por hora: '))
horas = int(input('e quantas horas você trabalha no mês: '))

salarioBruto = salario * horas
print(f'seu salário no mês é {salarioBruto}')

renda = 0.11
inss = 0.08
sindico = 0.05

comRenda = salarioBruto * renda
comInss = salarioBruto * inss
comSindico = salarioBruto * sindico
todosImpostos = comSindico + comInss + comRenda
salarioLiquido = salarioBruto - todosImpostos

print(f'você tem o desconto de R${todosImpostos} e o seu salario liquido é R${salarioLiquido}')

# exercico 16
metros = int(input("quantos metros quarados seram pintados? : "))
litros = metros * 3
lata =  litros / 18
preco = 80
qntdLata = print ("Deverá ser comprado ", lata, "latas , com  valor total de R$", (preco * lata ))

#exercicio 17
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
        
litros_necessarios =(area * 1.10 / 6)

lata_litros = 18
lata_preco = 80
galao_litros = 3.6
galao_preco = 25
        
latas_necessarias = (litros_necessarios / lata_litros)
preco_latas = latas_necessarias * lata_preco
galao_necessarios = (litros_necessarios * 6 / galao_litros)
preco_galoes = galao_necessarios * galao_preco

latas = litros_necessarios // lata_litros
resto_litros = litros_necessarios % lata_litros
galao_necessarios_mistura = (resto_litros * 6 / galao_litros)
preco_mistura = (latas * lata_preco) + (galao_necessarios_mistura * galao_preco)
        

print(f"Para uma área de {area:.2f} m², com 10% de folga:")
print(f"1. Apenas latas de 18 litros: {latas_necessarias} latas, R$ {preco_latas:.2f}")
print(f"2. Apenas galões de 3,6 litros: {galao_necessarios} galões, R$ {preco_galoes:.2f}")
print(f"3. Mistura de latas e galões: {latas} latas e {galao_necessarios_mistura} galões, R$ {preco_mistura:.2f}")
    
#exercicio 18
tamanho_mb = float(input("Digite o tamanho do arquivo em MB: "))
        

velocidade_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))
        
tempo_minutos = (tamanho_mb / (velocidade_mbps / 8)) / 60
       
print(f"O tempo aproximado de download é {tempo_minutos:.2f} minutos.")