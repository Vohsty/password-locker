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

