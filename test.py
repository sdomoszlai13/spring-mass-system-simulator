from main import *

"""Create test cases easy and fast by uncommenting the desired setup"""

def create_fixture(x, y):
    return Fixture(x, y)

def create_mass(m, x0, y0, vx0, vy0):
    return Mass(m, x0, y0, vx0, vy0)

def create_spring(l0, k, conn):
    return [Spring(l0, k, conn)]

def create_system(f, m, s, time, timesteps):
    return [SpringMassSystem(f, m, s, time, timesteps, save = False)]



# UNCOMMENT THE DESIRED TEST SETUP

"""
# 1) Pendulum starting from a horizontal position with spring at rest length

f = create_fixture(0.0, 10.0)
m1 = create_mass(1, -10.0, 10.0, 0.0, 0.0)
s1 = create_spring(10, 5000.0, [f, m1])
sms = create_system([f], [m1], [s1], 6, 20000)
sms[0].run()
"""

"""
# 2) Double pendulum with masses starting at slight displacement

f = create_fixture(0.0, 10.0)
m1 = create_mass(1, -3.0, 3.0, 0.0, 0.0)
m2 = create_mass(2, -3.0, 2.0, 0.0, 0.0)
s1 = create_spring(7.615, 5000.0, [f, m1])
s2 = create_spring(1.0, 5000.0, [m1, m2])
sms = create_system([f], [m1, m2], [s1, s2], 3, 12000)
sms[0].run()
"""

"""
# 2) Double pendulum with masses starting at vertical position
#    above the fixture

f = create_fixture(0.0, 10.0)
m1 = create_mass(1, 0.0, 13.0, 0.0, 0.0)
m2 = create_mass(2, 0.0, 16.0, -0.1, 0.0)
s1 = create_spring(3, 5000.0, [f, m1])
s2 = create_spring(3, 5000.0, [m1, m2])
sms = create_system([f], [m1, m2], [s1, s2], 6, 50000)
sms[0].run()
"""

"""
# 2) Triple pendulum with masses starting at vertical position
#    above the fixture

f = create_fixture(0.0, 10.0)
m1 = create_mass(1, 0.0, 13.0, 0.0, 0.0)
m2 = create_mass(1, 0.0, 16.0, 0.0, 0.0)
m3 = create_mass(2, -0.1, 19.0, 0.0, 0.0)
s1 = create_spring(3.0, 5000.0, [f, m1])
s2 = create_spring(3.0, 5000.0, [m1, m2])
s3 = create_spring(3.0, 5000.0, [m2, m3])
sms = create_system([f], [m1, m2, m3], [s1, s2, s3], 20, 100000)
sms[0].run()
"""

"""
# 3) Tethered chain of 3 masses connected by springs.
#    Left mass has an initial vertical velocity

f1 = create_fixture(0.0, 10.0)
f2 = create_fixture(12.0, 10.0)
m1 = create_mass(1, 3, 10, 0.0, 5.0)
m2 = create_mass(1, 6, 10, 0.0, 0.0)
m3 = create_mass(1, 9, 10, 0.0, 0.0)
s1 = create_spring(3, 500.0, [f1, m1])
s2 = create_spring(3, 5000.0, [m1, m2])
s3 = create_spring(3, 5000.0, [m2, m3])
s4 = create_spring(3, 5000.0, [m3, f2])
sms = create_system([f1, f2], [m1, m2, m3], [s1, s2, s3, s4], 5, 40000)
sms[0].run()
"""



