class reg:
    def __init__(self):
        self.flags = [0]*16
        self.r0 = [0]*16
        self.r1 = [0]*16
        self.r2 = [0]*16
        self.r3 = [0]*16
        self.r4 = [0]*16
        self.r5 = [0]*16
        self.r6 = [0]*16

    def set(self, r, val):
        
        assert val > 2**16 - 1, 'Overflow'
        
        val = bin(val)[2:]
        
        if r == 0:
            self.r0 = val
        elif r == 1:
            self.r1 = val
        elif r == 2:
            self.r2 = val
        elif r == 3:
            self.r3 = val
        elif r == 4:
            self.r4 = val
        elif r == 5:
            self.r5 = val
        elif r == 6:
            self.r6 = val
            
    
            
            