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
    pass


# ~~~~~ MAIN CALL ~~~~~
main()
