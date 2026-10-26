def my_exam_score():
    print("== EXAM SCORE ==")

    name = input("Name: ")
    exam_score = int(input("Enter score: "))

    if exam_score >= 50 and exam_score <= 100:
        return f"Congratulations {name}, you passed!"
    elif exam_score < 0 or exam_score > 100:
        return "Invalid score"
    else:
        return "Fail"
    
def main():
    print(my_exam_score())

if __name__ == "__main__":
    main()