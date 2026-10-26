# Python-Roadmap

# Python Basics — My Learning Journey

## About This Project

This repository contains my Python practice exercises as I learn programming. It covers the fundamentals of Python, including variables, data types, operators, user input, conditional statements, loops, lists, and functions.

The project also includes small programs that apply these concepts to real-world examples, such as calculating a person's future age and determining ticket prices.

My goal is to understand how Python works, improve my problem-solving skills, and build a strong foundation for full-stack development and cybersecurity.

## Topics Covered

### 1. Printing Output

I learned how to use `print()` to display text, values, and calculation results in the console.

```python
print("Hello, World!")
```

### 2. Variables

Variables store data that can be used throughout a program.

```python
x, y, z = "Samuel", "Ochygole", "Jireh"
my_age = 20
Car_Name = "BMW"
```

I practised assigning values to multiple variables and displaying their contents.

### 3. Data Types

Python provides different data types for storing different kinds of information.

- `int` — integers, such as `10`
- `float` — decimal numbers, such as `10.5`
- `str` — text, such as `"Hello"`
- `bool` — Boolean values, such as `True` and `False`

I used `type()` to identify data types and practised converting values with `int()`, `float()`, and `str()`.

### 4. Functions

Functions are reusable blocks of code that perform specific tasks.

```python
def myfunc():
    print("Python is awesome")

myfunc()
```

I practised defining functions, calling them, passing arguments, and returning results with `return`.

### 5. Arithmetic Operators

I practised using Python's arithmetic operators:

| Operator | Purpose | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `20 - 5` |
| `*` | Multiplication | `5 * 5` |
| `/` | Division | `7 / 2` |
| `//` | Floor division | `7 // 2` |
| `%` | Modulus (remainder) | `7 % 2` |
| `**` | Exponentiation | `10 ** 2` |

### 6. Comparison Operators

Comparison operators compare values and return either `True` or `False`.

The operators I practised include:

- `>` — greater than
- `<` — less than
- `==` — equal to
- `!=` — not equal to
- `>=` — greater than or equal to
- `<=` — less than or equal to

### 7. User Input and F-Strings

I learned how to collect information from users with `input()` and display dynamic messages using f-strings.

```python
nice_name = input("Enter your name: ")
print(f"Your name is {nice_name}")
```

I also practised collecting two numbers and adding them together after converting the input strings into integers.

### 8. Conditional Statements

Conditional statements allow a program to make decisions based on specific conditions.

I practised using:

- `if`
- `elif`
- `else`

For example, the job eligibility function checks a person's age and returns a message based on the result.

### 9. Lists and Loops

Lists store multiple items in a single variable.

```python
names = ["Jireh", "Janet", "John", "Joy"]
```

I practised list operations such as:

- `pop()` — removes and returns an item at a specified position.
- `remove()` — removes the first matching item.
- `insert()` — adds an item at a specified position.

I also used `for` loops to iterate over list items and `range()` to generate sequences of numbers.

## Projects and Exercises

### 1. Personal Introduction

**Purpose:** Collect a user's full name and favourite programming language, then display the information.

**Concepts practised:** Functions, `input()`, variables, and f-strings.

### 2. Age Calculator

**Purpose:** Ask for a name and age, validate the age input, and calculate how old the person will be in five years.

**Concepts practised:** Input validation, strings, integers, arithmetic, conditional statements, and return values.

The program uses `isdigit()` to check whether the age contains non-negative whole-number digits before converting it to an integer.

### 3. Ticket Calculator

**Purpose:** Calculate a ticket price based on a person's age and student status.

| Category | Base price |
|---|---:|
| Children under 12 | Free |
| Teenagers aged 12–17 | $8 |
| Adults aged 18–64 | $12 |
| Seniors aged 65 and above | $7 |

Students receive a $2 discount on the applicable base price.

**Concepts practised:** Functions, user input, Boolean values, nested conditions, comparison operators, and arithmetic.

### 4. Job Eligibility Checker

**Purpose:** Return a message based on a person's age.

- Ages 20–64: Eligible according to the exercise's age rule.
- Ages 65 and above: Not eligible according to the exercise's age rule.
- Under 20: Must wait until reaching the required age.

**Concepts practised:** Function parameters, `if`/`elif` statements, comparison operators, and return values.

*Note: This is a programming exercise, not a real-world employment rule.*

### 5. Basic Calculator Exercises

**Purpose:** Practise mathematical operations and understand the results produced by different operators.

**Concepts practised:** Arithmetic operators, numeric data types, and `print()`.

### 6. List Manipulation Exercises

**Purpose:** Practise storing, accessing, inserting, and removing items from a list.

**Concepts practised:** Lists, indexes, list methods, and `for` loops.

## How to Run the Programs

### Requirements

- Python 3 installed.
- A code editor such as Visual Studio Code, or a terminal.

### Steps

1. Save the code in a Python file, for example, `main.py`.
2. Open a terminal in the directory containing the file.
3. Run the program:

```bash
python3 main.py
```

4. Follow the prompts displayed in the terminal.

**Important:** The code contains multiple exercises, each with its own `main()` function and `if __name__ == "__main__":` block. If everything is saved in one file, the separate entry points will execute in sequence. For cleaner execution, save each exercise in its own Python file.

## Current Learning Goals

I am working towards:

- Writing clean, readable Python code.
- Understanding how variables, functions, and conditions work together.
- Improving input validation and error handling.
- Learning to solve programming problems independently.
- Building small projects before moving on to more advanced applications.
- Developing the programming foundation needed for full-stack development and cybersecurity.


## Month 2 — Beginning Python Practice

At the beginning of Month 2, I am building on the Python fundamentals I learned in Month 1. My focus is to understand how to combine variables, functions, user input, conditional statements, and error handling to solve simple problems independently.

### Exercise 1: Exam Score Checker

**Objective:** Build a program that collects a student's name and exam score, validates the input, and determines whether the student passed or failed.

**Concepts practised:**
- Functions and return values
- User input with `input()`
- String validation using `.strip()`
- Integer conversion using `int()`
- Error handling with `try` and `except ValueError`
- Conditional logic using `if`, `elif`, and `else`
- F-strings for formatted output
- Using `main()` as the program's entry point

**Scoring rules:**

| Score | Outcome |
|---|---|
| 50–100 | Pass |
| 0–49 | Fail |
| Below 0 or above 100 | Invalid score |
| Non-numeric input | Display an error message |
| Empty name | Ask the user to enter a name |

**Learning goal:** Understand how to validate user input and make decisions based on conditions instead of writing code that only works with valid input.

**Future improvements:** Add automated tests, improve validation messages, and practise handling different types of invalid input.

