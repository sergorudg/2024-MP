import math

class CartesianCoordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class SphericalCoordinate:
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi

    def __str__(self):
        return f"(r={self.r:.2f}, theta={self.theta:.2f}°, phi={self.phi:.2f}°)"

class FlyingObject:
    def __init__(self, id, cartesian_coordinate, velocity):
        self.id = id
        self.cartesian_coordinate = cartesian_coordinate
        self.velocity = velocity
        self.spherical_coordinate = None

    def __str__(self):
        return f"ID: {self.id}, Cartesian: {self.cartesian_coordinate}, Velocity: {self.velocity}, Spherical: {self.spherical_coordinate}"


class Radar:
    instance = None

    def __init__(self, cartesian_coordinate):
        if Radar.instance is None:
            Radar.instance = self
            self.cartesian_coordinate = cartesian_coordinate

    def __str__(self):
        return f"Cartesian: {self.cartesian_coordinate}"


def cartesian_to_spherical(cartesian_coordinate):
    r = math.sqrt(cartesian_coordinate.x**2 + cartesian_coordinate.y**2 + cartesian_coordinate.z**2)
    theta = math.atan2(cartesian_coordinate.y, cartesian_coordinate.x) * 180 / math.pi
    phi = math.acos(cartesian_coordinate.z / r) * 180 / math.pi
    return SphericalCoordinate(r, theta, phi)


def move_object(object, time):
    object.cartesian_coordinate.x += object.velocity[0] * time
    object.cartesian_coordinate.y += object.velocity[1] * time
    object.cartesian_coordinate.z += object.velocity[2] * time
    object.spherical_coordinate = cartesian_to_spherical(object.cartesian_coordinate)


def main():
    radar_cartesian_coordinate = CartesianCoordinate(float(input("Введите x-координату радара (м): ")), float(input("Введите y-координату радара (м): ")), float(input("Введите z-координату радара (м): ")))
    num_objects = int(input("Введите количество летающих объектов: "))
    objects = []
    for i in range(num_objects):
        x, y, z, vx, vy, vz = map(float, input(f"Введите декартовы координаты и проекции скорости {i+1}-го объекта (м/с): ").split())
        objects.append(FlyingObject(i+1, CartesianCoordinate(x, y, z), (vx, vy, vz)))
    
    radar = Radar(radar_cartesian_coordinate)

    for object in objects:
        object.spherical_coordinate = cartesian_to_spherical(object.cartesian_coordinate)
    
    print("Текущие сферические координаты объектов:")
    for object in objects:
        print(object)
    
    time = float(input("Введите время в секундах: "))
    
    for object in objects:
        move_object(object, time)
    
    print(f"Сферические координаты объектов через {time} секунд:")
    for object in objects:
        print(object)


if __name__ == "__main__":
    main()

