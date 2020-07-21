class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name: ", self.restaurant_name + " cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now working.")


my_rest_1 = Restaurant("Aimer", "AA")
my_rest_2 = Restaurant("Neige", "BB")
my_rest_3 = Restaurant("Inory", "CC")
print(my_rest_1.restaurant_name)
print(my_rest_1.cuisine_type)
print(my_rest_2.restaurant_name)
print(my_rest_2.cuisine_type)
print(my_rest_3.restaurant_name)
print(my_rest_3.cuisine_type)
my_rest_1.describe_restaurant()
my_rest_1.open_restaurant()
my_rest_2.describe_restaurant()
my_rest_2.open_restaurant()
my_rest_3.describe_restaurant()
my_rest_3.open_restaurant()
