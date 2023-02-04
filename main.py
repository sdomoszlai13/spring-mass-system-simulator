import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""
 Spring Mass System Simulator

 Simulates a system of connected springs, masses and fixtures.
 The trajectory of the masses can be plotted and saved in a text file.
"""


# Input funcionality

def smsInit():
    """User interface for data input"""

    print("To simulate a spring mass system, pass arrays of fixtures, masses, and springs. \n\n")

    # Get information for fixture(s)
    num_fixtures = input("Enter the number of fixtures you wish to simulate: ")
    print("The input format for the properties of fixtures is: [x0, y0].")
    print("x0, y0: position of fixture")

    fixtures = []

    for i in num_fixtures:
        x = input(f"Enter x coordinate of fixture {i}: ")
        y = input(f"Enter y coordinate of fixture {i}: ")
        fixtures.append(Fixture(x, y))


    # Get information for mass(es)
    num_masses = input("Enter the number of masses you wish to simulate: ")
    print("The input format for the properties of masses is: m, [x0, y0], [vx0, vy0].")
    print("m: mass")
    print("x0, y0: initial position of mass")
    print("vx0, vy0: initial velocity of mass")

    masses = []

    for i in num_masses:
        m = input(f"Enter mass of mass {i}: ")
        x0 = input(f"Enter x coordinate of initial position of mass {i}: ")
        y0 = input(f"Enter y coordinate of initial position of mass {i}: ")
        vx0 = input(f"Enter x component of initial velocity of mass {i}: ")
        vy0 = input(f"Enter y component of initial velocity of mass {i}: ")
        masses.append(Mass(m, x0, y0, vx0, vy0))


    # Get information for spring(s)
    num_springs = input("Enter the number of springs you wish to simulate: ")
    print("The input format for the properties of springs is: l0, k, conn.")
    print("l0: rest length")
    print("k: spring constant")
    print("conn: connected fixture(s) and/or mass(es) in an array")

    springs = []

    for i in num_springs:
        l0 = input(f"Enter rest length of spring {i}: ")
        k = input(f"Enter spring constant of spring {i}: ")
        obj1_name = input(f"Enter name of first connected fixture/mass: ")

        if obj1_name[0] == "f":
            obj1 = fixtures[int(obj1_name[1])]

        elif obj1_name[0] == "m":
            obj1 = masses[int(obj1_name[1])]

        else:
            # Throw exception - TO DO
            pass


        obj2_name = input(f"Enter name of second connected fixture/mass: ")

        if obj2_name[0] == "f":
            obj2 = fixtures[int(obj2_name[1])]

        elif obj2_name[0] == "m":
            obj2 = masses[int(obj2_name[1])]

        else:
            # Throw exception - TO DO
            pass

        springs.append(Spring(l0, k, [obj1, obj2]))


    return fixtures, masses, springs


class Fixture:
    """Initialize a fixture.
    Attributes:
    -pos: position
    -attached: attached objects (mass(es) and/or spring(s))"""

    def __init__(self, x, y):
        self.pos = [x, y]
        self.attached = [] # List format: [mass/fixture connected to this fixture,
                           #               spring constant of connecting spring,
                           #               rest length of connecting spring]


class Mass:
    """Initialize a mass.
    Attributes:
    -m: mass
    -pos: position
    -v: velocity
    -f: acting force
    -attached: attached objects (mass(es) and/or spring(s))
    -trajectory: trajectory
    
    Position and velocity must be provided as a list"""

    def __init__(self, m, x0, y0, vx0, vy0):
        self.m = m
        self.pos = [x0, y0]
        self.v = [vx0, vy0]
        self.f = []
        self.attached = [] # List format: [mass/fixture connected to this fixture,
                           #               spring constant of connecting spring,
                           #               rest length of connecting spring]
        self.trajectory = [self.pos]


class Spring:
    """Initialize a spring that connects a fixture and a mass, or two masses.
    Attributes:
    -l0: rest length
    -k: spring constant
    -conn: objects that the spring connects (list of mass(es) and/or fixture(s))
    
    Connecting mass(es) and/or fixture(s) must be provided as a list"""

    def __init__(self, l0, k, conn):
        self.l = l0
        self.k = k
        self.conn = conn

        # Attach spring to second element (fixture/mass)
        self.conn[0].attached.append([conn[1], self.k, self.l])
        self.conn[1].attached.append([conn[0], self.k, self.l])


class SpringMassSystem:
    """Initialize the spring mass system.
    Attributes with similar names as in Mass and Fixture class
    are defined identical.
    Additional attributes:
    -time: length of time interval to be simulated
    -timesteps: number of intervals time is to be divided into
    -g: gravitational acceleration
    -save: control of function save() that saves trajectories in a file

    Fixtures, masses, and springs must be provided as lists"""

    def __init__(self, fixtures, masses, springs, time = 1, timesteps = 100, g = 9.81, save = False):
        self.fixtures = fixtures
        self.masses = masses
        self.springs = springs
        self.g = -g
        self.timesteps = timesteps
        self.time = time
        self.delta_t = time / timesteps
        self.trajectories = []
        self.save_csv = save

        for m in self.masses:
            m.f = [0, m.m * self.g]


    def update(self):
        """Update positions and velocities of the masses, and
        the force acting on them"""

        # Update forces
        for m in self.masses:
            m.f = [0, 0]
            for elem in m.attached: # elem = [other_mass_or_fixture, spring_constant, rest_length]
                m.f[0] += -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((np.array(m.pos[0]) - np.array(elem[0].pos[0])) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos))))
                m.f[1] += -elem[1] * (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)) - elem[2]) * ((np.array(m.pos[1]) - np.array(elem[0].pos[1])) / (np.linalg.norm(np.array(elem[0].pos) - np.array(m.pos)))) + m.m * self.g

        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * self.delta_t
            m.pos[1] += m.v[1] * self.delta_t
            m.trajectory.append(m.pos[:]) # Deep copy of pos
            # print(f"Added to trajectory: {m.pos}")

        # Update velocities
        for m in self.masses:
            m.v[0] += m.f[0] / m.m * self.delta_t
            m.v[1] += m.f[1] / m.m * self.delta_t





    def save(self):
        # Save trajectories to csv file

        f = open("trajectories", "w")
        f.write(f"{self.trajectories};")
        f.close()


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

        # Update forces, positions and velocities. Create m.trajectory array for each m
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

        if self.save_csv == True:
            self.save()
            print(f"Saved trajectories to \"trajectories\"")

        # a = Animator(self)
        # a.animate()

        
        print("Begin plot")
        for f in self.fixtures:
            plt.scatter(f.pos[0], f.pos[1], c = "green", s = 80, marker = "H")
        for t in range(int(self.timesteps / 20)):
            if self.timesteps % 10 == 0: 
                plt.scatter(self.trajectories[20 * t][0], self.trajectories[10 * t][1], c = "blue", s = 0.2)
        plt.show()
        print("Plot finished")

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
        self.pause = 1
        self.j = 0

        f = open("trajectories", "w")
        for line in self.trajectories:
            f.write(f"{line}\n")
        f.close()

        # Create canvas
        self.fig = plt.figure()
        self.axis = plt.axes(xlim =(-50, 50), ylim =(-50, 50))

        self.line, = self.axis.plot([], [], "bo")

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
        # print(f"i: {i}")
        # print("Data to plot:")
        # print(f"xdata: {self.xdata}")
        # print(f"ydata: {self.ydata}")
        if i == 11999:
            f = open("xdata_ydata", "w")
            f.write(f"xdata and ydata at i = {i}: \n {self.xdata} \n {self.ydata}")
        return self.line,

    def animate(self):  
        anim = animation.FuncAnimation(self.fig, self.update, frames = self.timesteps, interval = self.pause, blit = True)
        plt.show()


# Create SpringMassSystem object based on user input and run simulation
sms = SpringMassSystem(smsInit())
sms.run()
