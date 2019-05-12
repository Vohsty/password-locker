import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
username_login
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("Steve", "Kimanthi", "Vohsty", "shazam")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        self.assertEqual(self.new_user.f_name, "Steve")
        self.assertEqual(self.new_user.l_name, "Kimanthi")
        self.assertEqual(self.new_user.username, "Vohsty")
        self.assertEqual(self.new_user.password, "shazam")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to user array
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()