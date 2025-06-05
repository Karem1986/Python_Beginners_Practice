class Greeting:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def greet(self):
        return f"Hello, {self.name} {self.surname}!"

first_greeting = Greeting("Sasya", "Kossak")
first_greeting.name = "Dear" # override the name
print(first_greeting.greet())


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_point(self):
        print('x=', self.x, ' y=', self.y)

p2 = Points(1, 2)
p2.x = 2  # override the x value
p2.print_point()
