def list_methods():
    """Modify a list and print its basic statistics."""
    numbers = [12, 5, 18, 7, 5]

    # TODO: Modify numbers as described in the PDF.
    numbers.append(10)
    numbers.insert(2, 9)
    numbers.remove(5)
    numbers.sort()
    numbers.reverse()
    # TODO: Calculate count, minimum, maximum, and total.
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)

    print("List:", numbers)
    print("Number of elements:", count)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Sum:", total)


def list_copy():
    """Compare an original list with its modified copy."""
    scores = [78, 92, 85, 60]

    # TODO: Create and modify copied list here.
    copied_scores = scores.copy()
    copied_scores[0]= 100
    copied_scores.append(88)

    print("Original list:", scores)
    print("Copied list:", copied_scores)


def temperature_stats():
    """Print the total, average, and count of temperatures at least 70."""
    temperatures = [68, 72, 75, 64, 81, 70]

    # TODO: Calculate total, count_at_least_70, and average.
    total = 0
    count_at_least_70 = 0

    for temperature in temperatures:
        total += temperature
        if temperature >= 70:
            count_at_least_70 += 1

    average = total /len(temperatures)

    print("Total:", total)
    print(f"Average: {average:.2f}")
    print("Temperatures greater than or equal to 70:", count_at_least_70)


def student_totals():
    """Print each student's total and identify the student with the highest total."""
    scores = [
        [85, 90, 78],
        [88, 76, 92],
        [90, 85, 87]
    ]

    totals = []

    # TODO: Populate totals using nested loops.

    for student in scores:
        total = 0
        for score in student:
            total += score
        totals.append(total)


    for index in range(len(totals)):
        print(f"Student {index + 1} total: {totals[index]}")

    # TODO: Find highest_total and highest_student.

    highest_total = totals[0]
    highest_student = 1

    for index in range(len(totals)):
        if totals[index] > highest_total:
            highest_total = totals[index]
            highest_student = index + 1

    print(f"Student with the highest total: Student {highest_student}")


def main():
    list_methods()
    list_copy()
    temperature_stats()
    student_totals()

if __name__ == "__main__":
    main()
