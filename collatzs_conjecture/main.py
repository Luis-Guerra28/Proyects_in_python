import random

def randomNumber():
    return str(random.randint(0,9))

def randomChar(string):
    return string[random.randint(0, len(string)-1)]



def main():





    TYPE = ['N', 'S', 'May', 'Min']
    SYMBOLS = '!@#$%^&*?.+=_'
    MAYUS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MINUS = 'abcdefghijklmnopqrstuvwxyz'
    password = []
    length = int(input('Introduzca el tamaño de la contraseña: '))

    password.append(randomNumber())
    password.append(randomChar(SYMBOLS))
    password.append(randomChar(MAYUS))
    password.append(randomChar(MINUS))

    if length == 4:
        random.shuffle(password)
        print(''.join(password))
        return 
    elif (length > 4) and (length <= 50): 
        for _ in range(length-4):
            rndm = random.choice(TYPE)
            if rndm == 'N':
                password.append(randomNumber())
            elif rndm == 'S':
                password.append(randomChar(SYMBOLS))
            elif rndm == 'May':
                password.append(randomChar(MAYUS))
            elif rndm == 'Min':
                password.append(randomChar(MINUS))
        
        random.shuffle(password)
        print(''.join(password))
        return

    elif (length > 50): 
        print('Error: Size limit exceeded')
        return
    else:
        print(f'Error: {length} is not a valid value ')
        return


if __name__ == '__main__':
    main()