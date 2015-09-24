
def add(num1, num2):
    if validate(num1) and validate(num2)==True:
        print num1 + num2
    else:
        print 'Numbers are invalid'

def subtract(num1, num2):
    if validate(num1) and validate(num2)==True:
        print num1 - num2
    else:
        print 'Numbers are invalid'

def multiply(num1, num2):
    if validate(num1) and validate(num2)==True:
        print num1 * num2
    else:
        print 'Numbers are invalid'

def divide(num1, num2):
    if validate(num1) and validate(num2)==True:
        print num1 / num2
    else:
        print 'Numbers are invalid'

def power(num1, num2):
    if validate(num1) and validate(num2)==True:
        result = 1
        for x in range(num2):
            result = result * num1
            print result
    else:
        print 'Numbers are invalid'

def square(num1):
    if validate(num1)==True:
        print power(num1, 2)
    else:
        print 'Number is invalid'

def cube(num1):
    if validate(num1)==True:
        print power(num1, 3)
    else:
        print 'Number is invalid'

def mod(num1, num2):
    if validate(num1) and validate(num2)==True:
        print num1 % num2
    else:
        print 'Numbers are invalid'

def validate(num1):
    if type(num1)==int :
        return True      
    else:
        return False 

"""def get_operation(operation):
    switcher = {
        '+': add,
        '-': subract,
        '*': multiply,
        '/': divide,
        'square':square,
        'cube': cube,
        'pow': power,
        'mod': mod

    }
    """

expression = raw_input("Enter your expression: ")
expression = expression.rstrip() 
list_nums = expression.split(" ")
operation = list_nums[0]
num1 = int(list_nums[1])

if len(list_nums) == 3:
    num2 = int(list_nums[2])


print 'operation :%s' % operation
if operation == '+':
    add(num1,num2)
elif operation == '-':
    subtract(num1, num2)
elif operation == '*':
    multiply(num1, num2)
elif operation == '/':
    divide(num1, num2)
elif operation == 'square':
    square(num1)
elif operation == 'cube':
    cube(num1)
elif operation == 'pow':
    power(num1, num2) 
elif operation == 'mod':
    mod(num1, num2)
else:
    print 'Cannot perform operation'
