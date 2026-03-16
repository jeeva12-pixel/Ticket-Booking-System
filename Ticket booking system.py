print("Welcome to the Bus Ticket Machine")
print("Available Destinations:")
print("1. Town Hall - ₹4")
print("2. Airport - ₹20")
print("3. Railway Station - ₹15")

choice = input("Enter destination number (1-3): ")

if choice == "1":
    place = "Town Hall"
    price = 4

elif choice == "2":
    place = "Airport"
    price = 20

elif choice == "3":
    place = "Railway Station"
    price = 15

else:
    print("Invalid choice")
    exit()

tickets = int(input(f"How many tickets to {place}? "))

total = price * tickets

print("\n----- Ticket Receipt -----")
print(f"Destination: {place}")
print(f"Price per ticket: ₹{price}")
print(f"Number of tickets: {tickets}")
print(f"Total Amount: ₹{total}")
print("Thank you for using the Bus Ticket Machine!")