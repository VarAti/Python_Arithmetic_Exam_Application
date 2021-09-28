# write your code here
import random


def get_task():
    global a, b, opr, base_n
    if level == 2:
        base_n = random.randint(11, 29)
        print(base_n)
    elif level == 1:
        opr_list = ['+', '-', '*']
        operands = [random.randrange(2, 10) for _ in range(2)]
        a = operands[0]
        b = operands[1]
        opr = random.choice(opr_list)
        print(f"{a} {opr} {b}")


def calc_task():
    global result
    result = 0
    if level == 2:
        result = base_n ** 2
    elif level == 1:
        if opr == '+':
            result = a + b
        elif opr == '-':
            result = a - b
        elif opr == '*':
            result = a * b
        elif opr == '/':
            try:
                result = a / b
            except ArithmeticError:
                print("Divide with zero!")


mark = 0
while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    try:
        level = int(input())
    except ValueError:
        print("Wrong format! Try again.")
    else:
        if level not in (1, 2):
            print("Incorrect format.")
        else:
            break
for _ in range(5):
    get_task()
    calc_task()
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect format.")
        else:
            if answer == result:
                print("Right!")
                mark += 1
                break
            else:
                print("Wrong!")
                break
print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
should_save = input().lower()
if should_save in ('y', 'Y', 'YES', 'Yes', 'yes'):
    print("What is your name?")
    name = input()
    with open("results.txt", mode='a') as file:
        level_text = "in level 1 (simple operations with numbers 2-9)." if level == 1 else \
            "in level 2 (integral squares of 11-29)."
        file.write(f"{name}: {mark}/5 {level_text}\n")
    print('The results are saved in "results.txt".')
