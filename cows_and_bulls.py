import random
import re
import copy

original_digits = []

for i in range(4):
    original_digits.append(str(random.randint(0,9)))

def count(_list):
    counts = {}
    for i in range(len(_list)):
        digit = _list[i]
        if digit not in counts:
            counts[digit] = 1
            for n in range(len(_list)):
                if _list[n] == digit and n != i:
                    counts[digit] += 1
    return counts

if __name__ == "__main__":

    print("\n####### WELCOME TO COWS AND BULLS ########")
    print("#######     Enter 'q' to quit     ########")

    cows = 0
    attempt = 1
    quitter = False

    while cows < 4:

        answer_digits = copy.copy(original_digits)

        if attempt == 0:
            user_input = input("\nEnter a 4 digit number: ").strip()
        else:
            user_input = input(f"\nAttempt #{attempt}: ").strip()
        if user_input == "q":
            quitter = True
            break
        elif len(user_input) != 4 or re.match(r'[\D]',user_input):
            print("Invalid answer.  Please enter a 4-digit number.")
            continue


        answer_counts = count(original_digits)
        user_counts = count(user_input)

        cows = 0
        bulls = 0

        for i in range(len(answer_digits)):
            if user_input[i] == answer_digits[i]:
                cows += 1
                answer_digits[i] = ""
        
        for i in range(len(answer_digits)):
            for n in range(len(answer_digits)):
                if answer_digits[n] == user_input[i]:
                    bulls += 1
                    answer_digits[n] = ""
                    break

        attempt += 1
        
        print(f"\n########  COWS: {cows}  ########")
        print(f"######## BULLS: {bulls}  ########")
    if not quitter:
        print("\n\n#################################\n#################################\n################## ##    ## #####\n###                      ########\n### ##     -WINNER-      ########\n#######                ##########\n#######  # ####### #  ###########\n#################################\n#################################\n\n")


