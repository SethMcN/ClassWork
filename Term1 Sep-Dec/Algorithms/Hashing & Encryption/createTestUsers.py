from hashing import hash_string
import random
import string
from Vigenère import VigenereCypher
import pandas as pd

def generate_random_email(names
                          
                          ):
    domains = ["example.com", "test.com", "sample.org"]
    name = random.choice(names)
    domain = random.choice(domains)
    return f"{name}@{domain}"

def createTestUsers():
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Jack"]
    passwords = ["password", "123456", "password123", "123456789", "password123456", "password123456789", "123456password", "123456789password", "passwordpassword", "123456789123456789"]
    

    emails = [generate_random_email(names) for _ in range(10)]
    usernames = [name.lower() for name in names]
    passwords = [hash_string(password) for password in passwords]

    df = pd.read_csv('users.csv')

    for i in range(10):
        encryptedEmail = VigenereCypher("securekey", emails[i])
        print(f"Email: {emails[i]}, Username: {usernames[i]}, Password: {passwords[i]}, Encrypted Email: {encryptedEmail}")
        df.loc[len(df)] = [len(df), usernames[i], passwords[i], encryptedEmail]
    
    df.to_csv('users.csv', index=False)



    print(emails)

createTestUsers()