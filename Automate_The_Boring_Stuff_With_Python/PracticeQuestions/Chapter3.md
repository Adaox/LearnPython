## 1. Why are functions advantageous to have in your programs?

## 2. When does the code in a function execute: when the function is defined or when the function is called?

## 3. What statement creates a function?

## 4. What is the difference between a function and a function call?

## 5. How many global scopes are there in a Python program? How many local scopes?

## 6. What happens to variables in a local scope when the function call returns?

## 7. What is a return value? Can a return value be part of an expression?

## 8. If a function does not have a return statement, what is the return value of a call to that function?

## 9. How can you force a variable in a function to refer to the global variable?

## 10. What is the data type of None?

## 11. What does the import areallyourpetsnamederic statement do?

## 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

## 13. How can you prevent a program from crashing when it gets an error?

## 14. What goes in the try clause? What goes in the except clause?

---

## Answers:

1.

- Functions organize your code and help prevent unnecessary code duplication

2.

- Functions execute when they are called

3.

- def funcName():

4.

- A function is a set of instructions (mini-program) within your code.
- A function call actually runs those instructions.

5.

- There is only one global scope
- There are x number of local scopes, where x is the number of functions called

6.

- Variables in the local scope are destroyed when a function is returned

7.

- Return values are what functions bring back to the caller upon finishing. If no return value is specified, this defaults to "None"
- Return values can be part of an expression.

8.

- A function without a return statement, defaults to None as it's value

9.

- You can declare a variable within a function call as global

10.

- NoneType is the data type for None

11.

- this will import the areallyourpetsnamederic module to your python file

12.

- spam.bacon()

13.

- Use a Try/Except clause

14.

- Code you'd like to protect from errors goes in a try clause.
- How you'd like the program to respond to a given error (or all errors if none are defined) go in the except clause
