def my_guest_list():
    print("== THE VIP GUEST LIST MANAGER ==")

    guest_list = ["Unwanted_Guest"]

    for guest in range(3):
        name = input("Enter Guest Name: ")

        guest_list.append(name)
    guest_list.insert(0, 'Sherlock')
    guest_list.remove("Unwanted_Guest" )
    removed_guest = guest_list.pop(-1)
    print(f"Sorry, {removed_guest}, the venue is full.")
    print(guest_list)

def main():
    my_guest_list()

if __name__ == "__main__":
    main()