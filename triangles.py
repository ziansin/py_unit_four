
def is_triangle(side1, side2, side3):
    if side1 + side2 <= side3:
        return False
    elif side2 + side3 <= side1:
        return False
    elif side1 + side3 <= side2:
        return False
    else:
        return True

def main():
    first = int(input("Enter the first length: "))
    second = int(input("Enter the second length: "))
    third = int(input("Enter the third length: "))
    if is_triangle(first, second, third):
        print("The lengths would make a triangle.")
    else:
        print("The lengths would not make a triangle.")

if __name__ == '__main__':
    main()







