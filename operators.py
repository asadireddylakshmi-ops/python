#arthimetic operators
a=10
b=3
print("addition:", a+b)
print("subtraction:",a-b)
print("multiplication:", a*b)
print("division:",a/b)
print("floor division:", a//b)
print("remainder:",a%b)
print("power:",a**b)


#simple calculator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("addition:", a+b)
print("subtraction:",a-b)
print("multiplication:", a*b)
print("division:",a/b)

#students marks calculator
name=input("enter student name:")
m1= int(input("enter python marks:"))
m2=int(input("enter java marks:"))
m3=int(input("enter SQL marks:"))
total=m1+m2+m3
average=total/3
print("\n-----student report-----")
print("name:",name)
print("total:",total)

#shopping bill calculator
price=float(input("enter product 1 price:"))
price=float(input("enter product 2 price:"))
price=float(input("enter product 3 price:"))
dicount=total1*0.10
final_amount=total-discount
print("discount:",discount)
print("final amount:",final_amount)

#assignment operators
x=10
x+=5
print(X)
x-=2
print(x)
x*=3
print(x)

#bank balance
balance=10000
deposite=5000
balance +=deposite
print("After deposite:",balance)
withdraw =2000
balance -=withdraw
print("After withdrawl:",balance)

#comparison operators
a=10
b=20
print(a==b)
print(a !=b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("Enter your age:"))
print("Eligible:",age >=18)

#pass or fail checker
marks=int(input("Enter marks:"))
print("assed:", marks >=40)

#login validation
correct_username ="admin"
correct_password="1234"

username = input("Enter username:")
password = input("Enter password:")

print(username == correct_username)
print(password == correct_password)

#identity operators 
a = None 
print(a is none)
print(a is not None)


 #bitwise operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)

#electric city bill calculator 
units = int(input("Enter elecricity units:"))
rate = 6
bill = units * rate
print("elecricity bill:", bill)

# travel expenses calculator
travel = float(input("Travel expense:"))
food = float(input("Food expense:"))
hotel = float(input("Hotel expense:"))
total = travel + food + hotel
print("Total Expense:", total)
 