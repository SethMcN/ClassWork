import pandas as pd
from hashing import hash_string
from Vigenère import VigenereCypher, VigenereDecypher
import random 


def validEmail():
    valid = False
    while not valid:

        email = input("Enter email: ")

        exists = False
        for i in range(len(df)):
            if VigenereCypher(df['key'][i], email) == df.iloc[i]['email']:
                print('Email already exists')
                exists = True
                break
        
        if '@' not in email:
            print("Invalid email")

        elif not exists:
            
            return email

def register():

    email = validEmail()

    valid = False
    while not valid: 

        username = input('Enter username: ').replace(" ","")
        if username in df['username'].values:
            print('Username already exists')
        else:
            valid = True

    same = False
    while not same:
        password = input('Enter password: ')
        confirm = input('Confirm password: ')
        if password != confirm:
            print('Passwords do not match')
        else:
            same = True    

    key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    hashed_password = hash_string(password)
    encryptedEmail = VigenereCypher(key, email)

    df.loc[len(df)] = [len(df), username, hashed_password, encryptedEmail,key]

    df.to_csv('users.csv', index=False)

    print('User registered successfully')

def login():
    logedIn = False
    while not logedIn:
            
        username = input('Enter username: ')

        if username in df['username'].values:

            password = input('Enter password: ')
            hashed_password = hash_string(password)

            if hashed_password == df[df['username'] == username]['password'].values:
                print('Login successful')
                return username

            else:
                print('Incorrect password')
        else:
            print('Username not found')


def main():
    options = input('''
Options:
    1. Login
    2. Register
    3. Dev options
    
    : ''')

    print("-------------------------------------------------")

    if options == "1":
        username = login()
        if username != None:
            print(f'Welcome {username}')
            exit()

    elif options == "2":
        register()

    elif options == "3":
        password = input('Enter password Developer password: ')
        if hash_string(password) == '0xf3b66e5d':
            options = input('''
Options:
    1. Show users data
    2. Exit
    : ''')
            
            if options == '1':
                for row in df.iterrows():
                    print("-------------------------------------------------")
                    print(f"""
ID: {list(row[1])[0]}
Username: {list(row[1])[1]}
Password: {list(row[1])[2]}
Email: {VigenereDecypher(list(row[1])[4], list(row[1])[3])}
Key: {list(row[1])[4]}""")  

            
            elif options == '2':
                exit()
        
        else:
            print('Invalid password')
            exit()
        
    else:
        print('Invalid option')
        

# example users are populated in a csv file
# can login with username: 'testuser' and password: 'pa55word'


# Load users from csv file
try:
    df = pd.read_csv('users.csv',delimiter=",")
    

except FileNotFoundError:
    print('File not found')
    print('exiting...')
    exit()


if __name__ == "__main__":

    while True:
        main()