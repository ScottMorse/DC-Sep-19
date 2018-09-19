def is_prime(num):

    if (not isinstance(num,int) and not num.is_integer()):
        raise ValueError("Invalid argument.  Use integers only.")

    if num <= 1:
        return False

    #simplification of the AKS primality test, after assigning 1 for x
    if 2**num % num == 2 % num:
        return True
    return False

if __name__ == "__main__":

    try:
        user_num = int(input("Enter a number: "))
    except:
        raise ValueError("Invalid input.  Use integers only.")

    result = ' ' if is_prime(user_num) else ' NOT '

    print(f"{user_num} is{result}prime.")
