import random
import string
from passlib.hash import sha256_crypt

# The stored hash (simulating a previously hashed password)
stored_password_hash = sha256_crypt.hash('your_password')  # Replace "your_password" with an actual hash

# Function to generate a random password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to attempt to brute-force the password
def brute_force_password(stored_hash, max_attempts=100000, password_length=8):
    for attempt in range(max_attempts):
        random_password = generate_random_password(password_length)
        print(f"Attempt {attempt+1}: Trying password '{random_password}'")

        if sha256_crypt.verify(random_password, stored_hash):
            print(f"Password found: {random_password}")
            return random_password

    print("Password not found within attempt limit.")
    return None

# Run brute-force attack
found_password = brute_force_password(stored_password_hash)

if found_password:
    print(f"Success: Password is '{found_password}'")
else:
    print("Failed to find the password.")
