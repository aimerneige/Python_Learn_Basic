class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog("jack", 4)
my_dog.sit()
my_dog.roll_over()
print(my_dog.name)
print(my_dog.age)
my_dog.name = 'farewell'
print(my_dog.name.title())
my_dog.sit()
