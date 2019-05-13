#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import string
import random

def create_user(f_name, l_name, username, password):
    '''
    Function to create new user
    '''
    new_user = User(f_name, l_name, username, password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function to check is a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def create_credential(username, account, acc_username, acc_password):
    '''
    Function to create new credentials
    '''
    new_credential = Credentials(username, account, acc_username, acc_password)
    return new_credential

def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credential()

def delete_credential(credentials):
    '''
    Function to delete cred
    '''
    credentials.delete_credential()

def find_credential(username, account):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credentials.find_by_account(username, account)

def check_existing_credential(username):
    '''
    Function to check is a credential exists with that username and return a Boolean
    '''
    return Credentials.credential_exist(username)

def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def generate_password(length):
    pwd = []
    count = 0
    while (count < length/3):
        pwd.append(random.choice(string.ascii_lowercase))
        pwd.append(random.choice(string.ascii_uppercase))
        pwd.append(str(random.randint(0,9)))
        count = count + 1
    random.shuffle(pwd)
    return ''.join(pwd)



def main():
    print("Hello, welcome to Password Locker.")

    while True:
        print('\n')
        print("Use the following short codes for navigation: ca - create a new account, da - delete your account, li - log in to your account, ex - exit application")
        short_code = input()
        if short_code == 'ca':
            print('Please fill in the following details to create a new account')
            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Username...")
            username = input()

            print("Ensure your password ")
            print("Password ...")
            password = input()

            print('\n')
            save_user(create_user(f_name, l_name, username, password))
            print('\n')

            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')

        