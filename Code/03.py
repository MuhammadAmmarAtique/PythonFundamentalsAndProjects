# 1) Conditional Statements

# age = 18

# if age < 18 and age > 0 :
#     print("you are not an adult")
# elif age >= 18 :
#     print("you are an adult")   
# else:
#     print("you are not even born yet")     

# 2) Mini project (Calculator)

num1= input("Enter First number: ")
num2= input("Enter Second number: ")

operator = input("Enter operation you want to do? (+, -, *, /) ")

if operator == "+":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1) - int(num2)) 
elif operator == "*":
    print(int(num1) * int(num2))
elif operator == "/":
    print(int(num1) / int(num2))  
else:
    print("Invalid Entry")              