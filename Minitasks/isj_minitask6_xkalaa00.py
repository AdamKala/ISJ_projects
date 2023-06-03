class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
p0 = Point()
print(p0) # Point(0, 0)

p1 = Point(3, 4)
result = p0 - p1
print(result) # Point(-3, -4)