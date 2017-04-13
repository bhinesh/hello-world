from math import sqrt

class Vector(object):
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates=tuple(coordinates)
            self.dimension=len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self,v):
        return self.coordinates == v.coordinates

    def plus(self,v):
        new_coordinates=[x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self,v):
        new_coordinates=[x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self,c):
        new_coordinates=[c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared=[x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
        
    def dot(self,v):
        return sum(x*y for x,y in zip(self.coordinates,v.coordinates)
                   
    def test(self):
        return 1
    
v1 = Vector([-0.221,7.437])
v2=Vector([8.813,-1.331,-6.247])
v3=Vector([5.581,-2.136])
v4=Vector([1.996,3.108,-4.554])
print(v1.magnitude())
print(v2.magnitude())
print(v3.normalized())
print(v4.normalized())
