# Un programita más 

pizzaPrice, refrescoPrice = 100, 15


print("\tLAS SUPER PIZZAS")
nombre = input("Introduce tu nombre: ")
pizza = int(input("Número de pizzas: "))
refresco = int(input("Número de refrescos: "))
total = (pizza*pizzaPrice)+(refresco*refrescoPrice)
print("Estimado: " + str(nombre) + " nos debes un total de  " + str(total))