dolars = input("¿How much dolars has?: ")
dolars = float(dolars)
dolar_value = input("How much is the dolar value now?: ")
dolar_value = float(dolar_value)
mexican_pesos = dolars * dolar_value
mexican_pesos = round(mexican_pesos,2)
mexican_pesos = str(mexican_pesos)
print("Has $" + mexican_pesos + " mexican pesos")