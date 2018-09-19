
def factorial(num):
    try:
        assert num >= 0 and (isinstance(num,int) or num.is_integer())
    except:
        raise ValueError("Invalid argument. Only natural integers possible.")
    
    result = 1
    for n in range(1,num+1):
        result *= n
    
    return result

if __name__ == "__main__":

    try:
        user_number = int(input("Enter a number (0 or greater): "))
        assert user_number >= 0
    except:
        raise ValueError("Invalid input.  Use only a natural integer.")

    print(f"{user_number}! = {factorial(user_number)}")