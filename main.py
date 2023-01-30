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

    def __init__(self, fixtures, masses, springs, timesteps = 100, g = 9.81):
        self.fixtures = fixtures
        self.masses = masses
        self.springs = springs
        self.timesteps = timesteps
        self.g = g
        self.delta_t = 1 / self.timesteps
        # Create arrays for force
        self.f0 = [0 for m in self.masses]
        self.f1 = [(m.m * self.g) for m in self.masses]
        self.forces = [list(x) for x in zip(self.f0, self.f1)]
        
        self.lengths = []
        for m in self.masses:
            self.lengths.append([])

    def run(self):
        # Run simulation

        # Create time steps
        self.times = np.linspace(0, 1, int(self.timesteps))

        for t in self.times:
            self.update()
        for m in self.masses:
            print(f"Trajectory of mass: {m.trajectory}")
        self.plot()
        print("Plot finished")

    
    def update(self):
        """Update position and velocity of a mass,
        the force acting on it and the length of the springs"""

        # Update forces
        print("Updating forces...")
        for m in self.masses:
            i = 0
            for elem in m.attached: # [other_mass, stiffness_constant, rest_length]
                self.forces[i][0] += -elem[1] * (np.linalg.norm(elem[0].pos[0] - m.pos[0]) - elem[2])
                self.forces[i][1] += -elem[1] * (np.linalg.norm(elem[0].pos[1] - m.pos[1]) - elem[2])
            i = i + 1

        print("Updating positions...")
        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * self.delta_t
            m.pos[1] += m.v[1] * self.delta_t
            m.trajectory.append(m.pos[:]) # Deep copy of pos
            print(f"Added position: {m.trajectory[-1]}")

        print("Updating velocities...")
        # Update velocities
        for m in self.masses:
            i = 0
            m.v[0] += self.forces[i][0] / m.m * self.delta_t
            m.v[1] += self.forces[i][1] / m.m * self.delta_t
            i = i + 1

        print("Updating lengths...")
        # Update lengths
        for s in self.springs:
            i = 0
            s.l = np.linalg.norm([s.conn[0].pos[0] - s.conn[1].pos[0],
            s.conn[0].pos[1] - s.conn[1].pos[1]])
            self.lengths[i].append(s.l)
            i = i + 1

    def save(self, pos, v, l):
        # Save to csv file
        pass

    def plot(self):
        # Plot trajectories
        # fig, ax = plt.subplots(figsize = (10, 6))
        # plt.plot([x for x in range(10)])
        # plt.show()
        # ax.plot(self.masses[0].trajectory)
        plt.scatter(x=[x[0] for x in self.masses[0].trajectory], y=[y[1] for y in self.masses[0].trajectory])
        plt.show()
