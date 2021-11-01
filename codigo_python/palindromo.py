def palindromo(palabra):
    #remplaza los espacios por nulos
    palabra = palabra.replace(' ', '')
    #convierte a minisuculas la palabra
    palabra = palabra.lower()
    #obtiene la palabra invertida
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()