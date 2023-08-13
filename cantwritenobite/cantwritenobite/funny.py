class Funny:
    def __init__(self, joke):
        self.joke = joke

    def tell_joke(self):
        print(self.joke)

    def tell_lots_of_jokes(self, num_jokes):
        for _ in range(num_jokes):
            self.tell_joke()
