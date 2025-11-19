# we are gonna make a inventory, we had something rules

names = "nombre"
price = "precio"
quantity = "cantidad"

# to make a system from inventory we need: to aks our user name, prices and quantity of products
ListaDeProductos = []
#una forma practica de pedir informacion y guardarla es con un diccionario, pero debe quedar claro en este caso que diccionario debe quedar poe fuera de la funcion 
diccionario = {
    
}
ListaDeProductos.append(diccionario)

names = input("please user, type the product name: ").capitalize().title()
diccionario["name"] = names
# since it's necesary be clair with the user about what value need to type we put a cuple rules
# we make a tool and we use try and except, and we print a menssage if the user type a wrong value
while True:
    try:
        price = float(input("please type the price of the product: "))
        diccionario["price"] = price
        if price > 0:
            break 
            
        else:
            print("los numeros deben ser positivos")
    except ValueError:
        print("ERROR, los valores deben ser solo nuericos ")
    
#And boths case we are gonna make a tool and use the commands try and except, because like a said it's necesary to be clair with our user about whay he can type and what not

while True:
    try:
        quantity = int(input("please type the quantity: "))
        diccionario["quantity"] = quantity
        break
    except ValueError:
        print("Error, please type just numeric values and positives")


# now we are let's define a mathematical function
totalvalor = price * quantity
print(f" your total for the numbers of products is:", totalvalor)

print(diccionario)