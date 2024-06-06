class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def taste(self):
        pass

class Apple(Fruit):
    def taste(self):
        return "sweet"
    
class Lemon(Fruit):
    def taste(self):
        return "sour"
    
apple = Apple("apple", "red")
lemon = Lemon("lemon", "yellow")
# Correct!!! name and color are attributes and taste is a
# method so it has parenthesis!!
apple_name = apple.name
apple_color = apple.color
apple_taste = apple.taste()

print(f"{apple_name} is {apple_color} and tastes {apple_taste}.")
print(Fruit.__subclasses__())