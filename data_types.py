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

#length of string
str1 = "Hello"
print(len(str1)) #5
str2 = "Python Programming"
print(len(str2)) #18

#indexing
#it is to get position of character in string
sample_str = "Python"
print(sample_str[0])  #P
print(sample_str[3])  #h
print(sample_str[2])  #n
print(sample_str[4])  #IndexError: string index out of range
#indexing starts from 0

first_char = sample_str[0]
second_char = sample_str[1]
third_char = sample_str[2]  
fourth_char = sample_str[3]
last_char = sample_str[4]
print(first_char)  #P
print(second_char) #y
print(third_char)  #t
print(fourth_char) #h
print(last_char)   #n
#last index is length-1
#P -- 0
#y -- 1
#t -- 2
#h -- 3
#o -- 4
#n -- 5

#negative indexing
print(sample_str[-1]) #n
print(sample_str[-3]) #h
print(sample_str[-6]) #P
#-1 refers to last character
first_char_neg = sample_str[-6]
second_char_neg = sample_str[-5]
third_char_neg = sample_str[-4]
fourth_char_neg = sample_str[-3]
last_char_neg = sample_str[-1]
print(first_char_neg)  #P
print(second_char_neg) #y
print(third_char_neg)  #t
print(fourth_char_neg) #h
print(last_char_neg)   #n

#P -- 0 -- -6
#y -- 1 -- -5
#t -- 2 -- -4
#h -- 3 -- -3
#o -- 4 -- -2
#n -- 5 -- -1

#changin case of string
text = "Hello, World!"
print(text.upper()) #HELLO, WORLD! upper case
print(text.lower()) #hello, world! lower case
print(text.capitalize()) #Hello, world! first letter capitalized
print(text.title()) #Hello, World! first letter of each word capitalized

#removing whitespace
text_with_spaces = "   Hello, Python!   "
stripped_text = text_with_spaces.strip()
print(stripped_text) #"Hello, Python!" without leading/trailing spaces

#removing leading whitespace
leading_stripped = text_with_spaces.lstrip()
print(leading_stripped) #"Hello, Python!   " without leading spaces     

#removing trailing whitespace
trailing_stripped = text_with_spaces.rstrip()
print(trailing_stripped) #"   Hello, Python!" without trailing spaces   

#finding substrings
main_str = "Hello, Hello welcome to Python programming."
#finding first occurrence of substring
#case-sensitive
#return -1 if not found

index = main_str.find("Python")
print(index) #18 
index_not_found = main_str.find("Java")
print(index_not_found) #-1

#replacing substrings
#it need 2 parameters: old substring and new substring
#replacing all occurrences of a substring with another substring
original_str = "I like apples. Apples are my favorite fruit."
#case-sensitive
new_str = original_str.replace("apples", "oranges")
print(new_str) #"I like oranges. Apples are my favorite fruit."

#5 bucket
#bucket 5.1
#check if all characters are alphabetic
str_alpha = "HelloWorld"
print(str_alpha.isalpha()) #True
str_alpha_num = "Hello123"
print(str_alpha_num.isalpha()) #False
print("Hello World".isalpha()) #False (space is not alphabetic)

#check if all characters are numeric
str_numeric = "12345"
print(str_numeric.isdigit()) #True
str_mixed = "123abc"
print(str_mixed.isdigit()) #False
print("5 bucket".isdigit()) #False

#check if all characters are alphanumeric (letters and numbers only no special characters)
#returns True if all characters are alphanumeric and there is at least one character
#otherwise False
#returns False for empty string
str_alnum = "Hello123"
print(str_alnum.isalnum()) #True
str_special = "Hello@123"
print(str_special.isalnum()) #False
print("5bucket".isalnum()) #True

#bucket 5.2
#isupper() method and islower() method
upper_str = "HELLO"
lower_str = "hello"
mixed_str = "Hello"
print(upper_str.isupper()) #True
print(lower_str.islower()) #True
print(mixed_str.isupper()) #False
print(mixed_str.islower()) #False
print("5BUCKET".isupper()) #True
print("5bucket".islower()) #True
#special example
special_str = "HELLO123!"
print(special_str.isupper()) #True (numbers and special characters are ignored)
special_str2 = "hello@world"
print(special_str2.islower()) #True (numbers and special characters are ignored)


