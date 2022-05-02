class Burger:
    def __init__(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):
        self.bun = bun
        self.cheese = cheese
        self.patty = patty
        self.sauce = sauce
        self.lettuce = lettuce
        self.tomato = tomato
        self.num_pickles = num_pickles

    def add_pickles(self, N):
        self.num_pickles += N

    def describe_burger(self):
        print("This burger has a", self.bun, "bun with a", self.patty, "patty.", end=" ")
        print("It's drizzled with a delicious", self.sauce, "sauce.", end=" ")
        if self.lettuce:
            print("There is a bed of lettuce.", end=" ")
        if self.tomato:
            print("There are fresh tomatoes.", end=" ")
        if self.num_pickles > 0:
            print("Also, there are exactly", self.num_pickles, "pickles.", end=" ")



self=Burger('koljlkjhjhkjlhkjuh', 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'oljk', 'uj', 'khj', 'lou', 5)
print(Burger().describe_burger())