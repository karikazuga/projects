action = ["+", "-", "*", "/"]
arg1 = input("Введите первое число >>")
arg2 = input("Введите второе число >>")
action = input("Введите действия >>")
try:
    if "." in arg1:
        arg1 = float(arg1)
    else:
        arg1 = int(arg1)
except ValueError:
    print("Error arg1")
    raise IndexError("IndexError")
try:
    if "." in arg2:
        arg2 = float(arg2)
    else:
        arg2 = int(arg2)
except ValueError:
    print("Error arg2")
    exit()
if 

if "." in arg1:
    arg1 = float(arg1)
else:
    arg1 = int(arg1)
if "." in arg2:
    arg2 = float(arg2)
else:
    arg1 = int(arg1)


arg1 = int(arg1)
arg2 = int (arg2)

if action not in action:
    print("Error")
    exit()
if action == "+":
    print(arg1 + arg2)
elif action == "-":
    print(arg1 - arg2)
elif action == "*":
    print(arg1 * arg2)
elif action == "/":
    print(arg1 / arg2)
