print("Hello, World!")
print("Hello","banana","cherry",sep="\t")
print("Hello",end="!!!")
print("Line 1",end="");print("Line 2")
name = "Alice";print(f"Hi, {name}!")
print("Line 1\nLine 2")
print("Line 1\tLine 2")
Samosa = 3.25
print(f"Samosa: Rs\t{Samosa:.2f}")
text= "test";print(f"{text:<10}")
text= "test";print(f"{text:>10}")
text= "test";print(f"{text:^10}")







#name

name=input("Enter your name: ")
print("Welcome",name)
print("Welcome " + name + "!")

x=10
print(x)
print(type(x))

y=123.45
print(y)

x="AAU, ICAR, INDIA"
print(x)
print(type(x))







#printing numbers based on user input (while loop)

b=0
num=input("Enter a number: ")
num1=int(num)

while b<=num1:
    print(b)
    b+=1
 
 





   
#largest number printing (condition)

num1=input("Enter number 1: ")
no1=int(num1)

num2=input("Enter number 2: ")
no2=int(num2)

num3=input("Enter number 3: ")
no3=int(num3)

if no1 >= no2 and no1 >= no3:
    print(no1," is largest number")
    
elif no2 >= no1 and no2 >= no3:
    print(no2," is largest number")
    
elif no3 >= no1 and no3 >= no2:
    print(no3," is largest number")
    
else:
    print("Error")
    
    
    
    
    
    
    
    
# Simple interest

p=int(input("Enter p: "))

r=int(input("Enter r: "))

n=int(input("Enter n: "))

answer=p+r+n/100

print(answer)

# Compound interest

p=float(input("Enter p: "))

r=float(input("Enter r: "))

n=float(input("Enter n: "))

t=float(input("Enter t: "))

A = p * (1 + r/n) ** (n*t)

print(A,"is compount interest of your data")
    






#Fabonacci

i=int(input("Enter a number: "))

a=0
b=1


for i in range(i):
    print(a)
    c=a+b
    a=b
    b=c
    
 
    
 
    
 
    
 
# List 

mylist = [1,"MClaren","7000RPM"]

print("output of your list is ",mylist)
print(type(mylist))






# Tuple 

mytuple = (2,"Shellby","6000RPM")

print("output of you tuple is ",mytuple)
print(type(mytuple))







# Set 

myset = {3,"GT40","6500RPM"}

print("output of your set is ",myset)
print(type(myset))







# Dictionary

Student = {406 : "Legends",405 : "Pro"}

Student[406]
Student[405]
print(type(Student))







# Dictionary with multiple records

students = [ {"id": 1, "name": "ken miles", "age": 40},
             {"id": 1, "name": "max verstappen", "age": 32}
           ]

for s in students:
   # print(s)
    
    print("ID : ",s['id'])
    print("Name : ",s['name'])
    print("age : ",s['age'])
    print("------------------------")
    






    
# Matrix 

import numpy as np

n1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

print(n1)







# Square of range mentioned

n1 = [x**2 for x in range(1,10)]
print("Square of the above range : ",n1)







# numpy version check

import numpy as np

print(np.__version__)







# to check the dimwnsio of array

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)







# how to define dimension  of an array

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)







# Filtering 

# for odd values
data = [1,2,3,5,7,8,12,14,17]
filtered = []

for d in data:
    if( d % 2 != 0):
        filtered.append(d)
        
        
print(filtered)

#for even values
data = [1, 2, 3, 5, 7, 8, 12, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25]
even = []

for a in data:
    if a % 2 == 0:
        even.append(a)

print(even)







# Function Definition

def add (a,b):
    return a+b

add1 = int(input("Enter number :"))
add2 = int(input("Enter number :"))

x = add(add1,add2)

print(x)







# Broadcasting

import numpy as np

x = [1,2,3,4]

x1 = np.array(x)

print(x)

type(x1)

type(x)

print(x1+1)

print(x1+10)

print(x1) # here it says that by broadcasting the original value of var does not change







# Matrix 2x3 of zeros

b = np.zeros((2,3))

print(b)







# vectors of ones

c = np.ones((3,4))

