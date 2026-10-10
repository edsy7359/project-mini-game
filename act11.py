try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError

    print("Square =", num ** 2)

except ValueError:
    print("Please enter zero or a positive number.")

finally:
    print("Thank you for using the program.")