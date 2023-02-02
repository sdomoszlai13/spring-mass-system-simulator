import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Fixture:
    """Initialize a fixture"""

    def __init__(self, pos):
        self.pos = pos
        self.attached = [] # Other mass/fixture, spring constant, rest length


class Mass:
    """Initialize a mass"""

    def __init__(self, m, pos, v):
        self.m = m
        self.pos = pos
        self.v = v
        self.f = []
        self.attached = []
        self.trajectory = [pos]


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

        # Attach spring to second element (fixture/mass)
        self.conn[0].attached.append([conn[1], self.k, self.l])
        self.conn[1].attached.append([conn[0], self.k, self.l])


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
        self.trajectories = [[[0, 4], [3, 8]]]

        for m in self.masses:
            m.f = [0, m.m * self.g]


    def update(self):
        """Update position and velocity of a mass,
        the force acting on it and the length of the springs"""

        # Update forces
        for m in self.masses:
            m.f = [0, 0]
            for elem in m.attached: # elem = [other_mass_or_fixture, stiffness_constant, rest_length]
                m.f[0] += -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((np.array(m.pos[0]) - np.array(elem[0].pos[0])) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos))))
                m.f[1] += -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((np.array(m.pos[1]) - np.array(elem[0].pos[1])) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)))) + m.m * self.g

        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * self.delta_t
            m.pos[1] += m.v[1] * self.delta_t
            m.trajectory.append(m.pos[:]) # Deep copy of pos
            print(f"Added to trajectory: {m.pos}")

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
        """
        # Plot trajectories
        for t_i in range(len(self.times)):
            #print(f"Plotting point {t_i}...")
            for m in self.masses:
                plt.scatter(m.trajectory[t_i][0], m.trajectory[t_i][1])

        for m in self.masses:
            plt.scatter(x = [x[0] for x in self.masses[0].trajectory], y = [y[1] for y in self.masses[0].trajectory], s = 0.1)

        # First dot in green
        for m in self.masses:
            plt.scatter(x = m.trajectory[0][0], y = m.trajectory[0][1], c = "green")

        # Last dot in red
        for m in self.masses:
            plt.scatter(x = m.trajectory[-1][0], y = m.trajectory[-1][1], c = "red")
        
        plt.show()
        """

    def run(self):
        """Runs the simulation"""

        # Create time steps
        self.times = np.linspace(0, 1, self.timesteps)

        # Update forces, positions and velocities. Creates m.trajectory array for each m
        for t in self.times:
            self.update()

        # Save trajectories of all masses in a single array (trajectories).
        # One element of the array contains the coordinates of all masses at a given point in time
        
        # self.trajectories = [self.timesteps, 2, len(self.masses)]
        self.trajectories = []



        for t in range(len(self.times)):
            x_coords = [m.trajectory[t][0] for m in self.masses]
            y_coords = [m.trajectory[t][1] for m in self.masses]
            self.trajectories.append([x_coords, y_coords])

        a = Animator(self)
        a.animate()

        """
        print("Begin plot")
        for f in self.fixtures:
            plt.scatter(f.pos[0], f.pos[1], c = "green")
        for t in range(self.timesteps):
            plt.scatter(self.trajectories[t][0], self.trajectories[t][1], c = "blue", s = 0.2)
        print("Plot finished")
        """

        # print("Beginning plot")
        # animator = Animator(sms = self, draw_trace = True)
        # animator.animate()
        # plt.show()
        # print("Plot finished")


# -----------------------------------------------

class Animator:

    def __init__(self, sms):
        self.fixtures = sms.fixtures
        self.masses = sms.masses
        self.springs = sms.springs
        self.timesteps = sms.timesteps
        self.time = sms.time
        self.delta_t = self.time / self.timesteps
        self.trajectories = sms.trajectories
        self.pause = 1000

        # Create canvas
        self.fig = plt.figure()
        self.axis = plt.axes(xlim =(-50, 50), ylim =(-50, 50))

        self.line, = self.axis.plot([], [], lw = 2)

        # Initialize coordinate arrays
        self.xdata = []
        self.ydata = []

        # Set data for line on canvas
        # def init():
        self.line.set_data([], [])
        # return self.line,



    # Called every time step
    def update(self, i):
        # Parameter for speed setting
        t = 0.1 * i

        # Update arrays for line to plot
        for coords in self.trajectories[i]:
            self.xdata.append(coords[0])
            self.ydata.append(coords[1])

        self.line.set_data(self.xdata, self.ydata)
        
        return self.line,

    def animate(self):  
        anim = animation.FuncAnimation(self.fig, self.update, frames = self.timesteps, interval = self.pause, blit = True)
        plt.show()