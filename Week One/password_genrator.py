import random
import string
length = input("How long should your password be?\n") # User input for length of password
letters = input("How many letters should be in the password?\n") # User input for number of letters in password
numbers = input("How many numbers should be in the password?\n") # user input for number of digits in password

# Converting input to integers
c_len = int(length)
n_letters = int(letters)
n_numbers = int(numbers)
n_sym = c_len - (n_letters + n_numbers)

def string_generator(size):
    """ Generate lower and upper case strings of a specified length
    Args:
        size (int): Length of the string
    Returns:
        string: mixture of uppercase and lowercase letters that are randomly selected
    """
    chars = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choices(chars,k=size))


def num_generator(size):
    """ Generate digits of  specified length
        Args:
            size (int): Length of the digits
        Returns:
            string:  randomly selected number
        """
    chars = string.digits
    return ''.join(random.choices(chars,k=size))

def symbols(size):
    """ Generate symbols of a specified length
        Args:
            size (int): number of symbols
        Returns:
            string: randomly selected symbols
        """
    chars = string.punctuation
    return ''.join(random.choices(chars, k=size))

def password(letters,number,symbols):
    """ Generate a string that has a mixture or digits,uppercase,lowercase and/or symbols
            Args:
                letters (int): number of Alphabets in string
                number (int): number of digits in the string
                symbols (int): number of symbols in the string

            Returns:
                string: randomly generated string
    """
    chars = letters+number+symbols
    return ''.join(random.sample(chars,k=len(chars)))


if c_len < 6:# Check to see if password is less than 6
    print("Length of password can not be less than 6")
elif n_letters + n_numbers > c_len: # To make sure sum of string and numbers doesn't exceed provided length of password
    print("Opps!!! The Length Of Letters And Numbers Is Out Of Range")
else:
    # Call password function and print the generated password
    result = password(string_generator(n_letters),num_generator(n_numbers),symbols(n_sym))
    print(result)

