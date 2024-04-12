def calculator(a, b, oper):
    result = None
    if oper == "multiply":
        result = a * b
    elif oper == "divide":
        result = int(a / b)
    elif oper == "add":
        result = a + b
    elif oper == "subtract":
        result = a - b
    return result


oper = input()
a = int(input())
b = int(input())
print(calculator(a, b, oper))
