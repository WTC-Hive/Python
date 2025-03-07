import string
# Task 1: Sum of Squares
def sum_of_squares(n):
    """
    Calculate the sum of squares of the first `n` natural numbers.
    Example: If n = 3, return 1² + 2² + 3² = 14.
    """
    total = 0
    for i in range(1, n + 1):
        total += i **2
    return total
 

# Task 2: Fibonacci Sequence
def fibonacci(n):
    """
    Generate the first `n` numbers in the Fibonacci sequence.
    Return the sequence as a list.
    Example: If n = 5, return [0, 1, 1, 2, 3].
    """
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_seq= [0,1]
    
    for i in range(2, n):
        next_seq= fib_seq[i-1] + fib_seq [i-2]
        fib_seq.append(next_seq)
    return fib_seq
        
        

# Task 3: Prime Number Check
def is_prime(num):
    """
    Check if a number is prime.
    Return True if the number is prime, otherwise False.
    Example: is_prime(7) → True, is_prime(10) → False.
    """
    if num <= 1:
        False
    
    for i in range (2, int(num ** 0.05)+1):
        if num % i == 0:
            return False
    return True
   

# Task 4: Largest Number in List
def find_largest(numbers):
    """
    Find the largest number in a list of numbers.
    Return the largest number.
    Example: find_largest([3, 7, 2, 9]) → 9.
    """
    
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Task 5: Reverse a Number
def reverse_number(num):
    """
    Reverse the digits of a number.
    Return the reversed number.
    Example: reverse_number(123) → 321.
    """
    
    reversed_num = int((str(num)[::-1]))
    return reversed_num
  

    pass

# Task 6: Leap Year Check
def is_leap_year(year):
    """
    Check if a year is a leap year.
    Return True if it is a leap year, otherwise False.
    A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.
    Example: is_leap_year(2000) → True, is_leap_year(1900) → False.
    """
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
    
    pass

# Task 7: Count Vowels
def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Return the count.
    Example: count_vowels("hello") → 2.
    """
    vowels= ["a","e","i","o","u"]
    counter = 0
    for char in text.lower():
        if char in vowels:
            counter += 1
    return counter
    
    pass

# Task 8: Factorial
def factorial(n):
    """
    Calculate the factorial of a number using a while loop.
    Return the factorial.
    Example: factorial(5) → 120.
    """
    
    if n < 1:
        return "invalid"
    
    fact = 1
    while n > 0:
        fact *= n
    n -= 1
    
    return fact



# Task 9: Grade Calculator
def calculate_grade(score):
    """
    Calculate the grade based on a score:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    Return the grade as a string.
    Example: calculate_grade(85) → "B".
    """
    
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif score < 60:
        return "F"
    
        
    
    

# Task 10: Password Validator
def validate_password(password):
    """
    Validate a password based on the following rules:
    - At least 8 characters long.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character (!@#$%^&*).
    Return True if the password is valid, otherwise False.
    Example: validate_password("Pass123!") → True.
    """
    
    if len(password) < 8:
        return "Invalid, password must be atleast 8 characters long"
    is_Upper= False
    is_lower= False
    isdigit = False
    is_special = False
    
    for char in password:
        if char.isupper():
            is_Upper = True
        elif char.islower():
            is_lower = True
        elif char.isdigit():
            isdigit = True
        elif char in string.punctuation():
            is_special = True
            
    if is_Upper  and is_lower and isdigit and is_special:
        return True
    return False
    
    pass