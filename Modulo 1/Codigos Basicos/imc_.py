nome =input("Qual e o seu nome ? ")
altura = float (input ( "Qual a sua altura ? "))
peso = float (input ("Qual e o seu peso ? "))

imc = peso / (altura*altura)

if imc <= 18.5:
    print(f"(nome) esta abaixo do peso e com o imc")

elif imc <= 24.9: 
    print(f"(nome) esta com o peso normal e com o imc")

elif imc <= 29.9:
    print(f"(nome) esta com sobrepeso e com o imc")

elif imc <= 34.9: 
    print(f"(nome) esta com obesidade grau 1 e com o imc")

elif imc <= 39.9: 
    print(f"(nome) esta com obesidade grau 2 e com o imc")


else: 
    print(f"(nome) esta com obesidade grau 3 e com o imc")
