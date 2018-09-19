import re

def is_palindrome(string):

    if not isinstance(string,str):
        raise ValueError("Invalid argument. Use string.")

    for i in range(len(string)):
        if string[i] != string[len(string) - (i + 1)]:
            return False
    return True

if __name__ == "__main__":

    user_string = input("Enter a word or phrase: ").strip()
    user_string_mod = user_string.lower().replace(' ','')
    #in case of punctuation of a phrase
    if re.match(r'[\W]',user_string_mod[-1]):
        user_string_mod = user_string_mod[:-1]
        user_string = user_string[:-1]

    result = ' ' if is_palindrome(user_string_mod) else ' NOT '

    print(f"'{user_string.capitalize()}' is{result}a palindrome.")