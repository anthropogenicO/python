# Lab Exercise 4

# Question 1: Sentinel and Score Validation
def score_validation():
    total = 0
    valid_score = 0
    
    while True:
        score = int(input("Enter a score (1-100, -1 to stop): "))

        if score == -1:
            break
        if 1 <= score <= 100:
            total += score
            valid_score +=1

        else:
            print("Invalid score. Try again.")

    print(f"Valid score: {valid_score}")
    print(f"Total: {total}")


# Question 2: Star Mountain
def star_mountain():
    for i in range(1, 6):
        for _ in range(i):
            print("*", end="")
        print()
    for i in range(4, 0, -1):
        for _ in range(i):
            print("*", end="")
        print()
    


# Question 3-1: Function Returning Sum
def add(a, b):
    sum = a+b
    return sum


# Question 3-2: Square Calculation Program
def print_square(box):
    square = box * box
    print (square)


def main():
    score_validation()
    star_mountain()


    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    sum = add(first, second)
    print_square(sum)


# main guard
if __name__ == "__main__":
    main()