def my_age_calculator():
    print("== MY AGE CALCULATOR ==")

    name = input("Name: ")
    age = input("Age: ")

    if not age.isdigit():
        return "Age must be a vaild non-negative number."

    age = int(age)
    future_age = age + 5

    return f"Hello {name}! You will be {future_age} years old in five years."

def main():
    print(my_age_calculator())

if __name__ == "__main__":
    main()