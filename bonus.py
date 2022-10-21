def bonus(salary, years):
    if years > 5:
        sal = salary + (salary * 0.05)
        return("Your total salary is: " + str(sal))
    else:
        sal = salary
        return("Your total salary is: " + str(sal))
def main():
    salary = float(input("What is your current salary?: "))
    years = float(input("How long have you worked here?: "))
    print(bonus(salary, years))

if __name__ == '__main__':
    main()