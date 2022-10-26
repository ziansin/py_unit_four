def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
def main():

    # Get the two pieces of input from the user.
    num = int(input("What is the first number? "))
    check = int(input("What is the second number? "))

    if is_divisible(num, check):
        print(num, "is divisible by", check)
    else:
        print(num, "is not divisible by", check)


if __name__ == '__main__':
    main()
