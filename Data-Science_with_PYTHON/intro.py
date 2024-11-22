#------------------------------------Intro---------------------------------------------------
print("Hello World!")

# Variables
customVar = "Aayush"
print(customVar)

# ----------------------------------DataTypes--------------------------------------------------
 #int,float,string and boolean

intNumber = 3
print(intNumber)
spell = type(intNumber)
print("The type of" , intNumber ," is ",spell)

decimate = 4.5
print(decimate)

string = "Aayush"
print(string)

bool = True
print(bool)

#complex
complex = 3+4j
print(type(complex))

#---------------------------------Operators----------------------------------------------------

#Arithmetic Operators -> + , - , * , /
num1 = 10
num2 = 30

print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)

#Relational Operators -> <,>,==,!=

print(num1<num2)
print(num1>num2)
print(num1==num2)
print(num1!=num2)

#Logical Operators -> &,|

log1 = True
log2 = False

print(log1&log2)
print(log1&log1)
print(log1|log1)
print(log1&log2)


#------------------------------Python Tokens----------------------------------------
# > Keywords
#       False, class, finally, Is, Return, None, continue, For, Lambda, Try, True, def, From, Nonlocal, While,    and, del, Global, Not, With, as,elif, if, or, Yield 
# > Identifiers
# > Literals
        #Constant in Python
# > Operators

#String in python
str1 = "Aayush"
str2 = 'Aayush'
str3 = '''A
          a
          y
          u
          s
          h'''

print(str3)

#String Properties
strExample = "Hello World"

# -1 gives the last letter
print(strExample[-1])
print(len(strExample))
print(strExample.upper())
print(strExample.lower())

#Replace
print(strExample.replace("World","Human"))

#Find
print(strExample.find("World"))

#Splitting a String
#Gives lists of substring
strSentence = "The spark of creativity is yours; we are merely the tools to bring it to life."
print(strSentence.split(';'))

#Lists
l1 = ['1','hi','you','human']
print(l1)
print(type(l1))
print(l1[3])
