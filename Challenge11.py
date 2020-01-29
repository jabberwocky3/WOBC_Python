import sys
arg1 = float(sys.argv[1])
arg2 = float(sys.argv[2])


class Sphere():
    ''' Creates a class with methods that calculate surface area, volume, and have the option to adjust radius '''
    pi = 3.14

    def __init__(self,radius):
        self.radius=radius

    def get_surface_area(self):
        print(f"The Surface Area is of the Sphere is: " + str(((self.radius**2)*4*(self.pi))))

    def get_volume(self):
        print(f"The volume of the sphere is: " + str(((self.radius**3)*(self.pi)*(4/3))))

    def set_radius(self, x):
        self.radius = x
        print(f"The new radius is:  {x}")


if __name__ == "__main__":
    sphere = Sphere(arg1) ##input initial value of the radius
    print(f"The radius is: {arg1}")
    sphere.get_surface_area()
    sphere.get_volume()
    sphere.set_radius(arg2) #inputs a second value to test
    sphere.get_surface_area()
    sphere.get_volume()
