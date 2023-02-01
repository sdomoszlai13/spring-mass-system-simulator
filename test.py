from main import *

"""
def create_fixture():
    print("Creating fixtures...")
    fix_1 = Fixture([5, 3])
    fix_2 = Fixture([6, 4])
    print("Fixtures created.")
    return [fix_1, fix_2]

def create_mass():
    print("Creating masses...")
    m_1 = Mass(5, [2, 3], [8, 5])
    m_2 = Mass(3, [4, 3], [5, 6])
    print("Masses created.")
    return [m_1, m_2]

def create_spring(masses):
    print("Creating springs...")
    s_1 = Spring(2, 10, masses)
    s_2 = Spring(1, 20, )
    print("Springs created.")
    return [s_1, s_2]


def create_system(fixtures, masses, springs):
    print("Creating spring mass system...")
    sms_1 = SpringMassSystem(fixtures, masses, springs)
    print("Spring mass system created.")
    return sms_1

"""

def create_fixture():
    return np.array([Fixture([0.0, 10.0])])

def create_mass():
    return np.array([Mass(1, [-3.0, 3.0], [0.0, 0.0])])

def create_spring(f, m):
    return np.array([Spring(7.615, 1000.0, [f[0], m[0]])])

def create_system(f, m, s):
    return np.array([SpringMassSystem(f, m, s, time = 3, timesteps = 3000)])


f = create_fixture()
m = create_mass()
s = create_spring(f, m)
sms = create_system(f, m, s)
sms[0].run()