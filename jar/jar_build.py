@property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self):
        self.capacity = capacity

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self):
        self.size = size

         if capacity < 0:
            raise ValueError('Take more cookies')
        if capacity > 12:
            raise ValueError('Not enough cookies!')