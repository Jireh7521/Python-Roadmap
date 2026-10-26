def my_exam_score():
    print("== EXAM SCORE ==")
    
    name = input("Name: ")
    if not name.strip():
        return "Please enter a name"

    try:
        exam_score = int(input("Enter score: "))
    except ValueError: 
        return "Please enter a valid whole number."

    if exam_score >= 50 and exam_score <= 100:
        return f"Congratulations {name}, you passed!"
    elif exam_score < 0 or exam_score > 100:
        return f"Invalid score {name}"
    else:
        return f"Sorry {name}, you failed!"
    
def main():
    print(my_exam_score())

if __name__ == "__main__":
    main()