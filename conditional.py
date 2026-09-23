number = int(input("enter a number:"))
if number % 5 ==0:
    print("divisible by 5")

 # temperature check
temperature = float(input("enter temperature:"))
if temperature > 40:
     print("high temperature")
marks = int(input("enter marks:"))
if marks >=40:
     print("pass")
else:
     print("fail")

number = int(input("enter a number"))
if number >=0:
     print("positive")
else:
     print("negative")
number = int(input("enter a number:"))
if number > 100:
     print("number is greater than 100")
else:
     print("number is not greater than 100")
marks = int(input("enter marks:"))
if marks >=90:
     print("Grade A")
elif marks >=75:
     print("Grade B")
elif marks >=60:
     print("Grade C")
elif marks >40:
     print("Grade D")
else:
     print("Fail")
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a > b:
     print("Largest:",a)
elif b > a:
     print("Largest:",b)
else:
     print("both are equal")
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a >= b and a >= c:
     print("largest:", a)
elif b >= a and b >= c:
     print("largest:", b)
else:
     print("largest:",c)
day = int(input("enter a number:"))
if day ==1:
     print("sunday")
elif day ==2:
     print("monday")
elif day ==3:
     print("tuesday")
elif day ==4:
     print("wednesday")
elif day ==5:
     print("thursday")
elif day ==6:
     print("friday")
elif day ==7:
     print("saturday")
else:
     print("invalid day")

a = float (input("enter first number:"))
b = float(input("enter second number:"))
operator = input("enter operator (+, -,*,/):")
if operator =="+":
     print("result:", a + b)
elif operator == "-":
     print("results:", a - b)
elif operator == "*":
     print("result:", a * b)
elif operator =="/":
     if b !=0:
          print("result:", a / b)
else:
     print("cannot divide by zero")

username = input("enter username:")
password = input("enter password:")
if username == "admin":
     if password == "1234":
          print("login successful")
     else:
          print("wrong password")
else:
     print("wrong username")

#balance  input
balance = float(input("enter balance:"))
amount = float(input("enter withdrawal amount:"))
if amount > 0:
     if amount <=balance:
          balance = balance - amount
          print("withdrawl successful")
          print("remaining balance:", balance)
     else:
          print("insufficient balance")
else:
     print("invalid amount")

marks = int(input("enter marks:"))
attendence = float(input("enter attendence percentage:"))
if marks >=40:
     if attendance >=75:
          print("eligible")
     else:
          print("not eligibile due to attendance")
else:
     print("fail")

age = int(input("enter your age:"))
test = input(" did  you pass thr driving test ? (yes/no):")
if age >=18:
     if test == "yes":
          print("license can be issued")
     else:
          print("pass the driving test first")
else:
     print("not eligible due to age")

