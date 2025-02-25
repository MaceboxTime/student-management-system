"""first project """
try:
    a = int(input("Enter a Number :"))
    b = int(input("Enter another Number :"))
    result = a / b
    print(F"Result : {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")
except Exception as e:
    print(F":Unexpected error {e}")
finally:
    print("Execution completed!")

"""Second project"""
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileExistsError:
    print("Error: File not found!")
except Exception as e:
    print(F"Unexpected error: {e}")
finally:
    print("Closing file (if opened)")
    if 'file' in locals():
        file.close()
"""third project"""
class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0:
        raise NegativeNumberError("Error: Negative numbers are not allowed!")
    else:
        print(F"Valid Number {num}")
try:
    n = int(input("Enter a number: "))
    check_number(n)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Error: Invalid input! Enter a number.")
"""Try-Except Block"""
try:
    a = int(input("Enter a number"))
    result = 10 / a
    print(F"Result {result}")
except ZeroDivisionError:
    print("Error: Zero से भाग नहीं कर सकते!")
except ValueError:
    print("Error: कृपया एक सही संख्या डालें।")
"""Finally Block"""
try:
    f = open("data.txt","r")
    content = f.read()
    print(content)
except FileExistsError:
    print("Error: फ़ाइल नहीं मिली।")
finally:
    print("यह हमेशा चलेगा, चाहे error आए या नहीं।")
"""Raising Custom Errors"""
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Error: बैलेंस से ज़्यादा पैसा नहीं निकाल सकते!")
    balance -= amount
try:
    wt = int(input("Enter withdraw balance"))
    new_balance = withdraw(3000,wt)
    print(F"Remaining Balance:{new_balance}")
except ValueError as e:
    print(e)