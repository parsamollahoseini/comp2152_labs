class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"
        print("Constructing the Person object")

    # Regular getter and setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Magic getter and setter using property decorators
    # (Comment out the regular ones when using these)
    """
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    """

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

# Creating an instance of Person
if __name__ == "__main__":
    person = Person("Mark", 20, 6)

    # Printing public attribute
    print(person.public_prop)

    # Trying to access private attribute (will cause AttributeError)
    try:
        print(person.__name)
    except AttributeError as e:
        print(f"Error: {e}")

    # Using getter and setter methods
    print(f"Current name: {person.get_name()}")
    person.set_name("Anna")
    print(f"New name: {person.get_name()}")

    # Comment out the above getter/setter usage and uncomment the following
    # when using property decorators
    """
    # Using magic getter and setter
    print(f"Current name: {person.name}")
    person.name = "Anna"
    print(f"New name: {person.name}")
    """