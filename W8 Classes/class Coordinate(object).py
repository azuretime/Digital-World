class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        # Tutor's test cases don't test for it, but you should check if other is a Coordinate.
        if not isinstance(other, Coordinate):
            return false
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        # It's best to specify __ne__ along with __eq__.
        # Otherwise, you can have == and != both be true.
        return not self==other



#My anw
class Coordinate(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def translate(self, dx, dy): 
        self.x =self.x + dx
        self.y =self.y + dy
        return (self.x, self.y)
        
    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.__dict__ == other.__dict__
        else:
            return False
        

       

p = Coordinate()
print p.x, p.y
print p.magnitude()
p.x = 3
p.y = 4
print p.magnitude()
q = Coordinate(3,4)
print p == q
q.translate(1,2)
print q.x
print p == q