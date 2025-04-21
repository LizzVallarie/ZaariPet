import random

class Pet:
    def __init__(self, name="ZAARI"):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.age = 0
        self.color = self.generate_color()
        print(f"✨ {self.name} the {self.color} pet was born! ✨")

    def generate_color(self):
        colors = ["Golden", "Silver", "Emerald", "Sapphire", "Ruby", "Onyx"]
        return random.choice(colors)

    def eat(self, food="pet food"):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍖 {self.name} devoured {food}! Hunger↓ {self.hunger}/10, Happiness↑ {self.happiness}/10")
        self.age += 0.1

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"😴 {self.name} had a power nap! Energy↑ {self.energy}/10")
        self.age += 0.2

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"⚡ {self.name} played wildly! Energy↓ {self.energy}/10, Happiness↑ {self.happiness}/10, Hunger↑ {self.hunger}/10")
        else:
            print(f"💤 {self.name} is exhausted and needs sleep!")
        self.age += 0.1

    def get_status(self):
        print(f"\n🌟 {self.name}'s STATUS 🌟")
        print(f"| Color: {self.color.ljust(10)} | Age: {round(self.age,1)} years |")
        print(f"| Hunger:  {'▣' * self.hunger}{'▢' * (10-self.hunger)} |")
        print(f"| Energy:  {'▣' * self.energy}{'▢' * (10-self.energy)} |")
        print(f"| Happiness:{'♥' * self.happiness}{'♡' * (10-self.happiness)} |")

    def train(self, trick):
        if self.energy >= 1:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            self.energy -= 1
            print(f"🎓 {self.name} mastered '{trick}'! (+1 Happiness, -1 Energy)")
        else:
            print(f"😴 Training failed! {self.name} needs rest.")
        self.age += 0.05

    def show_tricks(self):
        if self.tricks:
            print(f"🎩 {self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"🙈 {self.name} knows no tricks yet!")

    def birthday(self):
        self.age += 1
        self.happiness = min(10, self.happiness + 2)
        print(f"""
        🎂🎉✨
   Happy Birthday {self.name}!
  Now {int(self.age)} years old!
        """)