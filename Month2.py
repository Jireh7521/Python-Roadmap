nigeria_states_and_capitals = {
    "Abia": "Umuahia",
    "Adamawa": "Yola",
    "Akwa Ibom": "Uyo",
    "Anambra": "Awka",
    "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa",
    "Benue": "Makurdi",
    "Borno": "Maiduguri",
    "Cross River": "Calabar",
    "Delta": "Asaba",
    "Ebonyi": "Abakaliki",
    "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti",
    "Enugu": "Enugu",
    "Federal Capital Territory": "Abuja",
    "Gombe": "Gombe",
    "Imo": "Owerri",
    "Jigawa": "Dutse",
    "Kaduna": "Kaduna",
    "Kano": "Kano",
    "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi",
    "Kogi": "Lokoja",
    "Kwara": "Ilorin",
    "Lagos": "Ikeja",
    "Nasarawa": "Lafia",
    "Niger": "Minna",
    "Ogun": "Abeokuta",
    "Ondo": "Akure",
    "Ogun": "Abeokuta",
    "Osun": "Oshogbo",
    "Oyo": "Ibadan",
    "Plateau": "Jos",
    "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto",
    "Taraba": "Jalingo",
    "Yobe": "Damaturu",
    "Zamfara": "Gusau"
}

states = []
capitals = []

for key, value in nigeria_states_and_capitals.items():
    states.append(key)
    capitals.append(value)

for state in states:
    print(state)
    
for capital in capitals:
        print(capital)


Jerry = "boy"

while Jerry == "boy":
    print("Jerry is a boy")

    Jerry = input("What Gender is Jerry? \n Boy \n Girl: \n").strip().lower()
    if Jerry == "boy":
        print("Jerry is a boy")
    else:
        Jerry != "boy"
        print("Sorry Jerry is not a girl.")


uncange = ("Jireh", "Joy", "James", "Janet")

print(uncange[0])
for i, x in enumerate(uncange):
    print(i, x)
