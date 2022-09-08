class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# fish inherits from animal
class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe()
        print("underwater...")



nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"Nemo have { nemo.eyes } eyes.")