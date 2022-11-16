
def arithmetic_arranger(problems, showResult=False):

    firstLine = ''
    secondLine = ''
    thirdLine = ''
    fouthLine = ''

    if len(problems) > 5:
        print('Error: Too many problems.')
        return

    for problem in problems:
        x, op, y = problem.split()
        xSize = len(x)
        ySize = len(y)
        if (xSize > 4) or (ySize > 4):
            print('Error: Numbers cannot be more than four digits.')
            return

        if xSize > ySize:
            lineSize = max(xSize, ySize+2) + 1
        else: 
            lineSize = max(xSize, ySize+2)


        # Parte encargada del calculo del resultado -----------------
        try:
            x = int(x)
            y = int(y)
        except:
            print('Error: Numbers must only contain digits.')

        if op == '+':
            result = x+y
        elif op == '-':
            result = x-y
        else:
            print("Error: Operator must be '+' or '-'.")
            return
        #------------------------------------------------------------
        # 
        firstLine += f'{str(x):>{lineSize}}    '
        secondLine += f'{op}{str(y):>{lineSize-1}}    '
        thirdLine += "-"*lineSize + "    "
        fouthLine += f'{str(result):>{lineSize}}    '

    print(firstLine)
    print(secondLine)
    print(thirdLine)
    if showResult: print(fouthLine)
    print()


def main():
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

    arithmetic_arranger(["235 + 52" ], True)
    

if __name__ == "__main__":
    main()