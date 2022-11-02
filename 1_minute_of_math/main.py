import random, time

def get_divisor(n):
    divisors = []

    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)

    return random.choice(divisors)


def main():
    START_TIME = time.time()
    TIME_LIMIT = 60
    OPERATIONS = ['+', '-', '*', '/']
    answers = []
    count = 0
    correct = 0


    while True:
        count+=1
        x = random.randint(1, 99)
        op = random.choice(OPERATIONS)
        
        if op == '/':
            y = get_divisor(x)
            result = x / y
        
        elif op == '+':
            y = random.randint(1, 99)
            result = x + y
        
        elif op == '-':
            y = random.randint(1, 99)
            result = x - y
        
        elif op == '*':
            y = random.randint(1, 99)
            result = x * y

        
        print(f"{x}{op}{y} = ", end='')
        
        answer = int(input())

        answers.append(f"{x}{op}{y} = {answer}")

        if answer == result:
            correct+=1

        
        if time.time() - START_TIME > TIME_LIMIT:
            break
        else:
            if answer == result: 
                print(f'CORRECTO, quedan {TIME_LIMIT - int(time.time() - START_TIME)}')
            else: 
                print(f'INCORRECTO, quedan {TIME_LIMIT - int(time.time() - START_TIME)}')

    print('\n' + '-'*70)
    print(f'{count} respondidas, el porcentaje de acierto es {int(correct / count * 100)}%')
    
    for a in answers:
        print(a)


if __name__ == '__main__':
    main()
