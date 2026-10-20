def My_Ticket_Calculator():

    print("==  TICKET CALCULATOR ==")

    name = input("Enter name: ")

    age = int(input("Enter age: "))

    price = 0

    is_student = (input("Are you a Student: Ture or False \n").strip().lower() == "true")

    if age >= 65:
        price += 7
        if is_student == True:
            return f"Ticket for Seniors who are students Cost ${price - 2}"
        return f"Ticket for Seniors Cost ${price}"
    elif age >= 18 and age <= 64:
        price += 12
        if is_student == True:
            return f"Ticket for Adults who are students Cost ${price - 2}"
        return f"Ticket for Adults Cost ${price}"
    elif age >= 12 and age <= 17:
        price += 8
        if is_student == True:
            return f"Ticket for Teenagers who are students Cost ${price - 2}"
        return f"Ticket for Teenagers Cost ${price}"
    else:
        return f"Ticket for Children Cost ${price}, that's Free"
    
def main():
    print(My_Ticket_Calculator())

if __name__ == "__main__":
    main()