print('Enter first operand:')
operand1 = float(input())
print('Enter second operand:')
operand2 = float(input())
#operand 1 and 2 are the numbers being plugged into the calculator
print('Calculator Menu')
print('---------------')
# --------------- is just for looks i guess
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
#1, 2, 3, 4 will perform +, -, *, / respectively
print('Which operation do you want to perform?')
function = int(input())
#anything other than 1 through 4 will recieve error message
err = 'Error: Invalid selection! Terminating program.'
# error message
add = operand1 + operand2
sub = operand1 - operand2
mult = operand1 * operand2
if function == 1:
    print('The result of the operation is' , str(add) + '.' , 'Goodbye!')
if function == 2:
    print('The result of the operation is' , str(sub) + '.' , 'Goodbye!')
if function == 3:
    print('The result of the operation is' , str(mult) + '.' , 'Goodbye!')
if function == 4:
    try:
        div = operand1 / operand2
    except ZeroDivisionError:
        print(err)
    print('The result of the operation is' , str(div) + '.' , 'Goodbye!')
if function > 4:
    print(err)
if function < 1:
    print(err)



