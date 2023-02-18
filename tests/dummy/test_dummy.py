import unittest
from dummy.dummy import Dummy

class DummyTest(unittest.TestCase):

    def test_dummy (self):   
        sut = Dummy()
        self.assertEqual(sut.dummy_method(),True)
    