import numpy as np
import matplotlib.pyplot as plt

class Fixture:
    """Initialize a fixture"""

    def __init__(self, pos):
        self.pos = np.array(pos)
        self.attached = np.array([])


class Mass:
    """Initialize a mass"""

    def __init__(self, m, pos, v):
        self.m = m
        self.pos = np.array(pos)
        self.v = np.array(v)
        self.f = np.array([0.0, 0.0])
        self.attached = np.array([])
        self.trajectory = np.array([pos])


class Spring:
    """Initialize a spring that connects a fixture and a mass, or two masses.
    Attributes:
    -l0: rest length
    -k: stiffness parameter
    -c: connection points (list of Mass and/or Fixture objects)"""

    def __init__(self, l0, k, conn):
        self.l = l0
        self.k = k
        self.conn = np.array(conn)
        self.conn[0].attached = np.array([np.concatenate((self.conn[0].attached, np.array([conn[1], self.k, self.l])), axis = 0)])
        self.conn[1].attached = np.array([np.concatenate((self.conn[1].attached, np.array([conn[0], self.k, self.l])), axis = 0)])


class SpringMassSystem:
    """Initialize the spring mass system.
    Fixtures, masses, and springs must be provided as lists"""

    def __init__(self, fixtures, masses, springs, time = 1, timesteps = 100, g = 9.81):
        self.fixtures = np.array(fixtures)
        self.masses = np.array(masses)
        self.springs = np.array(springs)
        self.g = -g
        self.timesteps = timesteps
        self.time = time
        self.delta_t = time / timesteps
        self.trajectories = np.array([[[0, 4], [3, 8]]])

        for m in self.masses:
            m.f = np.array([0, m.m * self.g])


    def update(self):
        """Update position and velocity of a mass,
        the force acting on it and the length of the springs"""

        # Update forces
        for m in self.masses:
            for elem in m.attached: # elem = [other_mass_or_fixture, stiffness_constant, rest_length]
                m.f[0] = -elem[1] * (np.linalg.norm(elem[0].pos - m.pos) - elem[2]) * ((m.pos[0] - elem[0].pos[0]) / (np.linalg.norm(elem[0].pos - m.pos)))
                m.f[1] = -elem[1] * (np.linalg.norm(elem[0].pos - m.pos) - elem[2]) * ((m.pos[1] - elem[0].pos[1]) / (np.linalg.norm(elem[0].pos - m.pos))) + m.m * self.g

        # Update positions
        for m in self.masses:
            m.pos[0] += m.v[0] * self.delta_t
            m.pos[1] += m.v[1] * self.delta_t
            m.trajectory = np.concatenate((m.trajectory, np.array([m.pos])[:])) # Deep copy of pos
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

        # Save trajectories of all masses in a single array.
        # One element of the array contains the coordinates of all masses at a given point in time
        
        self.trajectories = np.zeros((self.timesteps, 2, len(self.masses)))


        for t in range(len(self.times)):
            for m in self.masses:
                self.trajectories[t][0] = m.trajectory.T[0][t]
                self.trajectories[t][1] = m.trajectory.T[1][t]

        print("Begin plot")
        for f in self.fixtures:
            plt.scatter(f.pos[0], f.pos[1], c = "green")
        for t in range(self.timesteps):
            plt.scatter(self.trajectories[t][0], self.trajectories[t][1], c = "blue", s = 0.2)
        print("Plot finished")
        # animator = Animator(sms = self, draw_trace=True)
        # animator.animate()
        plt.show()
        


class Animator:
    def __init__(self, sms, draw_trace = True):
        self.sms = sms
        self.draw_trace = draw_trace
        self.time = 0.0
  
        # set up the figure
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(-12, 12)
        self.ax.set_xlim(-12, 12)
  
        # prepare a text window for the timer
        self.time_text = self.ax.text(0.05, 0.95, '', 
            horizontalalignment='left', 
            verticalalignment='top', 
            transform=self.ax.transAxes)
  
        # initialize by plotting the last position of the trajectory
        self.line, = self.ax.plot(
            self.sms.trajectories[:][-1][:, 0], 
            self.sms.trajectories[-1][-1][:, 1], 
            marker='o')
          
        # trace the whole trajectory of the second pendulum mass
        if self.draw_trace:
            self.trace, = self.ax.plot(
                [a[2, 0] for a in self.pendulum.trajectory],
                [a[2, 1] for a in self.pendulum.trajectory])
     
    def advance_time_step(self):
        while True:
            self.time += self.sms.delta_t
            yield self.pendulum.evolve()
             
    def update(self, data):
        self.time_text.set_text('Elapsed time: {:6.2f} s'.format(self.time))
         
        self.line.set_ydata(data[:, 1])
        self.line.set_xdata(data[:, 0])
         
        if self.draw_trace:
            self.trace.set_xdata([a[2, 0] for a in self.pendulum.trajectory])
            self.trace.set_ydata([a[2, 1] for a in self.pendulum.trajectory])
        return self.line,
     
    def animate(self):
        self.animation = animation.FuncAnimation(self.fig, self.update,
                         self.advance_time_step, interval=25, blit=False, save_count = 100)
        self.animation.save('./anim.gif', writer='imagemagick', fps=50)
"""
pendulum = Pendulum(theta1=sp.pi, theta2=sp.pi - 0.01, dt=0.01)
animator = Animator(pendulum=pendulum, draw_trace=True)
animator.animate()
plt.show()
"""