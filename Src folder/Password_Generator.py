import secrets
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    """Generate a cryptographically secure random password."""
    characters = string.ascii_letters
    
    if include_digits:
        characters += string.digits
        
    if include_symbols:
        characters += string.punctuation
    

    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def get_yes_no_input(prompt):
    """Helper function to get yes/no input."""
    while True:
        response = input(prompt).lower()
        if response in ('yes', 'no', 'y', 'n'):
            return response in ('yes', 'y')
        print("Please enter 'yes' or 'no'")

def main():
    print("\n Secure Password Generator \n")
    
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Password length too short. Using minimum 8 characters.")
            length = 8
    except ValueError:
        print("Invalid input. Using default length of 12 characters.")
        length = 12
    
    include_digits = get_yes_no_input("Include digits? (yes/no): ")
    include_symbols = get_yes_no_input("Include symbols? (yes/no): ")
    
    password = generate_password(length, include_digits, include_symbols)
    print("\nGenerated Password:", password)
    print(" Warning! Remember to store this password securely!\n")

if __name__ == "__main__":
    main()