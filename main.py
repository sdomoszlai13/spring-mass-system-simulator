import numpy as np


class Fixture:
    """Initialize a fixture"""

    def __init__(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]


class Mass:
    """Initialize a mass."""

    def __init__(self, m, pos, v):
        self.m = m
        self.pos = pos
        self.v = v


class Spring:
    """Initialize a spring that connects a fixture and a mass, or two masses.
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
    def __init__(self, masses, springs, timesteps, gravity):
        self.masses = masses
        self.springs = springs
        self.timesteps = timesteps
        self.gravity = gravity

    def run(self):
        self.times = np.linspace(0, 1, self.timesteps)
        for t in times:
            for m in masses:
                updateXY(m)
                updateTrajectory(m)

    def updateF(self):
        """Update force acting on a mass."""
        for m in self.masses:
            f[0] = -k * self.mass.pos[0]
            f[1] = 
    
    def update(self):
        """"Update position and velocity of a mass."""

        delta_t = 1 / self.timesteps
        self.m.pos[0] += self.m.v[0] * delta_t
        self.m.pos[1] += self.m.v[1] * delta_t


        self.m.v[0] += f / self.m.m * delta_t
        self.m.v[1] += f / self.m.m * delta_t


class Trajectory:
    def __init__(self, mass):
        self.x = mass.pos[0]
        self.y = mass.pos[1]