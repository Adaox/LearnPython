## 1. What are the two values of the Boolean data type? How do you write them?

## 2. What are the three Boolean operators?

## Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

## 4. What do the following expressions evaluate to?

- (5 > 4) and (3 == 5)
- not (5 > 4)
- (5 > 4) or (3 == 5)
- not ((5 > 4) or (3 == 5))
- (True and True) and (True == False)
- (not False) or (not True)

## 5. What are the six comparison operators?

## 6. What is the difference between the equal to operator and the assignment operator?

## 7. Explain what a condition is and where you would use one.

## 8. Identify the three blocks in this code:

    spam = 0
    if spam == 10:
        print('eggs')
        if spam > 5:
            print('bacon')
        else:
            print('ham')
        print('spam')
    print('spam')

## 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

## 10. What keys can you press if your program is stuck in an infinite loop?

## 11. What is the difference between break and continue?

## 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

## 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

## 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

## Extra credit: Look up the round() and abs() functions on the internet, and find out what they do. Experiment with them in the interactive shell.

---

## Answers:

1.

- True
- False

2.

- and, or, not

3.

|       and       | evaluates to |
| :-------------: | :----------: |
|  True and True  |     True     |
| False and True  |    False     |
| True and False  |    False     |
| False and False |    False     |

|       or       | evaluates to |
| :------------: | :----------: |
|  True or True  |     True     |
| False or True  |     True     |
| True or False  |     True     |
| False or False |    False     |

|    not    | evaluates to |
| :-------: | :----------: |
| not False |     True     |
| not True  |    False     |

4.

- False
- False
- True
- False
- False
- True

5.

- ==
- !=
- \>
- <
- \>=
- <=

6.

- == (equal to) checks for equality (evaluates to Boolean)
- = (assignment) sets expression or value to variable

7.

- conditions are used in flow control to test if a block should run

8.

- everything following a : who's next line is indented

9.

    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!)

10.

- ctrl + c

11.

- break exits the loop
- continue goes back to the top of the loop

12.

- There is no difference

13.

    for i in range(1,11):
        print(i)

    i = 0
    while i < 10:
        print(i)
        i += 1

14.

- spam.bacon()

Extra Credit:

- https://docs.python.org/3/library/functions.html#abs
- https://docs.python.org/3/library/functions.html#round
