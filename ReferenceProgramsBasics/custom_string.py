class CustomStr(str):
    """String class with added next() method"""
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        if self.index == 0:
            return self.data[0]

        self.index = self.index + 1
        return self.data[self.index]
