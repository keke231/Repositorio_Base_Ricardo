armario = []
opçao = 0 
while opçao != 3:
    opçao = int(input("digite o que deseja fazer: \n 1- abrir o armario \n 2- adicionar coisas dentro \n 3- fechar"))
    if opçao == 1:
        print(f"itens no armario: \n {armario}")
    elif opçao == 2:
        item = input("digite o nome do item que foi adicionado: \n")
        armario.append(item)        
