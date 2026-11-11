class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError('a possitive number!!')
        
        self._capacity = capacity
        self._size = 0
        
    def __str__(self):
            return '🍪' * self.size


    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError()
        else:
            self._size += n


    def withdraw(self, n):
        if self._size < n:
            raise ValueError()
        else:
            self._size -= n
        


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
