def add(a, b):
	answer = a+ b
	print(str(a) + '+' + str(b) + ' = ' + str(answer))
 
def subtract(a, b):
	answer = a - b
	print(str(a) + '-' + str(b) + ' = ' + str(answer))
 
def multiply(a, b):
	answer = a * b
	print(str(a) + '*' + str(b) + ' = ' + str(answer))
 
def divide(a, b):
	answer = a / b
	print(str(a) + '/' + str(b) + ' = ' + str(answer))
 
print('A. Addition')
print('B. Subtraction')
print('C. Multiplication')
print('D. Division')
print('E. Exit')

choice = input('Input your choice: ')

if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        add(a, b)

elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Input first number: '))
        b = int(input('Input fisecondrst number: '))
        subtract(a, b)

elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Input first number: '))
        b = int(input('Input fisecondrst number: '))
        multiply(a, b)
elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Input first number: '))
        b = int(input('Input fisecondrst number: '))
        divide(a, b)
elif choice == 'e' or choice == 'E':
        print('Program ended')
        quit()


