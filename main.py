from pet import Pet
import time

def print_zaari_art():
    print(r"""
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
    """)

def main():
    print_zaari_art()
    print("🌟 WELCOME TO ZAARI'S WORLD 🌟")
    my_pet = Pet("ZAARI")

    actions = {
        "1": ("Feed", lambda: my_pet.eat(input("Food for ZAARI? "))),
        "2": ("Play", my_pet.play),
        "3": ("Sleep", my_pet.sleep),
        "4": ("Train", lambda: my_pet.train(input("New trick? "))),
        "5": ("Show Tricks", my_pet.show_tricks),
        "6": ("Check Status", my_pet.get_status),
        "7": ("Celebrate Birthday", my_pet.birthday)
    }

    while True:
        print("\n" + "="*30)
        print("MAIN MENU".center(30))
        for key, (action, _) in actions.items():
            print(f"{key}. {action}")
        print("0. Exit")
        
        choice = input(">> Your choice: ").strip()
        
        if choice == "0":
            print(f"Goodbye! {my_pet.name} will miss you! 💖")
            break
        elif choice in actions:
            actions[choice][1]()
            time.sleep(1)  # Pause for dramatic effect
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()