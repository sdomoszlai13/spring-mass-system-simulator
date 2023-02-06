from main import *
# Input functionality

def smsInit():
    """User interface for data input"""

    print("To simulate a spring mass system, pass arrays of fixtures, masses, and springs.\n\n")

    # Get information for fixture(s)
    num_fixtures = int(input("Enter the number of fixtures you wish to simulate: "))
    print("\n\nThe input format for the properties of fixtures is: [x0, y0].")
    print("x0, y0: position of fixture\n\n")

    fixtures = []

    for i in range(num_fixtures):
        x = float(input(f"Enter x coordinate of fixture {i}: "))
        y = float(input(f"Enter y coordinate of fixture {i}: "))
        fixtures.append(Fixture(x, y))


    # Get information for mass(es)
    num_masses = int(input("Enter the number of masses you wish to simulate: "))
    print("\n\nThe input format for the properties of masses is: m, [x0, y0], [vx0, vy0].")
    print("m: mass")
    print("x0, y0: initial position of mass")
    print("vx0, vy0: initial velocity of mass\n\n")

    masses = []

    for i in range(num_masses):
        m = float(input(f"Enter mass of mass {i}: "))
        x0 = float(input(f"Enter x coordinate of initial position of mass {i}: "))
        y0 = float(input(f"Enter y coordinate of initial position of mass {i}: "))
        vx0 = float(input(f"Enter x component of initial velocity of mass {i}: "))
        vy0 = float(input(f"Enter y component of initial velocity of mass {i}: "))
        masses.append(Mass(m, x0, y0, vx0, vy0))


    # Get information for spring(s)
    num_springs = int(input("Enter the number of springs you wish to simulate: "))
    print("\n\nThe input format for the properties of springs is: l0, k, conn.")
    print("l0: rest length")
    print("k: spring constant")
    print("conn: connected fixture(s) and/or mass(es) in an array\n\n")

    springs = []

    for i in range(num_springs):
        l0 = float(input(f"Enter rest length of spring {i}: "))
        k = float(input(f"Enter spring constant of spring {i}: "))
        print("The name of the connected objects (mass(es) and/or spring(s)) is as follows:")
        print("m0 for the first mass, m1 for the second mass...")
        print("f0 for the first fixture, f1 for the second fixture...")
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

        
    # Get information for time, timestep and saving

    time = float(input("Simulation time: "))
    timesteps = int(input("Number of timesteps: "))
    save = input("Save to file [y/n]: ")

    if save == "y":
        save = True
            
    elif save == "n":
        save = False
            
    else:
    # Throw exception - TO DO
        pass

    return fixtures, masses, springs, time, timesteps, save


# Create SpringMassSystem object based on user input and run simulation
fixtures, masses, springs, time, timesteps, save = smsInit()
sms = SpringMassSystem(fixtures, masses, springs, time, timesteps, save)
sms.run()