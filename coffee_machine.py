# Coffee Machine

class CoffeeMachine:

    def __init__(self):

        self.inventory = dict({'cash': 550,  # starting inventory
                    'water': 400,
                    'milk': 540,
                    'beans': 120,
                    'cups': 9})

        self.recipe = dict({'water': [0, 250, 350, 200],  # coffee recipes, [n/a, espresso, capp, latte]
                'milk': [0, 0, 75, 100],
                'beans': [0, 16, 20, 12],
                'price': [0, 4, 7, 6]})

    def actions(self, action):
        if action == 'buy':
            return self.buy()
        elif action == 'fill':
            return self.fill()
        elif action == 'take':
            return self.take()
        elif action == 'remaining':
            return self.show_inventory()
        elif action == 'exit':
            return action

    def buy(self):
        print()
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu')
        drink = input()
        if drink == 'back':
            self.action = ''
            return
        else:
            self.check_inventory(drink)  # adjust inventory by recipe amount

    def take(self):
        global inventory
        print()
        print('I gave you $',self.inventory['cash'])
        self.inventory['cash'] = 0
        return

    def fill(self):
        global inventory
        print()
        add_water = int(input('Write how many ml of water you want to add:\n'))
        self.inventory['water'] += add_water
        add_milk = int(input('Write how many ml of milk you want to add:\n'))
        self.inventory['milk'] += add_milk
        add_beans = int(input('Write how many grams of coffee beans you want to add:\n'))
        self.inventory['beans'] += add_beans
        add_cups = int(input('Write how many disposable coffee cups you want to add:\n'))
        self.inventory['cups'] += add_cups
        return

    def show_inventory(self):
        global inventory
        print()
        print('The coffee machine has:')
        print(self.inventory['water'], ' of water')
        print(self.inventory['milk'], ' of milk')
        print(self.inventory['beans'], 'of coffee beans')
        print(self.inventory['cups'], ' of disposable cups')
        print(self.inventory['cash'], ' of money')
        print()

    def check_inventory(self, drink):
        global inventory, recipe

        if self.inventory['water'] < self.recipe['water'][int(drink)]:
            print('Sorry, not enough water')
            return
        elif self.inventory['milk'] < self.recipe['milk'][int(drink)]:
            print('Sorry, not enough milk')
            return
        elif self.inventory['beans'] < self.recipe['beans'][int(drink)]:
            print('Sorry, not enough beans')
            return
        elif self.inventory['cups'] < 1:
            print('Sorry, not enough cups')
            return
        else:
            print()
            print('I have enough resources, making you a coffee!')
            self.inventory['cash'] += self.recipe['price'][int(drink)]
            self.inventory['water'] -= self.recipe['water'][int(drink)]
            self.inventory['milk'] -= self.recipe['milk'][int(drink)]
            self.inventory['beans'] -= self.recipe['beans'][int(drink)]
            self.inventory['cups'] -= 1
            return

def main():
    global action
    cm = CoffeeMachine()
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        if action == 'exit':
            break
        else:
            cm.actions(action)

main()
