from main import *


def create_fixture(pos):
    return Fixture(pos)

def create_mass(m, pos, v):
    return Mass(m, pos, v)

def create_spring(l0, k, conn):
    return [Spring(l0, k, conn)]

def create_system(f, m, s):
    return [SpringMassSystem(f, m, s, time = 3, timesteps = 12000)]


f = create_fixture([0.0, 10.0])
m1 = create_mass(1, [-3.0, 3.0], [0.0, 0.0])
m2 = create_mass(2, [-3.0, 2.0], [0.0, 0.0])
s1 = create_spring(7.615, 5000.0, [f, m1])
s2 = create_spring(1.0, 5000.0, [m1, m2])
sms = create_system([f], [m1, m2], [s1, s2])
sms[0].run()