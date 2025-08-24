# Design Your own Class
# Create a class representing anything you like(a Smartphone, Book, or even a superhero!)
# Add attributes and methods to bring the class to life
# Use constructors to initialize the class attributes
# Add an inheritance layer to explore polymorphism or encapsulation


class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def make_call(self, number):
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}...")
        else:
            print(f"Cannot make a call. {self.brand} {self.model} is OFF.")

    def send_message(self, number, message):
        if self.is_on:
            print(f"Sending message to {number}: {message}")
        else:
            print(f"Cannot send message. {self.brand} {self.model} is OFF.")

# Derieved class
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, storage, color, camera_megapixels):
        super().__init__(brand, model, storage, color)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.is_on:
            print(f"Taking a photo with {self.camera_megapixels}MP camera on {self.brand} {self.model}.")
        else:
            print(f"Cannot take photo. {self.brand} {self.model} is OFF.")

# Example usage
phone = AdvancedSmartphone("TechBrand", "X1000", "128GB", "Black", 48)
phone.power_on()   

phone = Smartphone("TechBrand", "X1000", "128GB", "Black")
phone.power_on()



class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
