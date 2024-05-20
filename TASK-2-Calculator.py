def add(first_number, second_number):
    print(f" ANSWER = {first_number + second_number}")


def subtract(first_number, second_number):
    print(f" ANSWER = {first_number - second_number}")


def multiply(first_number, second_number):
    print(f" ANSWER = {first_number * second_number}")


def divide(first_number, second_number):
    if second_number != 0:
        print(f" ANSWER = {first_number / second_number}")
    else:
        print("Division by Zero is not possible")


first_number = float(input("Enter the First number: "))
second_number = float(input("Enter the Second number: "))
print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")

choice = int(input("Enter your choice of operation: "))

if choice == 1:
    add(first_number, second_number)
elif choice == 2:
    subtract(first_number, second_number)
elif choice == 3:
    multiply(first_number, second_number)
elif choice == 4:
    divide(first_number, second_number)
else:
    print("Invalid Choice")
