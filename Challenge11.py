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

        
# Testing Section
# sphere = Sphere(1) ##input initial value of the radius
# sphere.get_surface_area()
# sphere.get_volume()
# sphere.set_radius(4) #inputs a second value to test
# sphere.get_surface_area()
# sphere.get_volume()
