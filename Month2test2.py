def my_nigerian_geopolitical_zone_analyzer():

    print("== THE NIGERIAN GEOPOLITICAL ZONE ANALYZER == \n")

    states_populations = {
        "Kano": 15.0,
        "Lagos": 16.5,
        "Anambra": 5.5,
        "Oyo": 8.0,
        "Borneo": 6.0,
        "Rivers": 7.5,
        "Kaduna": 9.5
    }

    states_zones = {
        "Kano" : "North West",
        "Kaduna" : "North West",
        "Lagos": "South West",
        "Oyo" : "South West",
        "Anambra" : "South East",
        "Borneo" : "North East",
        "Rivers" : "South South"
    }

    states = []
    populations = []
    zones = []

    for state, population in states_populations.items():
        if population > 8.0:
            print(f"the population of {state} is {population} million ")

    for state, zone in states_zones.items():
        population = states_populations[state]
        print(f"{state} is in the {zone} zone and has {population} million people."
            )

def main():
    my_nigerian_geopolitical_zone_analyzer()

if __name__ == "__main__":
    main()