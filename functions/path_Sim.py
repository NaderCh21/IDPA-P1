class WagnerFisher:
    """Class to encapsulate the Wagner-Fisher algorithm for string distance calculation."""

    def __init__(self, A, B):
        """Initialize the WagnerFisher object with two strings."""
        self.A = A  # First string
        self.B = B  # Second string
        self.M = len(A)  # Length of the first string
        self.N = len(B)  # Length of the second string
        # Initialize a matrix to store distances between substrings
        self.Distance = [[None for _ in range(self.N + 1)] for _ in range(self.M + 1)]

    @staticmethod
    def costUpdWord(A, B):
        """Calculate the update cost between two characters."""
        # If characters are the same, cost is 0, otherwise it's 1
        return 0 if A == B else 1

    @staticmethod
    def costInsWord():
        """Calculate the insertion cost."""
        # Cost of inserting a character is always 1
        return 1

    @staticmethod
    def costDelWord():
        """Calculate the deletion cost."""
        # Cost of deleting a character is always 1
        return 1

    def calculate_distance(self):
        """Calculate the minimum distance between two strings."""
        # Base case: distance between empty strings is 0
        self.Distance[0][0] = 0
        # Initialize the first column of the matrix
        for i in range(1, self.M + 1):
            self.Distance[i][0] = self.Distance[i - 1][0] + self.costDelWord()
        # Initialize the first row of the matrix
        for j in range(1, self.N + 1):
            self.Distance[0][j] = self.Distance[0][j - 1] + self.costInsWord()
        # Populate the matrix with distances
        for i in range(1, self.M + 1):
            for j in range(1, self.N + 1):
                # Calculate the minimum distance considering insertion, deletion, and update
                self.Distance[i][j] = min(
                    self.Distance[i - 1][j - 1]
                    + self.costUpdWord(self.A[i - 1], self.B[j - 1]),
                    self.Distance[i - 1][j] + self.costDelWord(),
                    self.Distance[i][j - 1] + self.costInsWord(),
                )
        # Return the distance between the two full strings
        return self.Distance[self.M][self.N]


def getSimPath(path1, path2):
    """Calculate the similarity between two paths."""
    # Split paths into arrays based on the "/" delimiter
    array1 = path1.split("/")
    array2 = path2.split("/")
    # Create a WagnerFisher object with the two arrays
    wf = WagnerFisher(array1, array2)
    # Calculate the distance between the two arrays
    distance = wf.calculate_distance()
    # Calculate the similarity score based on the distance
    sim = 1 - (distance / (len(array1) + len(array2)))
    return sim


if __name__ == "__main__":
    # Potential testing or further code can be added here
    pass
