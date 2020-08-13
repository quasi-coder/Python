class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps
        self.load = 0

    def connect(self,amps):
        if self.load+amps>self.capacity:
            raise Exception('Exceeds capacity')
        elif self.load+amps<0:
            raise Exception('Negative capacity')
        else:
            self.load+=amps
        

#create a 20A circuit breaker
cb = CircuitBreaker(20)
print(cb.load)
cb.connect(25)