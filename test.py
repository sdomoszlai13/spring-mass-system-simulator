from main import *


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
    s_1 = Spring(2, 1000, masses)
    print("Springs created.")
    return [s_1]


def create_system(fixtures, masses, springs):
    print("Creating spring mass system...")
    sms_1 = SpringMassSystem(fixtures, masses, springs)
    print("Spring mass system created.")
    return sms_1



f = create_fixture()
m = create_mass()
s = create_spring(m)
sms = create_system(f, m, s)
sms.run()