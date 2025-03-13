# Task 1: Create a Basic Class
class Vehicle:
    """
    Create a Vehicle class with the following attributes:
    - make (string)
    - model (string)
    - year (integer)
    Initialize these attributes via the constructor.
    """
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year= year
        
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
        
        

# Task 2: Add Methods to a Class
class BankAccount:
    """
    Create a BankAccount class with:
    - balance (float, initialized to 0)
    - Methods: deposit(amount), withdraw(amount), and get_balance().
    Withdrawing more than the balance should raise a ValueError.
    """
    
    def __init__(self, balance):
        
        self.balance= balance
        
    def deposit(self,amount):
        # self.amount= int(input('Enter amount: '))
        if amount <= 0:
            raise ValueError ("amount need to be a positive integer")
        self.balance += amount
        
    def withdraw(self,amount):
        
        if amount > self.balance:
            raise ValueError ("Insuficient funds")
        self.balance -= amount
        
    def get_balance(self):
        return self.balance
        
    
    pass

# Task 3: Inheritance
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    """
    Inherit from Animal and override speak() to return "Woof!".
    """
    def speak(self):
        
        return "woof"
dog = Dog()

# Task 5: Static Methods
class MathOperations:
    """
    Add static methods:
    - add(a, b): returns a + b
    - factorial(n): returns the factorial of n (use a loop).
    """

    @staticmethod    
    def add(a,b):
        results= a + b
        return results
    
    @staticmethod
    def factorial(n):
        if n < 0:
            return "Invalid input"
        
        fact = 1
        for i in range(1, n +1):
            fact *= i
        return fact
        


# Task 6: Properties and Setters
class Temperature:
    """
    Create a Temperature class with a private attribute _celsius.
    Add a property `celsius` and a property `fahrenheit` that converts between Celsius and Fahrenheit.
    (Formula: F = C * 9/5 + 32)
    """
    pass

# Task 7: Operator Overloading
class Vector:
    """
    Create a Vector class with x and y attributes.
    Overload the `+` operator to add two Vector instances.
    """
    
    def __init__(self, x, y):
        self.x= x
        self.y= y
    
    def __add__(self, other):
        
        return Vector(self.x + other.x, self.y + other.y)

# Task 8: Class with Exception Handling
class Book:
    """
    Create a Book class with:
    - title (string)
    - author (string)
    The constructor should raise a ValueError if title or author is empty.
    """
    
    def __init__(self,title, author):
        self.title= title
        self.author= author
        
        if title == "" or author == "":
            raise ValueError ("Title and author should be not empty")
        
        try:
            book1= Book("", "A.E. James")
            raise ValueError ("Author or Title should not be empty")
        except ValueError as e:
            print(f"Error {e}")