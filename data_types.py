"""
1. Numeric Types
    - int = integer numbers (e.g., -10, 0, 25)
    - float = floating-point numbers (e.g., -2.5, 0.0, 3.14)
    - complex = complex numbers (e.g., 2 + 3j)

2. Boolean Type
    - bool = represents True or False values

3. Text Type
    - str = string of characters (e.g., "Hello, World!")    

4. Sequence Types
    - list = ordered, mutable collection of items (e.g., [1, 2, 3])
    - tuple = ordered, immutable collection of items (e.g., (1, 2, 3))

5. Set Types
    - set = unordered collection of unique items (e.g., {1, 2, 3})

6. Mapping Type
    - dict = collection of key-value pairs (e.g., {"name": "Alice", "age": 30})

"""

#INTEGER
#Whole numbers without decimal point
a = 10
b = -5
c = 0
print(a)
print(b)
print(c)

#To check the data type
print(type(a)) #class 'int'
print(type(b)) #class 'int'
print(type(c)) #class 'int'

#ARITHMETIC OPERATIONS ON INTEGERS
a = 15
b = 4
print(a + b)  #Addition
print(a - b)  #Subtraction
print(a * b)  #Multiplication
print(a / b)  #Division (returns float)
print(a // b) #Floor Division (returns integer)
print(a % b)  #Modulus (remainder)
print(a ** b) #Exponentiation(Power)(10^3=1000)

#Comparison Operations
x = 10
y = 20
print(x == y)  #Equal to
print(x != y)  #Not equal to
print(x > y)   #Greater than
print(x < y)   #Less than
print(x >= y)  #Greater than or equal to
print(x <= y)  #Less than or equal to

#Type Conversion(Casting)
#float to int
f1 = 10.5
f2 = -3.7

print(int(f1)) #10
print(int(f2)) #-3

#string to int
s1 = "25"
s2 = "-7"
print(int(s1)) #25
print(int(s2)) #-7

#invalid string to int
s3 = "Hello"
# print(int(s3)) #ValueError: invalid literal for int() with base 10
a="10.5"
# print(int(a)) #ValueError: invalid literal for int() with base 10

#FLOAT
#Numbers with decimal point
x = 10.5
y = -3.14
z = 0.0
print(x)
print(y)
print(z)
print(type(x)) #class 'float'
print(type(y)) #class 'float'
print(type(z)) #class 'float'

#ARITHMETIC OPERATIONS ON FLOATS
a = 5.5
b = 2.0
print(a + b)  #Addition
print(a - b)  #Subtraction
print(a * b)  #Multiplication
print(a / b)  #Division
print(a // b) #Floor Division
print(a % b)  #Modulus
print(a ** b) #Exponentiation
#Always get float as result

#Mixed Operations
x = 10    #int
y = 3.5   #float
print(x + y)  #Addition
print(x - y)  #Subtraction
print(x * y)  #Multiplication
print(x / y)  #Division
#Output will be float

#Comparison Operations
p = 7.5
q = 10.0
print(p == q)  #Equal to
print(p != q)  #Not equal to
print(p > q)   #Greater than
print(p < q)   #Less than
print(p >= q)  #Greater than or equal to
print(p <= q)  #Less than or equal to

#Type Conversion(Casting)
#int to float
i1 = 10
i2 = -5
print(float(i1)) #10.0
print(float(i2)) #-5.0
#string to float
s1 = "12.34"
s2 = "-7.89"
print(float(s1)) #12.34
print(float(s2)) #-7.89
#invalid string to float
s3 = "World"
# print(float(s3)) #ValueError: could not convert string to float: 'World
s4 = "156abc"
# print(float(s4)) #ValueError: could not convert string to float: '15.6abc'

#built-in functions for floats
pi = 3.14159
print(round(pi))      #Rounds to nearest integer
print(round(pi, 2))   #Rounds to 2 decimal places

#precision issues
a = 0.1 + 0.2
print(a)              #0.30000000000000004
print(round(a, 2))  #0.3    

"""COMPLEX NUMBERS (complex) IN PYTHON

Complex number: a + bj
a → real part (int or float)
b → imaginary part (int or float)
j → imaginary unit (√-1)

Creating complex numbers

z1 = 2 + 3j real = 2, imaginary = 3
z2 = -1 - 4j
z3 = 5.0 + 0j real part float
z4 = 0 + 2j only imaginary

print(z1, z2, z3, z4)

Check data type
print(type(z1)) <class 'complex'>

Accessing real and imaginary parts
print(z1.real) 2.0
print(z1.imag) 3.0

print(z2.real) -1.0
print(z2.imag) -4.0

BASIC OPERATIONS WITH COMPLEX NUMBERS

a = 2 + 3j
b = 1 - 4j

Addition
print(a + b) (3-1j)

Subtraction
print(a - b) (1+7j)

Multiplication
print(a * b) (14-5j)

Division
print(a / b) (-0.5882352941176471 + 0.6470588235294118j) approx

Conjugate of a complex number
For z = a + bj, conjugate is a - bj
z = 3 + 4j
print(z.conjugate()) (3-4j)

Mixing with int and float

x = 5 int
y = 2.5 float
z = 3 + 4j complex

print(x + z) (8+4j)
print(y + z) (5.5+4j)

Note: if you mix int/float with complex, result becomes complex

Using complex numbers in simple examples

Example 1: Electrical engineering (impedance)

r = 4 resistance (real part)
x_react = 3 reactance (imaginary part)
impedance = complex(r, x_react) 4 + 3j
print("Impedance:", impedance)

Example 2: Distance from origin in complex plane

point = 3 + 4j
distance = abs(point) same as sqrt(3^2 + 4^2)
print("Distance from origin:", distance) 5.0
"""

#String Data Type (str)
#Strings are sequences of characters enclosed in single quotes(' '), double quotes(" "), or triple
empty_string = ""

#multi line string using triple quotes
multi_line_string = """This is a multi-line
string that spans multiple lines."""    
print(empty_string)
print(multi_line_string)
print(type(empty_string)) #class 'str'
print(type(multi_line_string)) #class 'str'
#single quote string and double quote string
single_quote_str = 'Hello, World!'
double_quote_str = "Python is awesome!"
print(single_quote_str)
print(double_quote_str)
