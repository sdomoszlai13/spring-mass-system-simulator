class Fixture:
    def __init__(self, i_pos):
        self.pos[0] = i_pos[0]
        self.pos[1] = i_pos[1]


class Mass:
    def __init__(self, i_m, i_pos, i_v):
        self.m = i_m
        self.pos[0] = [i_pos[0], i_pos[1]]
        self.v[0] = [i_v[0], i_v[1]]


class Spring:
    """Creates a spring that connects a fixture and a mass, or two masses.
    Attributes:
    -rest length
    -stiffness parameter
    -connection points"""

    def __init__(self, l0, k, conn):
        self.l0 = l0
        self.k = k
        self.conn[0] = conn[0]
        self.conn[1] = conn[1]
    
    def connectMassesAndFixtures(self):
        pass
    def connectMassesAndSprings(self):
        pass


class SpringMassSystem:
    def __init__(self, masses, springs, timestep, gravity):
        self.masses = masses
        self.springs = springs
        self.timestep = timestep
        self.gravity = gravity
    def run(self):
        pass


class Trajectory:
    def __init__(self, mass):
        self.x = mass.pos[0][0]
        self.y = mass.pos[0][1]