#isspace() method
space_str = "   "
non_space_str = " Hello "
empty_str = ""
print(space_str.isspace()) #True
print(non_space_str.isspace()) #False
print(empty_str.isspace()) #False
print(" \t\n".isspace()) #True (contains only whitespace characters)

#bucket 6

#6.1
#splitting strings
#when we split a string, it returns a list of substrings
#when there  is no separator specified, !!!!!!!!!!!!!!! it splits on whitespace by default !!!!!!!!!!!!!!!!!!!

sentence = "Python is a great programming language"
words = sentence.split() #splitting on whitespace
print(words) #['Python', 'is', 'a', 'great', 'programming', 'language'] 

#splitting with a specific separator
csv_data = " apple,bananacherry,date"
fruits = csv_data.split(",") #splitting on comma
print(fruits) #['apple', 'banana', 'cherry', 'date']    

data = "one;two;three;four;five"
items = data.split(";") #splitting on semicolon
print(items) #['one', 'two', 'three', 'four', 'five']

#6.2
#joining strings
#when we join a list of strings, it combines them into a single string with a specified separator
#we can specify any string as separator
#it does not add space by default

words_list = ['Python', 'is', 'fun']
sentence_joined = " ".join(words_list) #joining with space as separator write the joiner string in double quotes in front of join function
print(sentence_joined) #"Python is fun"
csv_joined = ",".join(fruits) #joining with comma as separator
print(csv_joined) #"apple,banana,cherry,date"
semicolon_joined = ">>>>>".join(items) #joining with semicolon as separator
print(semicolon_joined) #"one;two;three;four;five"

#joining without any separator
no_space_joined = "".join(words_list) #joining without any separator
print(no_space_joined) #"Pythonisfun"


#bucket 7

#starting and ending substrings

main_string = "Hello, welcome to Python programming."

#check if string starts with a substring

print(main_string.startswith("Hello")) #True
print(main_string.startswith("welcome")) #False

#check if string ends with a substring

print(main_string.endswith("programming.")) #True
print(main_string.endswith("Python")) #False

#bucket 8
#counting occurrences of a substring
#it counts number of times a substring appears in the string
#case-sensitive
#non-overlapping occurrences are counted
text = "banana"
count_a = text.count("a")
print(count_a) #3
text2 = "Python programming in Python is fun"
count_python = text2.count("Python")
print(count_python) #2
count_java = text2.count("Java")
print(count_java) #0



#slicing strings
#syntax: string[start:end:step]
#string is cake 
cake = "Chocolate Cake"
#extracting substring "Chocolate"
substr1 = cake[0:9] #from index 0 to 8
print(substr1) #"Chocolate"
#extracting substring "Cake"
substr2 = cake[10:14] #from index 10 to 13
print(substr2) #"Cake"
#last index not included
substr3 = cake[:9] #from start to index 8
print(substr3) #"Chocolate"
substr4 = cake[10:] #from index 10 to end
print(substr4) #"Cake"
substr5 = cake[:] #entire string
print(substr5) #"Chocolate Cake"
#default start is 0 and default end is length of string

#negative indexing in slicing
string = "Programming"
substr_neg1 = string[-11:-6] #from index -11 to -7
print(substr_neg1) #"Progr"
substr_neg2 = string[-5:-6] #from index -5 to -7
print(substr_neg2) #"" (empty string, as -5 is greater than -6)
substr_neg3 = string[-11:] #entire string
print(substr_neg3) #"Programming"
substr_neg4 = string[:-6] #from start to index -7
print(substr_neg4) #"Program"   

#concatenation of strings
str1 = "Hello,"
str2 = "World!"
greeting = str1 + " " + str2
print(greeting) #"Hello, World!"

#repetition of strings
word = "Ha"
laughter = word * 3
print(laughter) #"HaHaHa"

#string with number
age = 25
#error: can't concatenate str and int
# message = "I am " + age + " years old." type error
# print(message)
#correct way using str() to convert int to str
#solution 1
message = "I am " + str(age) + " years old."
print(message) #"I am 25 years old."

#solution 2 using comma in print function
print("I am", age, "years old.") #"I am 25 years old."

#solution 3 using f-strings (formatted string literals)
message_fstring = f"I am {age} years {25} old."
print(message_fstring) #"I am 25 years old."

#email example
username = "pranav"
domain = "example.com"
email = username + "@" + domain
print(email) #"

#using f-strings
email_fstring = f"{username}@{domain}"
print(email_fstring) #"


name = "John"
mobile = 1234567890
