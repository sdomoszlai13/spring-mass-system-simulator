import numpy as np

class Fixture:
    """Initialize a fixture"""

    def __init__(self, pos):
        self.pos = pos
        self.attached = []


class Mass:
    """Initialize a mass."""

    def __init__(self, m, pos, v):
        self.m = m
        self.pos = pos
        self.v = v
        self.attached = []


class Spring:
    """Initialize a spring that connects a fixture and a mass, or two masses.
    Attributes:
    -l0: rest length
    -k: stiffness parameter
    -c: connection points (array)"""

    def __init__(self, l0, k, conn):
        self.l = l0
        self.k = k
        self.conn = conn
        conn[0].attached.append([conn[1], self.k, self.l])
        conn[1].attached.append([conn[0], self.k, self.l])


class SpringMassSystem:
    """Initialize the spring mass system"""

    def __init__(self, masses, springs, timesteps = 2000, g = 9.81):
        self.masses = masses
        self.springs = springs
        self.timesteps = timesteps
        self.gravity = g
        self.f0 = [0, 0]
        self.f1 = [0, 0]

    def run(self):
        self.times = np.linspace(0, 1, self.timesteps)

        # Create arrays for force
        f0 = [0 for m in self.masses]
        f1 = [self.masses[i].m * self.g for i in self.masses]
        forces = zip(f0, f1)

        for t in self.times:
            self.update(self, forces)

    
    def update(self, forces):
        """"Update position and velocity of a mass,
        the force acting on it and the length of the springs."""

        delta_t = 1 / self.timesteps

        # Update forces
        for m in self.masses:
            i = 0
            for elem in m.attached: # [other_mass, stiffness_constant, rest_length]
                forces[i][0] += -elem[1] * (np.linalg.norm(elem[0].pos[0] - m.pos[0]) - elem[2])
                forces[i][1] += -elem[1] * (np.linalg.norm(elem[0].pos[1] - m.pos[1]) - elem[2])
            i = i + 1

        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * delta_t
            m.pos[1] += self.m.v[1] * delta_t

        # Update velocities
        for m in self.masses:
            i = 0
            m.v[0] += forces[i][0] / self.m.m * delta_t
            m.v[1] += forces[i][1] / self.m.m * delta_t
            i = i + 1

        # Update spring lengths
        for s in self.springs:
            s.l = np.linalg.norm([s.conn[0].pos[0] - s.conn[1].pos[0], s.conn[0].pos[1] - s.conn[1].pos[1]])


class Trajectory:
    def __init__(self, mass):
        self.x = mass.pos[0]
        self.y = mass.pos[1]


