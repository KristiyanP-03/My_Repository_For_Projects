from random import randint
from time import sleep
print("System: Choose R for rock, P for paper or S for scissors: ", end="")
your_choice = input()
the_object = ""
if your_choice == "R" or your_choice == "P" or your_choice == "S":
    if your_choice == "R":
        the_object = "rock"
    elif your_choice == "P":
        the_object = "paper"
    elif your_choice == "S":
        the_object = "scissors"
    print("System: You've choiced " + the_object + "!")
else:
    raise SystemExit("System: Invalid input ... Use only [R/P/S]")
sleep(1)
PCs_choice_into_code = randint(1, 3)
if PCs_choice_into_code == 1:
    the_object = "rock"
elif PCs_choice_into_code == 2:
    the_object = "paper"
elif PCs_choice_into_code == 3:
    the_object = "scissors"
print("System: PC choiced " + the_object + "!")
if PCs_choice_into_code == 1 and your_choice == "R" or \
    PCs_choice_into_code == 2 and your_choice == "P" or \
    PCs_choice_into_code == 3 and your_choice == "S":
    sleep(2)
    print("System: Draw")
    sleep(2)
    print("PC: Pff ... Use something else next time! :O")
elif PCs_choice_into_code == 3 and your_choice == "R" or \
    PCs_choice_into_code == 1 and your_choice == "P" or \
    PCs_choice_into_code == 2 and your_choice == "S":
    sleep(2)
    print("System: You won!")
    sleep(3)
    print("PC: We've played 1/3 rounds? [Y/N]")
    your_answer = input()
    if your_answer == "Y":
        sleep(1)
        print("PC: Maybe next time. I'm too busy writing other codes.")
    if your_answer == "N":
        print("PC: Oho! Now you are winner and can't nobody tell you nothing? >:/")
    else:
        raise SystemExit("System: Invalid input ... Use only [Y/N] for this question")
elif PCs_choice_into_code == 2 and your_choice == "R" or \
    PCs_choice_into_code == 3 and your_choice == "P" or \
    PCs_choice_into_code == 1 and your_choice == "S":
    sleep(2)
    print("System: PC won!")
    sleep(2)
    print("PC: Hah! Weak. :P")
