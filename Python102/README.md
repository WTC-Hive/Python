# Python Loops and Functions Project

Welcome to the Python Loops and Functions Project! In this project, you will practice working with **for/while loops, if/else statements, and functions** to solve challenging problems.

## Instructions

### Step 1: Set Up Your Environment

1. **Navigate to the Project Directory**:  
   - Move into the project folder:  
     ```bash
     cd Python102
     ```

2. **Set Up a Virtual Environment**:  
   - Create a virtual environment:  
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:  
     - On Windows:  
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:  
       ```bash
       source venv/bin/activate
       ```
   - Your terminal should now show the virtual environment name (e.g., `(venv)`).

3. **Install Dependencies**:  
   - Install the required packages:  
     ```bash
     pip install -r requirements.txt
     ```

---

### Step 2: Complete the Tasks

1. **Complete the Tasks**:  
   - Open `tasks.py` and implement the functions as described in the docstrings.  
   - Test your implementation using the provided unit tests.

2. **Run the Tests**:  
   - Run the tests and make sure they all pass:  
     ```bash
     pytest test_tasks.py
     ```
   - Passing test cases will appear like this:
     ![Alt text](testcases.png)

3. **Deactivate the Virtual Environment**:  
   - When you're done working, you can deactivate the virtual environment:  
     ```bash
     deactivate
     ```

4. **Commit and Push Your Changes**:  
   - Add your changes:  
     ```bash
     git add tasks.py
     ```
   - Commit your changes:  
     ```bash
     git commit -m "Completed tasks"
     ```
   - Push your changes to your branch:  
     ```bash
     git push origin main
     ```

5. **Submit a Pull Request**:  
   - Go to your forked repository on GitHub and click "New Pull Request".  
   - Select your branch (`YOUR_NAME`)from https://github.com/WTC-Hive/Python and submit the pull request to the main repository.
   
---

## Tasks Overview

### Task 1: Sum of Squares
- Calculate the sum of squares of the first `n` natural numbers.

### Task 2: Fibonacci Sequence
- Generate the first `n` numbers in the Fibonacci sequence.

### Task 3: Prime Number Check
- Check if a number is prime.

### Task 4: Largest Number in List
- Find the largest number in a list of numbers.

### Task 5: Reverse a Number
- Reverse the digits of a number.

### Task 6: Leap Year Check
- Check if a year is a leap year.

### Task 7: Count Vowels
- Count the number of vowels in a string.

### Task 8: Factorial
- Calculate the factorial of a number using a while loop.

### Task 9: Grade Calculator
- Calculate the grade based on a score.

### Task 10: Password Validator
- Validate a password based on specific rules.

---

## Running Tests

To run the tests, use the following command:  
```bash
pytest test_tasks.py