print(c)
print("Shape : ",c.shape)
type(c)







# Transpose of Matrix

import numpy as np

m1 = np.array([[1, 2], [3, 4], [5, 6]]) 
m1t = m1.T  # Transpose
print("Matrix before transpose")
print(m1)
print("Matrix after Transpose")
print(m1t)
print("Shape : ",m1t.shape)







# Adaptive range (a range)

d = np.arange (0,21,4)

print(d)
type(d)

# Random 

e = np.random.rand(2,2)

print(e) # everytime the output will be diff as we fire the program







# practice

x='hello how are you'
y=1234

print(y)

print(x.upper())

print(x.lower())

print(x.title())

print(x.capitalize())

print(x.swapcase()) # it swapes the letters in upper and lower case

print(x.count('o'))

print(x.find('h'))

print(x.replace('you','U')) # replace char or letter

print('1234'.isalnum()) # it checks if it is alpha numeric or not, answers in true or false

print('hello'.isalnum())

print('1234 hello'.isalnum())

print('aaa'.isdigit())

print('1A23'.isalpha())

print('ABC'.isupper())

print('abc'.isupper())

print('Thisisram'.istitle())

print('This is ram'.istitle())

print('This Is Ram'.istitle())

print('  '.isspace())

print('  v'.isspace())

print('Vadodara'.startswith('Va'))

print('surat'.endswith('at'))

print('2025'.isnumeric())

s='python'
print(s[:]) # prints full string
print(s[::]) # prints full string
print(s[0:4:2]) # prints acc to range
print(s[-4:-1])
print(s[-6:])
print(s[0:5])
print(s[::2])
print(s[1::-2])
print(s[1::-1])

# number to character

n=input("Enter Number :")
n=int(n)
num = {
    0:"zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred",
    1000: "one thousand"
}

if n in num:
    print(num[n])

elif n>20 and n<=99:
 m=n%10*10
 a=n//10
 
 print(m,a)
 print(num[m],num[a])
 
elif n>99 and n<=999:
 m=n%100
 a=n-m
 c=m//10*10
 d=m%10
 print(c)
 print(d)
 print(a,m)
 print(num[a],num[c],num[d])
else:
 print("not in 1 to 1000")
 





   
# Tic Tak Toe

#import random

def initialize_board():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board

def print_board(board):
    for row in board:
        print(row)
    print()

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty.append((i, j))
    return empty

def check_rows(board, player):
    for i in range(3):
        row = board[i]
        if row.count(player) == 2 and row.count(' ') == 1:
            return i, row.index(' ')
    return None

def check_columns(board, player):
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(player) == 2 and col.count(' ') == 1:
            return col.index(' '), j
    return None

def check_diagonals(board, player):
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count(' ') == 1:
        idx = diag1.index(' ')
        return idx, idx
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count(player) == 2 and diag2.count(' ') == 1:
        idx = diag2.index(' ')
        return idx, 2 - idx
    return None

def ai_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        move = check_rows(board, 'O') or check_columns(board, 'O') or check_diagonals(board, 'O')
        if not move:
            move = check_rows(board, 'X') or check_columns(board, 'X') or check_diagonals(board, 'X')
        if not move:
            move = empty_cells[0]
        row, col = move
        board[row][col] = 'O'

def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    while True:
        print_board(board)
        move = input("Enter your move as row and column (0 0 to 2 2): ")
        i, j = move.strip().split()
        i = int(i)
        j = int(j)
        if board[i][j] != ' ':
            print("Cell already taken. Try again.")
            continue
        board[i][j] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move(board)
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()







# dict

dict = {'a':1,'b':2}
print(dict['a'])
print(dict)
del dict['b']
print(dict)

dict.keys() #functions of dictionary
dict.values()
dict.items()
dict.update({'z':4})
dict.update({'f':5})
print(dict)
dict.get('z',"Not in dict")


d = {'x':{'y':2}} #dict in dict 
print(d)
print(d['x'])
print(d.values())
print(d.items())
print(d.keys())
d.update({'g':7})
print(d)

# if and else condi.

a=10
b=2
if a>5 and b>5:
    print("correct")
