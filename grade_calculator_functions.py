def get_student_score() -> float:
    """Prompts the user to enter a valid numerical score and returns it."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """Determines the letter grade based on the given score."""
    grades = {
        (90, 100): 'A',
        (80, 89): 'B',
        (70, 79): 'C',
        (60, 69): 'D'
    }
    for range_, grade in grades.items():
        if range_[0] <= score <= range_[1]:
            return grade
    return 'F'

def main():
    """Main function to execute the grade calculator."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
