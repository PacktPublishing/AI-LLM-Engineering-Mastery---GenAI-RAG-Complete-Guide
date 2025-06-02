dream_destinations = {}

print("Let's plan your dream travel itinerary ✈️")
print("Enter 'done' when you're finished. \n")

while True:
    country = input("Which country would you like to visit?")
    if country.lower() == "done":
        break

    note = input(
        f"Anything specific you'd like to do or see in {country}? (press enter to skip)"
    )

    # add the country and optional note to the dic
    dream_destinations[country] = note if note else "No specific plans"
    print("Got it! Let's keep going or type 'done' to finish!")

print("\nYour Dream Travel Itinerary:")
for country, note in dream_destinations.items():
    print(f"- {country}: {note}")

print("\nLooks like an exciting adventure awaits! Safe Travels!")
