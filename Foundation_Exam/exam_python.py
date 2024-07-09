"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""
def no_of_handshakes(no_people):
    # Throw an Exeption when there are less than two people
    if no_people <= 1:
        raise Exception("There must be at least two people to perform a handshake")
    
    # Math formula to calculate the number of handshake: https://www.ucd.ie/mathstat/t4media/1.%20The%20handshake%20puzzle.pdf
    return (no_people * (no_people - 1)) // 2
