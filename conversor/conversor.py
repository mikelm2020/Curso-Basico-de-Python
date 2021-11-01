mexican_pesos = input("¿How much mexican pesos has?: ")
mexican_pesos = float(mexican_pesos)
dolar_value = input("How much is the dolar value now?: ")
dolar_value = float(dolar_value)
dolars = mexican_pesos / dolar_value
dolars = round(dolars,2)
dolars = str(dolars)
print("Has $" + dolars + " dolars")

