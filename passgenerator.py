import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_weak_password():
    weak_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'welcome', 'admin']
    return random.choice(weak_passwords)

def main():
    while True:
        strength = input("Enter the strength of the password you want to generate (weak/strong): ").lower()
        if strength == 'weak':
            password = generate_weak_password()
        elif strength == 'strong':
            length = int(input("Enter the length of the strong password you want to generate: "))
            if length < 4:
                print("Please enter a length of at least 4 characters.")
                continue
            password = generate_strong_password(length)
        else:
            print("Invalid input. Please enter 'weak' or 'strong'.")
            continue
        print("Generated password:", password)
        prompt = input("Do you want to generate another password? (yes/no): ").lower()
        if prompt != 'yes':
            break

if __name__ == "__main__":
    main()

