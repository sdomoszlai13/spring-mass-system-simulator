from main import *

"""Create a double pendulum as a test the fast and easy way"""

def create_fixture(x, y):
    return Fixture(x, y)

def create_mass(m, x0, y0, vx0, vy0):
    return Mass(m, x0, y0, vx0, vy0)

def create_spring(l0, k, conn):
    return [Spring(l0, k, conn)]

def create_system(f, m, s):
    return [SpringMassSystem(f, m, s, time = 3, timesteps = 12000, save = False)]


f = create_fixture(0.0, 10.0)
m1 = create_mass(1, -3.0, 3.0, 0.0, 0.0)
m2 = create_mass(2, -3.0, 2.0, 0.0, 0.0)
s1 = create_spring(7.615, 5000.0, [f, m1])
s2 = create_spring(1.0, 5000.0, [m1, m2])
sms = create_system([f], [m1, m2], [s1, s2])
sms[0].run()