else:
    print("incorrect")
    

a=10;b=20
print(a is b) # out : false, because a != b


a=[1,2,3,4,5]
b=3

print(b in a)


# if, elseif, else

a = 10
if a>9:
    print("a>9")
elif a<10:
    print("a<10")
else:
    print("fool")
    
# practice cdoe 

name_set = {"vatsal"}
pass_set = {"ait2025"}

enter1=input("Enter your username : ")
enter2=input("Enter your Password : ")

if enter1 in name_set and enter2 in pass_set:
    print("Successfully logged in")
    enter3=int(input("Enter your Age : "))
    if enter3 >= 15 and enter3 <= 40:
        print("Aaap javan ho")
    if enter3 > 40:
        print("Aap Aadhed ho")
    if enter3 < 15:
        print("Aap aabhi bacche ho")
        
else:
    print("Incorrect username or password")


# For loop

for i in range(5):
    if i==2:
        #continue
        pass
        #break
    print(i)
    #print("hello")
    
    
for i in range(2,5):
    print(i)

    
for i in range(2,15,3):
    print(i)
    

for i in range(2,10):   # imp 
    print(f"value of {i}")
    
# example

name=input("Enter your name : ")
pass1=input("Enter your password : ")
print(f"your name is {name} and password is {pass1}")

    
word='hello'
for i in word:
    print(i)
    
# enumerate    
colors = ["red","green","blue"]
for i, j in enumerate(colors):
    print(f"color at index {i}: {j}") # imp


for i in range(1,4):    # 1 2 3
    for j in range(1,4):# 1 2 3
        print(f"{i}x{j}=",i*j)
        

# star printing

rows = int(input("Enter number of rows : "))

for i in range(rows):
   
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")

    
    print()

        
    
# pandas, csv file

import pandas as pd
df=pd.read_csv('Book1.csv')
print(df)
print(df.head())
print(df.tail())
print(df.info())

    # other operations 
    
import pandas as pd
df=pd.read_csv("Book1.csv")
print(df)
#print(df.shape())
print(df.columns)
print(df.tail(2))
print(df.head(2))
print(df.info())
print(df.describe())

print("'''''''''''''''''''")
print(df.min(axis=0,numeric_only=True))

print("'''''''''''''''''''")
print(df.sum(axis=0,numeric_only=True))
print("'''''''''''''''''''")                
    
    
    
#axis=1==row and axis=0==column with pandas and matplotlib library

import pandas as pd
import matplotlib as plt
df=pd.read_csv("student.csv")
print(df)

mean=df.mean(axis=1,numeric_only=True)
print(mean)
print("--------------")
maxx=df.max(axis=0,numeric_only=True)
print(maxx)

mean=df.max(axis=1,numeric_only=True)
print(mean)
print("--------------")
df["summ"]=df[["math", "science", "gujarati", "hindi", "english"]].sum(axis=1)
print(df[["name","summ"]])
print("--------------")
df["std"]=df[["math", "science", "gujarati", "hindi", "english"]].std(axis=1)
print(df[["name","std"]])
print("--------------")
df["mean"]=df[["math", "science", "gujarati", "hindi", "english"]].mean(axis=1)
print(df[["name","mean"]])
print("--------------")
df["min"]=df[["math", "science", "gujarati", "hindi", "english"]].min(axis=1)
print(df[["name","min"]])
print("--------------")
df["max"]=df[["math", "science", "gujarati", "hindi", "english"]].max(axis=1)
print(df[["name","max"]])
print("--------------")
print("check persentage")
print("--------------")
df["summ"]=df[["math", "science", "gujarati", "hindi", "english"]].sum(axis=1)
#print(df[["name","summ"]])
df["per"]=(df["summ"]*100)/500
print(df[["name","per"]])
print("*************************")
print(df[["name","per","summ","mean","min","max","std"]])
print("//////////////////////////   matplotlib")
plt.plot(df["name"], df["per"], marker="o", color="green")
plt.title("Percentage Trend")
plt.xlabel("Student")
plt.ylabel("Percentage (%)")
plt.grid(True)
plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
