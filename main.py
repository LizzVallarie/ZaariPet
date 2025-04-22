# Zaari Pet Project - Main Menu
# Zaari Pet Project - Main Menu
class ZaariPet:
    def eat(self):
        print("Nom nom! Your pet is eating.")

    def play(self):
        print("Your pet is playing happily!")

    def sleep(self):
        print("Zzz... Your pet is sleeping.")

    def train(self):
        print("Your pet learned a new trick!")

    def show_tricks(self):
        print("Your pet shows off its tricks!")

    def get_status(self):
        print("Your pet is healthy and happy!")

    def celebrate_birthday(self):
        print("Happy birthday to your pet!")

# Initialize the pet
my_pet = ZaariPet()

# Define actions
actions = {
    "1": ("Feed", lambda: my_pet.eat()),
    "2": ("Play", lambda: my_pet.play()),
    "3": ("Sleep", lambda: my_pet.sleep()),
    "4": ("Train", lambda: my_pet.train()),
    "5": ("Show Tricks", lambda: my_pet.show_tricks()),
    "6": ("Check Status", lambda: my_pet.get_status()),
    "7": ("Celebrate Birthday", lambda: my_pet.celebrate_birthday())
}

# Main loop
while True:
    print("\n" + "-" * 30)
    print("MAIN MENU".center(30))
    for key, (action, _) in actions.items():
        print(f"{key}. {action}")
    print("0. Exit")

    choice = input("Choose an action: ").strip()
    if choice == "0":
        print("Goodbye!")
        break
    elif choice in actions:
        actions[choice][1]()  # Execute the action
    else:
        print("Invalid choice. Try again.")
