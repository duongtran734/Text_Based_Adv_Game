class RPGInfo():
    author = "Duong"

    def __init__(self, game_title):
        self.title = game_title
        self.char = None

    # Instance method, required self to be passed through it
    def welcome(self):
        print(f"Welcome {self.char.name} to {self.title}")

    # Require nothing to be pass to it
    @staticmethod
    def info():
        print("\nMade using the OOP RPG Creator (c) me")
        print("Your objective in this game is to find a Giant Spider and kill it")
        print("However there are different enemies that you'll have to defeat on your way")
        print("Good Luck in your game Hero\n\n")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"Created by {cls.author}")

