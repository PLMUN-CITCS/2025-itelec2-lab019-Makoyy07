def get_student_score() -> float:
    """
    Prompts the user to enter a valid score and returns it.
    Ensures the input is a number between 0 and 100.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Takes the score as input and returns the corresponding grade.
    Grading scale:
        90 - 100: A
        80 - 89 : B
        70 - 79 : C
        60 - 69 : D
        Below 60: F
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main program
def main():
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()