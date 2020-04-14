# Run script for quiz. Add questions to dictionary to expand quiz.
animals = ["bear", "python", "peacock", "kangaroo", "whale", "platypus"]
questions = {
    "1 The animal at 1 ": animals[1],
    "2. The third (3rd) animal. ": animals[2],
    "3. The ﬁrst (1st) animal. ": animals[0],
    "4. The animal at 3. ": animals[3],
    "5. The ﬁfth (5th) animal. ": animals[4],
    "6. The animal at 2. ": animals[2],
    "7. The sixth (6th) animal. ": animals[5],
    "8. The animal at 4. ": animals[4],
    "9. The second (2nd) animal. ": animals[1],
}

print(animals)
for question, answer in questions.items():
    input(question)
    print("Answer: ", answer)
