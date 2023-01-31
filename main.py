import numpy as np
import matplotlib.pyplot as plt

class Fixture:
    """Initialize a fixture"""

    def __init__(self, pos):
        self.pos = pos
        self.attached = []


class Mass:
    """Initialize a mass"""

    def __init__(self, m, pos, v):
        self.m = m
        self.pos = pos
        self.v = v
        self.f = [0, 0]
        self.attached = []
        self.trajectory = []


class Spring:
    """Initialize a spring that connects a fixture and a mass, or two masses.
    Attributes:
    -l0: rest length
    -k: stiffness parameter
    -c: connection points (list of Mass and/or Fixture objects)"""

    def __init__(self, l0, k, conn):
        self.l = l0
        self.k = k
        self.conn = conn
        conn[0].attached.append([conn[1], self.k, self.l])
        conn[1].attached.append([conn[0], self.k, self.l])


class SpringMassSystem:
    """Initialize the spring mass system.
    Fixtures, masses, and springs must be provided as lists"""

    def __init__(self, fixtures, masses, springs, time = 1, timesteps = 100, g = 9.81):
        self.fixtures = fixtures
        self.masses = masses
        self.springs = springs
        self.g = -g
        self.timesteps = timesteps
        self.time = time
        self.delta_t = time / timesteps

        for m in self.masses:
            m.f = [0, m.m * self.g]


    def run(self):
        # Run simulation

        # Create time steps
        self.times = np.linspace(0, 1, self.timesteps)

        for t in self.times:
            self.update()
        self.plot()


    def update(self):
        """Update position and velocity of a mass,
        the force acting on it and the length of the springs"""

        # Update forces
        for m in self.masses:
            for elem in m.attached: # elem = [other_mass_or_fixture, stiffness_constant, rest_length]
                m.f[0] = -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((m.pos[0] - elem[0].pos[0]) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos))))
                m.f[1] = -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((m.pos[1] - elem[0].pos[1]) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)))) + m.m * self.g

        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * self.delta_t
            m.pos[1] += m.v[1] * self.delta_t
            m.trajectory.append(m.pos[:]) # Deep copy of pos

        # Update velocities
        for m in self.masses:
            m.v[0] += m.f[0] / m.m * self.delta_t
            m.v[1] += m.f[1] / m.m * self.delta_t


    def save(self, pos, v, l):
        # Save to csv file
        pass

    def plot(self):
        # Plot trajectories
        # fig, ax = plt.subplots(figsize = (10, 6))
        # plt.plot([x for x in range(10)])
        # plt.show()
        # ax.plot(self.masses[0].trajectory)

        # Plot fixtures
        for f in self.fixtures:
            plt.scatter(x = f.pos[0], y = f.pos[1], s = 100, marker = "H")

        # Plot trajectories
        for m in self.masses:
            plt.scatter(x = [x[0] for x in self.masses[0].trajectory], y = [y[1] for y in self.masses[0].trajectory], s = 0.1)

        # First dot in green
        for m in self.masses:
            plt.scatter(x = m.trajectory[0][0], y = m.trajectory[0][1], c = "green")

        # Last dot in red
        for m in self.masses:
            plt.scatter(x = m.trajectory[-1][0], y = m.trajectory[-1][1], c = "red")
        
        plt.show()
