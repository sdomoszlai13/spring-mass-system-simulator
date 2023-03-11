# Spring Mass System Simulation

**This progam simulates a system of an arbitrary number of masses, fixtures and springs in a gravity field.**

When the fixtures, masses and spings are set up, the forces acting on the masses are calculated. This in turn allows to calculate their velocity and position. These steps are repeated for every time step. At the end, a plausibility check is performed by looking at the conservation of energy. At the beginning and at the end of the process, the total energy of the system is calculated and the values are compared. The total energy of the system at a given point in time is the sum of the kinetic and potential energies of all the masses and the potential energy of the springs (we assume massless springs). Ideally, the total energy of the system should not change with time. At the end, the trajectories of the masses are plotted.

The calculations are based on an Euler method. This is one of the simplest method to solve differential equations numerically. This project shows how much can be achieved even with a simple numerical method.

The images below show the results of some test cases.

The repository consists of 3 .py files:

* **main.py**: contains classes and functions for solving the equations of motion
* **test.py**: contains functions to create spring mass systems quickly
* **user_input.py**: contains functions for a simple CLI to create a spring mass system

To setup a system of springs and masses, run user_input.py and follow the prompts. The SI unit system is used in this simulation.
Note: if the time steps are too large, the simulation will become unstable and large errors will occur in the calculations. To prevent this, it is recommended to chosse at least 1,000 time steps for every second of simulation time.
Once you are done with the input, the simulation will run and a plot will be shown.
</br>
</br>

**Change log**

**V1.1:**</br>
Changes:
* Springs are now plotted at their initial positions
* Bug fixes


**V1.0:**</br>
Functionality:
* set up an arbitrary number of fixtures, masses and springs
* run the simulation for a desired time with a desired number of time steps (temporary resolution)
* perform a plausibility check by looking at the conservation of energy (known bug: sometimes wrong final point in trajectory and therefore wrong final energy)
* plot the trajectories of the masses
* save the trajectories of the masses in a text file

