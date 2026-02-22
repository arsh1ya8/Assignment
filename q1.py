# Program: Simple Bio Card


# Storing personal details in variables
name = "Syeda Arshiya"
age = "21"
course = "Python Programming"
college = "Navodaya Institute of Technology"
hobby = "Photography"
gmail = "arshinesyeda@gmail.com"


# Printing the formatted bio card
print("\n" + "╔" + "═"*60 + "╗")
print("║                 MY BIO CARD                 ║")
print("╠" + "═"*60 + "╣")

print(f"║  Name      : {name:<42}║")
print(f"║  Age       : {age:<42}║")
print(f"║  Course    : {course:<42}║")
print(f"║  College   : {college:<42}║")
print(f"║  Hobby     : {hobby:<42}║")
print(f"║  Gmail     : {gmail:<42}║")


print("╚" + "═"*60 + "╝")