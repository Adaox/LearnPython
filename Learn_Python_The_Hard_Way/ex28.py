q1 = "True and True"
q2 = "False and True"
q3 = "1 == 1 and 2 == 1"
q4 = '"test" == "test"'
q5 = "1 == 1 or 2 != 1"
q6 = "True and 1 == 1"
q7 = "False and 0 != 0"
q8 = "True or 1 == 1"
q9 = '"test" == "testing"'
q10 = "1 != 0 and 2 == 1"
q11 = '"test" != "testing"'
q12 = '"test" == 1'
q13 = "not (True and False)"
q14 = "not (1 == 1 and 0 != 1)"
q15 = "not (10 == 1 or 1000 == 1000)"
q16 = "not (1 != 10 or 3 == 4)"
q17 = 'not ("testing" == "testing" and "Zed" == "Cool Guy")'
q18 = '1 == 1 and (not ("testing" == 1 or 1 == 0))'
q19 = '"chunky" == "bacon" and (not (3 == 4 or 3 == 3))'
q20 = '3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))'


questions = [
    q1,
    q2,
    q3,
    q4,
    q5,
    q6,
    q7,
    q8,
    q9,
    q10,
    q11,
    q12,
    q13,
    q14,
    q15,
    q16,
    q17,
    q18,
    q19,
    q20,
]
count = 1

for question in questions:
    input(f"{count}. {question}: ")
    print(eval(question))
    count += 1
