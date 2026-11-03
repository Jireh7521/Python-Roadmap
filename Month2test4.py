# def my_guest_list():
#     friday_party = {"Alex", "Ben", "Chloe", "Dan"}
#     saturday_party = {"Ben", "Chloe", "Emma", "Fred"}
#     sunday_party = {"Dan", "Emma", "George"}

#     odd_guests = friday_party ^ saturday_party ^ sunday_party

#     friday_and_saturday = friday_party & saturday_party

#     print("Odd guests:", odd_guests)
#     print("Friday & Saturday guests:", friday_and_saturday)

# def main():

#     my_guest_list()

# if __name__ == "__main__":
#     main()

def get_guest_metrics(*parties):
    """
    Analyzes any number of guest lists using set operations.
    Returns sorted lists of odd-party guests and Friday/Saturday intersections.
    """
    if not parties:
        return [], []

    # Task 1: Dynamically chain the ^ operator across all passed sets
    odd_guests_set = parties[0].copy()
    for party in parties[1:]:
        odd_guests_set ^= party
    # Your code here (Loop or reduce to apply ^ to all remaining parties)

    # Task 2: Intersect the first two party sets (Friday and Saturday)
    # Hint: Ensure at least two parties exist before intersecting parties[0] and parties[1]
    friday_and_saturday_set = parties[0] & parties[1] if len(parties) >= 2 else set()

    # Return sorted lists so the output is always alphabetical
    return sorted(list(odd_guests_set)), sorted(list(friday_and_saturday_set))


def main():
    friday_party = {"Alex", "Ben", "Chloe", "Dan"}
    saturday_party = {"Ben", "Chloe", "Emma", "Fred"}
    sunday_party = {"Dan", "Emma", "George"}

    odd_guests, friday_and_saturday = get_guest_metrics(friday_party, saturday_party, sunday_party)

    print("Odd guests:", odd_guests)
    print("Friday & Saturday guests:", friday_and_saturday)

if __name__ == "__main__":
    main()