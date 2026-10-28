def my_inventory_scanner():

    valid_codes = ("A101", "B202", "C303", "D404")

    running = True

    print("--- Warehouse Scanner Terminal ---")
    print("Type 'quit' to exit the scanner.\n")

    while running:
        user_input = input("Scan item code: ")
    
        if user_input == "quit":
            return "Thank you!, Goodbye!"
        elif user_input in valid_codes: 
            print("Item accepted.")
        else:
            print("Invalid item!")


def main():
    print(my_inventory_scanner())

if __name__ == "__main__":
    main()