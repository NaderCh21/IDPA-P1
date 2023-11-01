# Define a class to encapsulate the Wagner-Fisher algorithm and related methods
class WagnerFisher:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.M = len(A)
        self.N = len(B)
        self.Distance = [[None for _ in range(self.N + 1)] for _ in range(self.M + 1)]

    # Function to calculate the update cost between two words
    @staticmethod
    def costUpdWord(A, B):
        return 0 if A == B else 1

    # Function to calculate the insertion cost
    @staticmethod
    def costInsWord():
        return 1

    # Function to calculate the deletion cost
    @staticmethod
    def costDelWord():
        return 1

    # Main function to calculate the minimum distance between two arrays of words
    def calculate_distance(self):
        self.Distance[0][0] = 0
        for i in range(1, self.M + 1):
            self.Distance[i][0] = self.Distance[i - 1][0] + self.costDelWord()
        for j in range(1, self.N + 1):
            self.Distance[0][j] = self.Distance[0][j - 1] + self.costInsWord()
        for i in range(1, self.M + 1):
            for j in range(1, self.N + 1):
                self.Distance[i][j] = min(
                    self.Distance[i - 1][j - 1]
                    + self.costUpdWord(self.A[i - 1], self.B[j - 1]),
                    self.Distance[i - 1][j] + self.costDelWord(),
                    self.Distance[i][j - 1] + self.costInsWord(),
                )
        return self.Distance[self.M][self.N]


# Function to calculate the similarity between two paths
def getSimPath(path1, path2):
    array1 = path1.split("/")
    array2 = path2.split("/")
    wf = WagnerFisher(array1, array2)
    distance = wf.calculate_distance()
    sim = 1 - (distance / (len(array1) + len(array2)))
    return sim
