
def gets_a_zero(total_classes, class_missed):
    if total_classes * 0.25 <= class_missed:
        return True

def main():
    total = int(input("How many total classes? "))
    missed = int(input("How many classes missed? "))
    if gets_a_zero(total, missed):
        print("You get a zero!!!!!")
    else:
        print("You pass!!")


main()