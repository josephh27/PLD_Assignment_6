#Import a k
print("Wrong inputs will result into deductions.")
import random
quiz = True
count = 0 
correct = 0
deduction = 0
while quiz:
    try:
        number1 = random.randint(0,99)
        number2 = random.randint(0,99)
        userAnswer = int(input(f"What is the sum of {number1} and {number2}? "))
        answer = number1 + number2
        if answer == userAnswer:
            correct = correct + 1
            print("Well played!")
        else:
            print(f"The answer was {answer}.")
        count = count + 1
        totalScore = correct - deduction
        if count == 10:
            print(f"You have {deduction} deduction(s).")
            print(f"You got {totalScore} /10!")
            break
    except:
        print("Please input only numbers or you will have a deduction.")
        deduction = deduction + 1




