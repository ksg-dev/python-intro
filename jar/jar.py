class Jar:
    # class like form/survey - instance is individual form/survey completed w unique info
    # creating Jar - each "instance" is new jar - but each jar has capacity of 12
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        return '🍪' * (self.size)

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity Error")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Not enough cookies!")
        if size > 12:
            raise ValueError("Too many cookies!")
        self._size = size



jar = Jar()
print(str(jar))




