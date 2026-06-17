# Addition:
add1 = 54
add2 = 34
add3 = add1 + add2

# print(add3)
print(f"Addition: {add3}")


# Subtraction:
sub1 = 99
sub2 = 45

print(sub1 - sub2)
print(f"Subtraction: {sub1 - sub2}")


# Multiplication:
mul1 = 5
mul2 = 9
mul3 = 9 * 5

print(f"{mul1} x {mul2} = {mul3}")
# print(mul3)


# Division:
div_num1 = 49
div_num2 = 7

div = div_num1/div_num2
print(div)


# Modulus: It's basically the remainder after dividing the number
mod1 = 50
mod2 = 4

mod = mod1 % mod2
print(mod)


# Exponentiation: Baically square of the number
expo1 = 3
expo2 = 4

expo = expo1 ** expo2                           # 3*3*3*3
print(expo)


# Floor Division: rounds the result down to the nearest whole number
x = 15
y = 7

z = x // y
print(z)



# Calculator using user defined 
num1 = 84
num2 = 12

print(f'Addition: {num1} + {num2} = {num1 + num2}')
print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
print(f'Multiplication: {num1} x {num2} = {num1 * num2}')
print(f'Division: {num1} / {num2} = {num1 / num2}')
print(f'Modulus: {num1} % {num2} = {num1 % num2}')
print(f'Exponentiation: {num1} ** {num2} = {num1 ** num2}')
print(f'Floor Division: {num1} // {num2} = {num1 // num2}')


# Calculator using user input:
num_a = int(input("Enter the number here: "))
num_b = int(input("Enter the number here: "))

sum = num_a + num_b
print(f'Addition: {num_a} + {num_b} = {num_a + num_b}')

sub = num_a - num_b
print(f'Subtraction: {num_a} - {num_b} = {sub}')

mul = num_a * num_b
print(f'Multiplication: {num_a} x {num_b} = {mul}')

div = num_a / num_b
print(f'Division: {num_a} / {num_b} = {div}')

mod = num_a % num_b
print(f'Modulus: {num_a} % {num_b} = {mod}')

Expo = num_a ** num_b
print(f'Exponentiation: {num_a} ** {num_b} = {Expo}')

FD = num_a // num_b
print(f'Floor Division: {num_a} // {num_b} = {FD}')

