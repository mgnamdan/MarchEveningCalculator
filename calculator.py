# ~~~~~ IMPORTS AND HELPER FUNCTIONS ~~~~~
def add(numOne, numTwo):
    return float(numOne) + float(numTwo)


def subtract(numOne, numTwo):
    return float(numOne) - float(numTwo)


def multiply(numOne, numTwo):
    return float(numOne) * float(numTwo)


def divide(numOne, numTwo):
    try:
        return float(numOne) / float(numTwo)
    except ZeroDivisionError:
        return "You can't divide by zero!"

# ~~~~~ MAIN DEFINITION ~~~~~
def main():
    calcOn = True

    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide
                  }

    while calcOn:
        print("\nEnter a number:")
        firstNum = input(" --> ")

        print("\nEnter an operation: [+, -, *, /]")
        operation = input(" --> ").lower()

        print("\nEnter another number:")
        secondNum = input(" --> ")

        result = operations[operation](firstNum, secondNum)

        # if operation in ["+", "plus", "add"]:
        #     result = add(firstNum, secondNum)
        # elif operation in ["-", "minus", "subtract"]:
        #     result = subtract(firstNum, secondNum)
        # elif operation in ["*", "times", "multiply"]:
        #     result = multiply(firstNum, secondNum)
        # elif operation in ["/", "divided by", "divide"]:
        #     result = divide(firstNum, secondNum)
        # else:
        #     result = "Invalid operation - try again!"

        print(f"\nYour result is: {result}")

        print("\nWould you like to perform another calculation? [(Y)es or (N)o]")
        moreCalc = input(" --> ").lower()
        if moreCalc in ["n", "no"]:
            calcOn = False


# ~~~~~ MAIN CALL ~~~~~
main()
