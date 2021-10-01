class Animal():
    noise = 'grunt'
    size = 'large'
    color = 'brown'
    hair = 'covers body'

    @property
    def get_color(self):
        return self.color

    def make_noise(self):
        return self.noise


# dog = Animal()
# print(dog.make_noise())


class Dog(Animal):  # Dog class inheriting animal class
    name = 'jon'
    color = 'brown'


# dog = Dog()
# print(dog.name)-
# print(dog.get_color)
