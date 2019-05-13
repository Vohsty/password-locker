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

        elif short_code == 'da':
            print('Enter the username of the account you would like to delete')
            delete_name = input()
            if check_existing_users(delete_name):
                search_user = find_user(delete_name)
                print("Enter your password")
                password = input()
                if password == search_user.password_login:
                    print(f"Are you sure you want to delete {search_user.f_name} {search_user.l_name}")
                    print("y - yes, n - no")
                    yesNo = input().lower()
                    if yesNo == 'y':
                        delete_user(search_user)
                        print(f"{search_user.f_name} {search_user.l_name} has been deleted")
                    elif yesNo == 'n':
                        print("User still present")
            else:
                print("Account does not exist")


        elif short_code == 'li':
            print("Welcome to log in")
            print("Enter your username: ")
            username = input()
            if check_existing_users(username):
                print("Enter your password:")
                password = input()
                search_user = find_user(username)
                if (password == search_user.password):
                    print(f"Welcome {search_user.f_name} {search_user.l_name}")

                    while True:
                        print('\n')
                        print('\n')
                        print("What would you like to do: cc - create a new credential, dc - delete credential, vc - view credential, va - view all credentials, lo - log out")
                        acc_nav = input()

                        if acc_nav == 'cc':
                            print ("Account type eg. Github ....")
                            account = input()

                            print("Account username ...")
                            acc_username = input()

                            print("Account password...")
                            print("Would you like an auto generated Password?")
                            print("y - Yes, n - No")
                            decision = input().lower()
                            if decision == 'y':
                                print('\n')
                                print("Please enter desired password length")
                                try:
                                    length = int(input())
                                except ValueError:
                                    print("Only numbers accepted")
                                    break
                                acc_password = generate_password(length)
                                print('\n')
                                print(f"Your new password for {account} is {acc_password}.")
                            elif decision == 'n':
                                print('\n')
                                print("Please enter your new password")
                                acc_password = input()
                            else:
                                print('\n')
                                print("Use either y or n")
                                print('\n')

                            print('\n')
                            save_credential(create_credential(username, account, acc_username, acc_password))
                            print('\n')

                            print('\n')
                            print(f"New Credentials for {account} created")
                            print('\n')

                        elif acc_nav == 'dc':
                            print('Enter the account name of the credential you would like to delete')
                            delete_name = input()
                            if check_existing_credential(delete_name):
                                search_cred = find_credential(username, delete_name)
                                print(f"Are you sure you want to delete {search_cred.account} credentials")

                                print('\n')
                                print("y - Yes, n - No")
                                print('\n')
                                decision = input().lower()
                                if decision == 'y':
                                    delete_credential(search_cred)
                                    print('\n')
                                    print(f"{search_cred.account} credentials have been deleted")
                                    print('\n')
                                else:
                                    print('\n')
                                    print("Credentials still available")
                                    print('\n')
                            else:
                                print('\n')
                                print ("The credential does not exist")
                                print('\n')

                       