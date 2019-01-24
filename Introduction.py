import math

# type defining of the variable and playing with variables.
a = 5.0
print(id(a))
a = 10
print("hello.....")
print(type(a))
print(id(a))

# locating addresses...
b = [5, 6, 7]
print(id(b))
b.append(10)
print(id(b))

# Strings...

name = input("Enter Your Name:: ")  # iNPUTTING AS NAME
print(name)
print(len(name))
print(name[2])
print(name[0:3])
print(name[-2:])

# Escape Sequence
# \'
# \"
# \\
# \n
message = 'Python "Programming"'
print(message)
message = """Python 
New Line..
Programmin"""
print(message)
# string Concatenation

lastname = input("Enter Your Last Name:: ")  # iNPUTTING AS NAME
print(lastname)
print(name + " " + lastname)

full = f"{name} {lastname}"
print("Another way of writing... \n" + full)
print(full.upper())  # converts into upper case.
print(full.find("ip"))  # finding location of specific char. Returns index number.

print("Dipesh" in full)  # returns Boolean value either true or false..
print("Patel" in full)
print(full.replace("Rafaliya", "Patel"))

# Binary representation of any number...
print(bin(a))  # binary of a = 10
print(hex(a))  # Hexadecimal of a..

x = 0b0101
print((x))  # binary num a
print(bin(x))  # binary printing of a

# complex Number...
complex = a + 5j
print(complex)  # printing complex number
y = 3
# operations
q = a + y  # addition
print(q)
w = a - y  # substraction
print(w)
e = a * y  # multiplication
print(e)
r = a / y  # division
print(r)
t = a // y  # division but only print integer value
print(t)
g = a ** y  # to the power of
print(g)
m = a % y  # remainder
print(m)

# constants variables..
PI = 3.14  # this is a var with a constant value
print(abs(PI))  # absolute value of PI
print(round(PI))  # round up value of PI
no = -8.56
print(math.floor(no))  # floor value of no
print(math.ceil(no))  # ceiling value of no

# if-elif-else loop
age = 10
if age >= 21:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# ternary operator
print("Adult" if age >= 21 else "Teenager")

# for loops
for p in "Dipesh":
    print(p)

for l in range(0, 10, 2):  # range is a kind of list...
    print(l)

answer = 10
guess = 1
while answer != guess:  # while loop for guessing
    guess = int(input("Enter your Guess::  "))
else:
    pass  # this is used to break the loop...

# defining a function ... Number is even or odd..
def evenodd(numb):
    if numb % 2 == 0:
        return "even"
    else:
        return "odd"


print("The Number is " + evenodd(20))

# printing the row at a time...
def rows(**ro):
    print(ro)


rows(name="Dipesh", id=1)

