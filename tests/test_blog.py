import unittest
from app.models import Blog
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Blog(title='inspiration',pitch= 'you good')

    def tearDown(self):
        Blog.query.delete ( )


    def test_check_instance_variables(self):
            self.assertEquals ( self.new_pitch.title , 'inspiration' )
            self.assertEquals ( self.new_pitch.pitch , 'you good' )
