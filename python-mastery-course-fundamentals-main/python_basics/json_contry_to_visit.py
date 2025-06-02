import json
from pathlib import Path


def save_to_json(data, filename="countries.json"):
    """Save the list of countries to a JSON File"""
    with Path.open(filename, "w") as f:
        json.dump(data, f)


def read_from_json(filename="countries.json"):
    with Path.open(filename, "r") as f:
        return json.load(f)


def main():
    countries = []
    print("Enter country names. Type 'quit' to finish")

    while True:
        country = input("Country:")
        if country.lower() == "quit":
            break
        countries.append(country)

        # save the list of countries to a JSON File
        save_to_json(countries)

        # read the contents from the JSON file and display
        saved_countries = read_from_json()
        print("\nYou've added the following countries:")
        for country in saved_countries:
            print(country)


if __name__ == "__main__":
    main()
