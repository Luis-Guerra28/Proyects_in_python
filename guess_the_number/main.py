import random, time

def main():

    print('Que dificultad deseas: \nFacil (f), \nMedio (m) \nDificil (d)')
    difficulty = input('').lower()
    attempts = 1
    limit = 0

    if difficulty == 'f':
        limit = 10
    elif difficulty == 'm':
        limit = 100
    elif difficulty == 'd':
        limit = 1000
    
    number = random.randint(0, limit)

    #Inicio del juego
    start = time.time() 

    while True:
        try:
            answer = int(input('Intenta adivinar el número: '))
        
            if answer == number:
                print('Has adivinado. ¡Enhorabuena!')
                print(f'Tiempo:    {int(time.time() - start)} segundos')
                print(f'Intentos:  {attempts}')
                break
            elif answer > number:
                print('Muy ALTO, vuelve a intentar.')
            elif answer < number:
                print('Muy BAJO, vuelve a intentar.')
        except:
            print('Que es esto!? Coloca un número baboso!')
    
        attempts += 1



if __name__ == '__main__':
    main()
