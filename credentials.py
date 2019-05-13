class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []

    def __init__(self, username, account, acc_username, acc_password):
        '''
        Take input to create new credentials
        '''
        self.username = username
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credential(self):
        '''
        save_credential method saves user objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, username, account):
        '''
        Method that takes in an account name and returns credentials that matches that account.
        Args:
            account:  account to search for
        Returns :
            Credentials of account that matches the account name
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account and credentials.username == username:
                return credentials

    @classmethod
    def credential_exist(cls, account):
        '''
        Method that checks if a credentials exists from the credentials array.
        Args:
            account:  account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user array
        '''
        return cls.credentials_list