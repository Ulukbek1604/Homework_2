
class Animal:

    def __init__(self, weight, age, color):
        self.weight = weight
        self.age = age
        self.color = color

    def voiceT(self):
        print(f'{self.voise}')

class Dog(Animal):
    def __init__(self, voice):
        self.voice =voice

rex = Dog(12, 2, 'blue', 'F' )
    





