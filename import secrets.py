import secrets
import string

def generate_password(length=12):
    
    #Combines to provide a wide variety of characters for a robust password
    alphabet = string.ascii_letters + string.digits + string.punctuation

    #Iterates and uses secrets to choose random character for each position
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

print("Generated secure password (secrets):", generate_password(16))