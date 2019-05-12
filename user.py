class User:
    """
    Class to generate new instances of users
    """
    user_list= [] # Empty user list

    def __init__(self, f_name, l_name, username_login, password_login):
        '''
        To take user input to create a new user
        '''
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password

   