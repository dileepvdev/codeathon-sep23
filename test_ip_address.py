import unittest
from validate_ip_address import is_valid_ip_address

class TestIsValidIPAddress(unittest.TestCase):
    def test_is_valid_ip_address_empty(self):
        self.assertFalse(is_valid_ip_address(''))

    def test_is_valid_ip_address_short(self):
        self.assertFalse(is_valid_ip_address('127.0.0'))

    def test_is_valid_ip_address_long(self):
        self.assertFalse(is_valid_ip_address('127.0.0.1.1'))

    def test_is_valid_ip_address_out_of_range(self):
        self.assertFalse(is_valid_ip_address('256.0.0.0'))

    def test_is_valid_ip_address_non_numeric(self):
        self.assertFalse(is_valid_ip_address('127.0.0.a'))

    def test_is_valid_ip_address_valid(self):
        self.assertTrue(is_valid_ip_address('127.0.0.1'))

if __name__ == '__main__':
    unittest.main()