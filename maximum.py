import random

random_one = random.randint(-10,10)
random_two = random.randint(-10,10)
print(random_one)
print(random_two)
def max(first, second):
    if first > second:
        print(first)
        return first
    if first < second:
        print(second)
        return second
    if first == second:
        print("The numbers are equal")
        return("The numbers are equal")

def main():
    max(random_one, random_two)

main()