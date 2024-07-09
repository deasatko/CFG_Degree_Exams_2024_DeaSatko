import unittest
from exam_python import no_of_handshakes  # Import the function to be tested

# Create test suite
class TestHandshakeFunction(unittest.TestCase):

    # Test cases for valid scenarios
    def test_valid_cases(self):
        # Test cases where the function should return the correct number of handshakes
        self.assertEqual(no_of_handshakes(2), 1)
        self.assertEqual(no_of_handshakes(3), 3)
        self.assertEqual(no_of_handshakes(5), 10)
        self.assertEqual(no_of_handshakes(10), 45)
        self.assertEqual(no_of_handshakes(100), 4950)
    
    # Test cases for invalid scenarios
    def test_invalid_cases(self):
        # Test cases where the function should raise an exception
        with self.assertRaises(Exception) as context:
            no_of_handshakes(1)  # Attempting to handshake with only 1 person
        self.assertEqual(str(context.exception), "There must be at least two people to perform a handshake")
        
        with self.assertRaises(Exception) as context:
            no_of_handshakes(0)  # Attempting to handshake with 0 people
        self.assertEqual(str(context.exception), "There must be at least two people to perform a handshake")

        with self.assertRaises(Exception) as context:
            no_of_handshakes(-10)  # Attempting to handshake with a negative number of people
        self.assertEqual(str(context.exception), "There must be at least two people to perform a handshake")

# Run the test suite
if __name__ == '__main__':
    unittest.main()
