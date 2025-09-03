def calc():
    '''The function defines the calculator'''
    number1 = float(input("Enter the number1 :"))
    number2 = float(input("Enter the number2 :"))
    op = input("Enter the operation to be performed (+,-,*,/) :")
    if op == '+':
        result = number1 + number2
    elif op == '-':
        result = number1 - number2
    elif op == '*':
        result = number1 * number2
    elif op == '/':
        if number2 == 0:
            result = 'Zero Division error.'  
        else:
            result = number1 / number2
    else:
        result = 'Invalid operation' 

    return result   

if __name__ == '__main__':
    print(calc())

