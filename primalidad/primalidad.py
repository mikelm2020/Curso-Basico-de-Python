def es_primo(parameter_number):
    found_divisor = False
    i = 2
    while i <= parameter_number/2 and not found_divisor:
        if parameter_number % i == 0:
            found_divisor = True
        i +=1

    if not found_divisor and numero > 1:
        return True
    else:
        return False

 





def run():
    variable_number = int(input('Write a number: '))
    if es_primo(variable_number):
        print('Is primo')
    else:
        print('Not is primo')




if __name__ == '__main__':
    run()