class Enemy:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Prepare to meet your doom, {self.name}!')
