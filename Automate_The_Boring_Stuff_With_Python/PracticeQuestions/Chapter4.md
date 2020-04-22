## 1. What is []?

## 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

---

## For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

---

## 3. What does spam[int(int('3' * 2) // 11)] evaluate to?

## 4. What does spam[-1] evaluate to?

## 5. What does spam[:2] evaluate to?

---

## For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

---

## 6. What does bacon.index('cat') evaluate to?

## 7. What does bacon.append(99) make the list value in bacon look like?

## 8. What does bacon.remove('cat') make the list value in bacon look like?

## 9. What are the operators for list concatenation and list replication?

## 10. What is the difference between the append() and insert() list methods?

## 11. What are two ways to remove values from a list?

## 12. Name a few ways that list values are similar to string values.

## 13. What is the difference between lists and tuples?

## 14. How do you type the tuple value that has just the integer value 42 in it?

## 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

## 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

## 17. What is the difference between copy.copy() and copy.deepcopy()?

---

## Answers:

1.

- [] is an empty list

2.

- spam[2] = "hello"

3.

- "d"

4.

- "d"

5.

- ["a","b"]

6.

- 1

7.

- [3.14, 'cat', 11, 'cat', True, 99]

8.

- [3.14, 11, 'cat', True]

9.

- list concatenation uses +
- list replication uses \*

10.

- append adds the value to the end of the list
- insert adds the value at the index passed to it

11.

- del list[index]
- list.remove(value)

12.

- Both can be indexed
- Both can be iterated

13.

- lists are mutable denoted by []
- tuples are immutable denoted by ()

14.

- (42,)

15.

- list(tuple)
- tuple(list)

16.

- Reference id's

17.

- copy.copy() works on a normal list
- copy.deepcopy() works on nested lists
