

class Punto2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        if isinstance(self.x, int):
            return self.x
        else:
            raise TypeError("El punto x debe de ser un numero entero")
        
    def get_y(self):
        if isinstance(self.y, int):
            return self.y
        else:
            raise TypeError("El punto y debe de ser un numero entero")
        
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    
    def traslacion(self, a, b):
        self.x += a
        self.y += b

    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)

class Punto3D(Punto2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def get_z(self):
        if isinstance(self.z, int):
            return self.z
        else:
            raise TypeError("El punto z debe de ser un numero entero")
        
    def set_z(self, z):
        self.z = z

    
    def traslacion(self, a, b, c):
        super().traslacion(a, b)
        self.z += c

    def __str__(self):
        return "{}; Z: {}".format(super().__str__(), self.z)
    
if __name__ == "__main__":
    a = Punto2D(1, 2) 
    print("A = {}".format(a)) 
 
    a.traslacion(-1, -2) 
    print("A = {}".format(a)) 
 
    b = Punto2D(-3, 0) 
    b.traslacion(5, -1) 
    print("B = {}".format(b))

    c = Punto3D(1,5,-3) 
    c.traslacion(0, -2, 1) 
    print("C = {}".format(c)) 
